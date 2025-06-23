from fastmcp import FastMCP
import asyncio
import logging
from typing import List, Dict, Any
import json
import uuid
import time
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create MCP server
mcp = FastMCP("LiveCodingMCPServer")

# Global variable to store the WebSocket manager reference
# This will be set by sse_server.py
websocket_manager = None

# Global dictionary to store pending code requests
pending_code_requests = {}

# Initialize Strudel documentation system
try:
    import sys
    sys.path.append(str(Path(__file__).parent / "llm_docs"))
    from strudel_docs_system_v2 import StrudelDocsSystemV2
    docs_system = StrudelDocsSystemV2()
    logger.info("Strudel documentation system v2 (faithful librarian) loaded successfully")
except Exception as e:
    docs_system = None
    logger.warning(f"Could not load Strudel documentation system: {e}")

def set_websocket_manager(manager):
    """Set the WebSocket manager from sse_server.py"""
    global websocket_manager
    websocket_manager = manager

def handle_code_response(request_id: str, code: str):
    """Handle code response from browser and resolve the pending request"""
    global pending_code_requests
    if request_id in pending_code_requests:
        future = pending_code_requests[request_id]
        if not future.done():
            future.set_result(code)
        del pending_code_requests[request_id]
        logger.info(f"Resolved code request {request_id} with {len(code)} characters")

async def _play_strudel_pattern_impl(code: str, description: str = "", session_id: str = "") -> str:
    """
    Internal implementation for playing Strudel patterns
    """
    global websocket_manager
    
    print(f"🔍 _play_strudel_pattern_impl called with session_id='{session_id}'")
    
    if not websocket_manager:
        return "❌ No WebSocket manager available. Is the web interface connected?"
    
    try:
        metadata = {"description": description} if description else {}
        
        message = {
            "type": "strudel-code",
            "code": code,
            "autoplay": True,
            "metadata": metadata,
            "timestamp": asyncio.get_event_loop().time()
        }
        
        print(f"🔍 Available sessions: {list(websocket_manager.session_connections.keys())}")
        
        # Send to specific session (now required)
        print(f"🔍 Attempting to send to session '{session_id}'")
        success = await websocket_manager.send_to_session(session_id, json.dumps(message))
        if success:
            print(f"✅ Successfully sent to session {session_id}")
            return f"🎵 Strudel pattern sent to session {session_id.upper()}. Pattern: {code[:50]}{'...' if len(code) > 50 else ''}"
        else:
            print(f"❌ Failed to send to session {session_id}")
            return f"❌ Session {session_id.upper()} not found. Make sure the browser is open with this session code."
            
    except Exception as e:
        logger.error(f"Error in play_strudel_pattern: {e}")
        return f"❌ Error playing pattern: {str(e)}"

def _validate_strudel_code(code: str) -> tuple[bool, str]:
    """
    Basic validation of Strudel code to catch common syntax errors
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not code or not code.strip():
        return False, "Code cannot be empty"
    
    # Check for basic syntax issues
    try:
        # Count parentheses
        if code.count('(') != code.count(')'):
            return False, "Mismatched parentheses"
        
        # Check for basic Strudel patterns
        if not any(keyword in code.lower() for keyword in ['note', 'sound', 's', 'n', 'stack', 'cat', 'seq']):
            return False, "Code doesn't appear to contain Strudel patterns (missing note/sound/s/n/stack/cat/seq)"
        
        # Check for dangerous patterns (basic security)
        dangerous = ['import', 'require', 'eval', 'function', 'window.', 'document.', 'fetch', 'xhr']
        if any(danger in code.lower() for danger in dangerous):
            return False, f"Code contains potentially dangerous elements: {[d for d in dangerous if d in code.lower()]}"
        
        return True, "Code validation passed"
        
    except Exception as e:
        return False, f"Validation error: {str(e)}"

@mcp.tool()
async def play_code(session_id: str, code: str = 'note("c d e f").s("piano").slow(2)', description: str = "") -> str:
    """
    Play live coding pattern in the connected browser
    
    Args:
        session_id: Required session ID (e.g. "fox8") to target specific browser
        code: The code to execute. Defaults to a simple piano scale
        description: Optional description of the pattern
    
    Returns:
        Status message indicating success or failure
    """
    print(f"🔍 play_code MCP tool called with session_id='{session_id}', code='{code[:30]}...'")
    
    # Validate code before sending
    is_valid, validation_message = _validate_strudel_code(code)
    if not is_valid:
        return f"Invalid code: {validation_message}"
    
    return await _play_strudel_pattern_impl(code, description, session_id)

@mcp.tool()
async def stop_play(session_id: str) -> str:
    """
    Stop playback in specific browser session
    
    Args:
        session_id: Required session ID (e.g. "fox8") to target specific browser
    
    Returns:
        Status message
    """
    global websocket_manager
    
    if not websocket_manager:
        return "No WebSocket manager available"
    
    try:
        message = {
            "type": "strudel-stop",
            "timestamp": asyncio.get_event_loop().time()
        }
        
        # Send to specific session (now required)
        success = await websocket_manager.send_to_session(session_id, json.dumps(message))
        if success:
            return f"Stop signal sent to session {session_id.upper()}"
        else:
            return f"❌ Session {session_id.upper()} not found. Make sure the browser is open with this session code."
        
    except Exception as e:
        logger.error(f"Error in stop_play: {e}")
        return f"Error stopping playback: {str(e)}"

@mcp.tool()
async def get_mcp_status(session_id: str) -> str:
    """
    Get the current status of specific MCP session
    
    Args:
        session_id: Required session ID (e.g. "fox8") to check specific browser status
    
    Returns:
        Status information about the specific browser session
    """
    global websocket_manager
    
    if not websocket_manager:
        return "WebSocket manager not available"
    
    connection_count = len(websocket_manager.active_connections)
    session_count = len(websocket_manager.session_connections)
    
    # Check specific session (now required)
    if session_id in websocket_manager.session_connections:
        return f"✅ Session {session_id.upper()} is connected and ready for live coding!"
    else:
        return f"❌ Session {session_id.upper()} not found. Make sure the browser is open with this session code."

@mcp.tool()
async def get_currently_playing_code(session_id: str) -> str:
    """
    Get the current code from the editor in specific browser session
    
    Args:
        session_id: Required session ID (e.g. "fox8") to get code from specific browser
    
    Returns:
        The actual code from the editor, or error message if session not found or timeout
    """
    global websocket_manager, pending_code_requests
    
    if not websocket_manager:
        return "WebSocket manager not available"
    
    connection_count = len(websocket_manager.active_connections)
    
    if connection_count == 0:
        return "No browsers currently connected. Open http://localhost:8080/strudel to get editor content!"
    
    if session_id not in websocket_manager.session_connections:
        return f"❌ Session {session_id.upper()} not found. Make sure the browser is open with this session code."
    
    try:
        # Generate unique request ID
        request_id = str(uuid.uuid4())
        
        # Create future to wait for response
        future = asyncio.Future()
        pending_code_requests[request_id] = future
        
        # Send request for current code to specific session
        message = {
            "type": "get-current-code",
            "request_id": request_id,
            "timestamp": asyncio.get_event_loop().time()
        }
        
        success = await websocket_manager.send_to_session(session_id, json.dumps(message))
        if not success:
            return f"❌ Failed to send request to session {session_id.upper()}"
        logger.info(f"Sent code request {request_id} to session {session_id}")
        
        # Wait for response with timeout
        try:
            code = await asyncio.wait_for(future, timeout=5.0)
            return f"Current editor code from session {session_id.upper()}:\n\n{code}"
        except asyncio.TimeoutError:
            # Clean up pending request
            if request_id in pending_code_requests:
                del pending_code_requests[request_id]
            return "Timeout waiting for browser response. Make sure the web interface is active and try again."
        
    except Exception as e:
        logger.error(f"Error requesting current code: {e}")
        return f"Error requesting current code: {str(e)}"

# Documentation tools - Faithful librarian approach
@mcp.tool()
async def get_strudel_docs(page: str = "", outline: str = "", format: str = "", related_to: str = "") -> str:
    """
    Get Strudel documentation - faithful to the original website structure.
    
    Args:
        page: Specific page path (e.g. "learn/samples", "workshop/first-sounds")
        outline: Show site structure ("true" for all, or category like "learn")
        format: "complete" for all pages concatenated, "printable" for organized reference
        related_to: Find pages related to a topic with descriptions
        
    Returns:
        Complete pages exactly as written, or site navigation
    """
    if not docs_system:
        return "Documentation system not available. Please check if docs are properly installed."
    
    try:
        if page:
            return docs_system.get_complete_page(page)
        elif outline:
            if outline.lower() == "true":
                return docs_system.get_site_outline()
            else:
                return docs_system.get_site_outline(outline)
        elif format == "complete" or format == "printable":
            return docs_system.get_all_pages_concatenated()
        elif related_to:
            return docs_system.find_related_pages(related_to)
        else:
            # Default: show site outline
            return docs_system.get_site_outline()
    except Exception as e:
        logger.error(f"Error accessing documentation: {e}")
        return f"Error accessing documentation: {str(e)}"

@mcp.tool()
async def get_strudel_examples(example_type: str = "all", function: str = "", concept: str = "", difficulty: str = "") -> str:
    """
    Get curated Strudel code examples from across all documentation pages.
    This is where the MCP adds value - collecting examples by theme.
    
    Args:
        example_type: Type of examples (drum_patterns, melodies, effects_chains, basic_patterns, polyrhythm)
        function: Get all examples using a specific function (e.g. "note", "lpf", "delay")
        concept: Get examples for a concept (drums, timing, effects, chords, patterns, bass, melody)
        difficulty: Get examples by level (beginner, intermediate, advanced)
        
    Returns:
        Curated code examples with source page attribution
    """
    if not docs_system:
        return "Documentation system not available. Please check if docs are properly installed."
    
    try:
        return docs_system.get_curated_examples(example_type, function, concept, difficulty)
    except Exception as e:
        logger.error(f"Error getting examples: {e}")
        return f"Error getting examples: {str(e)}"

@mcp.tool()
async def get_strudel_page_info(topic: str) -> str:
    """
    Find documentation pages related to a topic with navigation help.
    
    Args:
        topic: What you're looking for (e.g. "samples", "timing", "effects")
        
    Returns:
        Related page paths with descriptions and how to read them
    """
    if not docs_system:
        return "Documentation system not available."
    
    try:
        return docs_system.find_related_pages(topic)
    except Exception as e:
        logger.error(f"Error finding related pages: {e}")
        return f"Error finding related pages: {str(e)}"

@mcp.tool()
async def search_strudel_functions(query: str, limit: int = 10) -> str:
    """
    Search for Strudel functions by name or description.
    
    Args:
        query: Search term (function name, keyword, or concept)
        limit: Maximum number of results to return (default 10)
        
    Returns:
        Matching functions with descriptions and examples
    """
    if not docs_system:
        return "Documentation system not available."
    
    try:
        return docs_system.search_functions(query, limit)
    except Exception as e:
        logger.error(f"Error searching functions: {e}")
        return f"Error searching functions: {str(e)}"


@mcp.tool()
async def get_strudel_quick_reference() -> str:
    """
    Get a quick reference guide for common Strudel patterns and functions.
    
    Returns:
        Quick reference guide with essential Strudel syntax
    """
    return """# Strudel Quick Reference

## Basic Patterns
- `note("c d e f")` - Play notes (C D E F)
- `note("c3 e3 g3")` - Play chord (C major)
- `note("<c d e f>")` - Sequence through notes
- `s("bd sd hh")` - Basic drum samples (kick, snare, hihat)

## Timing
- `.slow(2)` - Half speed
- `.fast(2)` - Double speed  
- `*4` - Repeat 4 times per cycle
- `/2` - Every other cycle

## Structure  
- `stack(pattern1, pattern2)` - Layer patterns
- `"<a b c>"` - Sequence through values
- `"a [b c] d"` - Subdivision (b and c share one beat)
- `"a ~ b ~"` - Rests (~)

## Effects
- `.gain(0.5)` - Volume (0 to 1)
- `.lpf(800)` - Low-pass filter
- `.delay(0.3)` - Echo
- `.room(0.3)` - Reverb
- `.pan(0.5)` - Stereo position

## Basic Examples
- Simple melody: `note("c d e f").s("piano").slow(2)`
- Basic rhythm: `s("bd ~ sd ~")`
- Chord progression: `note("<c3 f3 g3 c3>").s("piano")`
- Layered pattern: `stack(note("c d e f").s("piano"), s("bd sd"))`
"""

if __name__ == "__main__":
    # Run the MCP server in stdio mode
    mcp.run()
