import os
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse, FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
import json
import logging
from typing import List
from pathlib import Path
from server import mcp, set_websocket_manager, handle_code_response

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# WebSocket connection manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        logger.info(f"New WebSocket connection. Total: {len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
        logger.info(f"WebSocket disconnected. Total: {len(self.active_connections)}")

    async def broadcast(self, message: str):
        """Send message to all connected clients"""
        disconnected = []
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except Exception as e:
                logger.error(f"Error broadcasting to connection: {e}")
                disconnected.append(connection)
        
        # Remove disconnected clients
        for connection in disconnected:
            self.disconnect(connection)

# Create WebSocket manager and make it available to server.py
manager = ConnectionManager()
set_websocket_manager(manager)

# Create the ASGI app for MCP
http_app = mcp.http_app(transport="sse", path='/sse')

# Minimal OAuth endpoint (just enough for Claude.ai)
async def oauth_metadata(request: Request):
    base_url = str(request.base_url).rstrip("/")
    return JSONResponse({
        "issuer": base_url
    })

# Create a FastAPI app and mount the MCP server
app = FastAPI(lifespan=http_app.lifespan, title="Strudel MCP Server")

# Add CORS middleware with WebSocket support
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Access-Control-Allow-Origin
    allow_methods=["GET", "POST", "OPTIONS", "PUT", "DELETE"],  # Access-Control-Allow-Methods
    allow_headers=["Content-Type", "Authorization", "x-api-key", "Upgrade", "Connection", "Sec-WebSocket-Key", "Sec-WebSocket-Version", "Sec-WebSocket-Protocol"],  # Access-Control-Allow-Headers
    expose_headers=["Content-Type", "Authorization", "x-api-key"],  # Access-Control-Expose-Headers
    max_age=86400  # Access-Control-Max-Age (in seconds)
)

# Add the OAuth metadata route before mounting
app.add_api_route("/.well-known/oauth-authorization-server", oauth_metadata, methods=["GET"])


# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Add route to serve the Strudel player
@app.get("/strudel", response_class=FileResponse)
async def serve_strudel_player():
    """Serve the Strudel live coding interface"""
    return FileResponse("static/index.html")

# WebSocket endpoint for real-time communication
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time communication with the Strudel player"""
    logger.info(f"WebSocket connection attempt from: {websocket.client}")
    try:
        await manager.connect(websocket)
        logger.info(f"WebSocket connected successfully. Total connections: {len(manager.active_connections)}")
    except Exception as e:
        logger.error(f"WebSocket connection failed: {e}")
        raise
    
    try:
        while True:
            # Listen for messages from the client
            data = await websocket.receive_text()
            try:
                message = json.loads(data)
                if message.get("type") == "ping":
                    await websocket.send_text(json.dumps({"type": "pong"}))
                elif message.get("type") == "evaluation-error":
                    # Log client-side evaluation errors
                    error_msg = message.get("error", "Unknown error")
                    code_snippet = message.get("code", "Unknown code")
                    logger.error(f"Client-side Strudel evaluation error: {error_msg} | Code: {code_snippet}")
                elif message.get("type") == "current-code-response":
                    # Handle code response and resolve pending request
                    current_code = message.get("code", "")
                    request_id = message.get("request_id", "")
                    timestamp = message.get("timestamp", "")
                    logger.info(f"Received current editor code ({len(current_code)} chars): {current_code[:100]}{'...' if len(current_code) > 100 else ''}")
                    
                    # Resolve the pending MCP request
                    if request_id:
                        handle_code_response(request_id, current_code)
            except json.JSONDecodeError:
                logger.warning(f"Invalid JSON received: {data}")
                
    except WebSocketDisconnect:
        manager.disconnect(websocket)

# Add a simple status endpoint
@app.get("/api/status")
async def get_status():
    """Get current server status"""
    return {
        "server": "running",
        "mcp_tools": "active", 
        "websocket_connections": len(manager.active_connections),
        "strudel_interface": "/strudel"
    }

# Add WebSocket test endpoint
@app.get("/ws-test")
async def websocket_test():
    """Test endpoint to verify WebSocket route is accessible"""
    return {
        "websocket_endpoint": "/ws",
        "status": "WebSocket endpoint should be accessible",
        "active_connections": len(manager.active_connections)
    }

# Mount the MCP server to handle SSE - must be AFTER all other routes
app.mount("/", http_app)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    
    print(f"""
🎵 Strudel MCP Server Starting!

- MCP Tools: http://localhost:{port}/sse
- Strudel Player: http://localhost:{port}/strudel
- Server Status: http://localhost:{port}/api/status

Ready for live coding with Claude! 🤖🎶
    """)
    
    uvicorn.run(app, host="0.0.0.0", port=port)
