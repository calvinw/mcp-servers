import os
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse, FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
import json
import logging
from typing import List, Dict
from pathlib import Path
import random
import string
from server import mcp, set_websocket_manager, handle_code_response

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# WebSocket connection manager with session support
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.session_connections: Dict[str, WebSocket] = {}  # session_id -> websocket

    async def connect(self, websocket: WebSocket, session_id: str = None):
        await websocket.accept()
        self.active_connections.append(websocket)
        if session_id:
            self.session_connections[session_id] = websocket
            print(f"🔍 WebSocket connected with session_id='{session_id}'")
            print(f"🔍 Current sessions: {list(self.session_connections.keys())}")
            logger.info(f"New WebSocket connection with session {session_id}. Total: {len(self.active_connections)}")
        else:
            print(f"🔍 WebSocket connected without session_id")
            logger.info(f"New WebSocket connection. Total: {len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
        # Remove from session connections
        session_to_remove = None
        for session_id, ws in self.session_connections.items():
            if ws == websocket:
                session_to_remove = session_id
                break
        if session_to_remove:
            del self.session_connections[session_to_remove]
            logger.info(f"WebSocket disconnected (session {session_to_remove}). Total: {len(self.active_connections)}")
        else:
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
    
    async def send_to_session(self, session_id: str, message: str) -> bool:
        """Send message to specific session. Returns True if successful."""
        print(f"🔍 send_to_session called with session_id='{session_id}'")
        print(f"🔍 Available sessions: {list(self.session_connections.keys())}")
        
        if session_id in self.session_connections:
            try:
                print(f"✅ Found session {session_id}, sending message")
                await self.session_connections[session_id].send_text(message)
                return True
            except Exception as e:
                print(f"❌ Error sending to session {session_id}: {e}")
                logger.error(f"Error sending to session {session_id}: {e}")
                self.disconnect(self.session_connections[session_id])
                return False
        else:
            print(f"❌ Session {session_id} not found in connections")
            return False
    
    def generate_session_id(self) -> str:
        """Generate a memorable 4-character session ID (3 letters + 1 digit)"""
        while True:
            letters = ''.join(random.choices(string.ascii_lowercase, k=3))
            digit = random.choice(string.digits)
            session_id = letters + digit
            # Ensure it's not already in use
            if session_id not in self.session_connections:
                return session_id

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

# Add route to serve the Strudel player with session ID
@app.get("/strudel")
async def serve_strudel_player():
    """Serve the Strudel live coding interface with session ID"""
    session_id = manager.generate_session_id()
    
    # Read the HTML template
    html_content = open("static/index.html", "r").read()
    
    # Inject session ID into the HTML
    html_content = html_content.replace(
        '<!-- SESSION_ID_PLACEHOLDER -->', 
        f'<script>window.sessionId = "{session_id}";</script>'
    )
    
    return HTMLResponse(content=html_content)

# WebSocket endpoint for real-time communication
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, session_id: str = None):
    """WebSocket endpoint for real-time communication with the Strudel player"""
    logger.info(f"WebSocket connection attempt from: {websocket.client}")
    
    # Get session_id from query parameters
    session_id = websocket.query_params.get('session_id')
    print(f"🔍 WebSocket endpoint called with session_id='{session_id}' from query params")
    
    try:
        await manager.connect(websocket, session_id)
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
