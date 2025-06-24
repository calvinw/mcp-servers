from fastmcp import FastMCP
import asyncio
import logging
import json
import uuid
import time
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create MCP server
mcp = FastMCP("ButtonStateMCPServer")

# Global variable to store the WebSocket manager reference
# This will be set by sse_server.py
websocket_manager = None

# Global dictionary to store pending state requests
pending_state_requests = {}

def set_websocket_manager(manager):
    """Set the WebSocket manager from sse_server.py"""
    global websocket_manager
    websocket_manager = manager

def handle_state_response(request_id: str, state: Dict[str, Any]):
    """Handle state response from browser and resolve the pending request"""
    global pending_state_requests
    if request_id in pending_state_requests:
        future = pending_state_requests[request_id]
        if not future.done():
            future.set_result(state)
        del pending_state_requests[request_id]
        logger.info(f"Resolved state request {request_id} with state: {state}")

@mcp.tool()
async def get_button_state(session_id: str = "") -> str:
    """
    Get the current button state from the web interface via WebSocket.
    
    Args:
        session_id: Optional session ID to target specific browser connection
        
    Returns:
        JSON string containing the current Zustand state from the web interface
    """
    global websocket_manager, pending_state_requests
    
    if not websocket_manager:
        return json.dumps({
            "error": "WebSocket manager not available",
            "status": "disconnected"
        })
    
    # Check if there are any connected clients
    if not websocket_manager.has_connections():
        return json.dumps({
            "error": "No web interface clients connected",
            "status": "no_clients"
        })
    
    # Generate unique request ID
    request_id = str(uuid.uuid4())
    
    # Create a future to wait for the response
    future = asyncio.Future()
    pending_state_requests[request_id] = future
    
    # Send request to get current state
    message = {
        "type": "get-button-state",
        "request_id": request_id,
        "timestamp": int(time.time() * 1000)
    }
    
    try:
        # Broadcast the request to all connected clients (or specific session)
        if session_id:
            await websocket_manager.send_to_session(session_id, json.dumps(message))
        else:
            await websocket_manager.broadcast(json.dumps(message))
        
        logger.info(f"Sent button state request {request_id}")
        
        # Wait for response with timeout
        try:
            state = await asyncio.wait_for(future, timeout=10.0)
            return json.dumps({
                "status": "success",
                "state": state,
                "request_id": request_id,
                "timestamp": int(time.time() * 1000)
            })
        except asyncio.TimeoutError:
            # Clean up the pending request
            if request_id in pending_state_requests:
                del pending_state_requests[request_id]
            return json.dumps({
                "error": "Timeout waiting for state response from web interface",
                "status": "timeout",
                "request_id": request_id
            })
            
    except Exception as e:
        # Clean up the pending request
        if request_id in pending_state_requests:
            del pending_state_requests[request_id]
        logger.error(f"Error getting button state: {e}")
        return json.dumps({
            "error": f"Failed to get button state: {str(e)}",
            "status": "error"
        })

@mcp.tool()
async def get_connection_status() -> str:
    """
    Get the status of WebSocket connections to the web interface.
    
    Returns:
        JSON string with connection status information
    """
    global websocket_manager
    
    if not websocket_manager:
        return json.dumps({
            "status": "disconnected",
            "message": "WebSocket manager not available"
        })
    
    connection_count = websocket_manager.get_connection_count()
    
    return json.dumps({
        "status": "connected" if connection_count > 0 else "no_clients",
        "connection_count": connection_count,
        "message": f"{connection_count} client(s) connected"
    })

if __name__ == "__main__":
    # Run the MCP server
    mcp.run()