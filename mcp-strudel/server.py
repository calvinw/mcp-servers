from fastmcp import FastMCP
import asyncio
import logging
from typing import List, Dict, Any
import json
import uuid
import time

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

async def _play_strudel_pattern_impl(code: str, description: str = "") -> str:
    """
    Internal implementation for playing Strudel patterns
    """
    global websocket_manager
    
    if not websocket_manager:
        return "❌ No WebSocket manager available. Is the web interface connected?"
    
    try:
        metadata = {"description": description} if description else {}
        
        # Send the code to all connected browsers
        message = {
            "type": "strudel-code",
            "code": code,
            "autoplay": True,
            "metadata": metadata,
            "timestamp": asyncio.get_event_loop().time()
        }
        
        await websocket_manager.broadcast(json.dumps(message))
        
        connection_count = len(websocket_manager.active_connections)
        
        if connection_count > 0:
            return f"🎵 Strudel pattern sent to {connection_count} connected browser(s). Pattern: {code[:50]}{'...' if len(code) > 50 else ''}"
        else:
            return "⚠️ Pattern ready, but no browsers connected. Open the web interface to hear it!"
            
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
async def play_code(code: str = 'note("c d e f g").s("piano").slow(2)', description: str = "") -> str:
    """
    Play live coding pattern in the connected browser
    
    Args:
        code: The code to execute. Defaults to a simple piano scale
        description: Optional description of the pattern
    
    Returns:
        Status message indicating success or failure
    """
    # Validate code before sending
    is_valid, validation_message = _validate_strudel_code(code)
    if not is_valid:
        return f"Invalid code: {validation_message}"
    
    return await _play_strudel_pattern_impl(code, description)

@mcp.tool()
async def stop_play() -> str:
    """
    Stop all playback in connected browsers
    
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
        
        await websocket_manager.broadcast(json.dumps(message))
        
        connection_count = len(websocket_manager.active_connections)
        return f"Stop signal sent to {connection_count} connected browser(s)"
        
    except Exception as e:
        logger.error(f"Error in stop_play: {e}")
        return f"Error stopping playback: {str(e)}"

@mcp.tool()
async def get_mcp_status() -> str:
    """
    Get the current status of MCP connections
    
    Returns:
        Status information about connected browsers
    """
    global websocket_manager
    
    if not websocket_manager:
        return "WebSocket manager not available"
    
    connection_count = len(websocket_manager.active_connections)
    
    if connection_count == 0:
        return "No browsers currently connected. Open http://localhost:8080/strudel to start jamming!"
    else:
        return f"{connection_count} browser(s) connected and ready for live coding!"

@mcp.tool()
async def get_currently_playing_code() -> str:
    """
    Get the current code from the editor in connected browsers
    
    Returns:
        The actual code from the editor, or error message if no browsers connected or timeout
    """
    global websocket_manager, pending_code_requests
    
    if not websocket_manager:
        return "WebSocket manager not available"
    
    connection_count = len(websocket_manager.active_connections)
    
    if connection_count == 0:
        return "No browsers currently connected. Open http://localhost:8080/strudel to get editor content!"
    
    try:
        # Generate unique request ID
        request_id = str(uuid.uuid4())
        
        # Create future to wait for response
        future = asyncio.Future()
        pending_code_requests[request_id] = future
        
        # Send request for current code to all connected browsers
        message = {
            "type": "get-current-code",
            "request_id": request_id,
            "timestamp": asyncio.get_event_loop().time()
        }
        
        await websocket_manager.broadcast(json.dumps(message))
        logger.info(f"Sent code request {request_id} to {connection_count} browser(s)")
        
        # Wait for response with timeout
        try:
            code = await asyncio.wait_for(future, timeout=5.0)
            return f"Current editor code:\n\n{code}"
        except asyncio.TimeoutError:
            # Clean up pending request
            if request_id in pending_code_requests:
                del pending_code_requests[request_id]
            return "Timeout waiting for browser response. Make sure the web interface is active and try again."
        
    except Exception as e:
        logger.error(f"Error requesting current code: {e}")
        return f"Error requesting current code: {str(e)}"

# Pattern examples database
EXAMPLES = {
    "kick": {
        "code": 's("bd bd bd bd")',
        "description": "Four-on-the-floor kick pattern"
    },
    "snare": {
        "code": 's("~ sd ~ sd")',
        "description": "Backbeat snare on 2 and 4"
    },
    "hihat": {
        "code": 's("hh*4").gain(0.6)',
        "description": "Steady hi-hat groove"
    },
    "bass": {
        "code": 'note("c2 ~ eb2 ~ f2 ~ g2 ~").s("sawtooth").lpf(800)',
        "description": "Deep filtered bass line"
    },
    "melody": {
        "code": 'note("c4 d4 e4 f4 g4 f4 e4 d4").s("triangle").slow(2)',
        "description": "Simple ascending melody"
    },
    "complex": {
        "code": '''stack(
  note("c2 eb2 g2 bb2").s("sawtooth").lpf(400).slow(2),
  note("c4 d4 eb4 f4 g4 ab4 bb4 c5").s("triangle").gain(0.7),
  s("bd ~ bd ~").fast(1.5)
)''',
        "description": "Layered bass, melody and drums"
    },
    "ambient": {
        "code": 'note("c4 g4 e5 c5").s("sawtooth").slow(4).room(0.8).delay(0.5)',
        "description": "Spacey ambient texture"
    },
    "arpeggio": {
        "code": 'note("c4 e4 g4 c5 g4 e4").fast(2).s("square").lpf(sine.range(400, 2000))',
        "description": "Filtered square wave arpeggio"
    },
    "polyrhythm": {
        "code": 'stack(s("bd*3"), s("~ sd ~ sd ~ sd"), s("hh*8").gain(0.4))',
        "description": "Complex polyrhythmic drums"
    },
    "chord": {
        "code": 'note("<c4 e4 g4>").s("piano").slow(2).room(0.3)',
        "description": "Simple piano chord progression"
    }
}

@mcp.tool()
async def get_example_names() -> str:
    """
    Get list of all available example pattern names
    
    Returns:
        List of available pattern names with descriptions
    """
    result = "Available example patterns:\n\n"
    for name, data in EXAMPLES.items():
        result += f"- {name}: {data['description']}\n"
    return result

@mcp.tool()
async def get_example_code(name: str = "complex") -> str:
    """
    Get the code for a specific example pattern
    
    Args:
        name: Name of the pattern (use get_example_names to see available options). Defaults to "complex"
    
    Returns:
        The code for the pattern, or error if not found
    """
    if name not in EXAMPLES:
        available = ", ".join(EXAMPLES.keys())
        return f"Unknown pattern '{name}'. Available patterns: {available}"
    
    example = EXAMPLES[name]
    return f"Pattern: {name}\nDescription: {example['description']}\n\nCode:\n{example['code']}"

if __name__ == "__main__":
    # Run the MCP server in stdio mode
    mcp.run()
