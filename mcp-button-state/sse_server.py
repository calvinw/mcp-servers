import os
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse, FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
import json
import logging
from typing import List, Dict, Any
from pathlib import Path
import random
import string
from server import mcp, set_websocket_manager, handle_state_response

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
            logger.info(f"New WebSocket connection with session {session_id}. Total: {len(self.active_connections)}")
        else:
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
        if session_id in self.session_connections:
            try:
                await self.session_connections[session_id].send_text(message)
                return True
            except Exception as e:
                logger.error(f"Error sending to session {session_id}: {e}")
                self.disconnect(self.session_connections[session_id])
                return False
        else:
            return False
    
    def has_connections(self) -> bool:
        """Check if there are any active connections"""
        return len(self.active_connections) > 0
    
    def get_connection_count(self) -> int:
        """Get the number of active connections"""
        return len(self.active_connections)
    
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

# Wrap with FastAPI
app = FastAPI(title="Button State MCP Server")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
static_path = Path(__file__).parent / "static"
if static_path.exists():
    app.mount("/static", StaticFiles(directory=str(static_path)), name="static")

@app.get("/")
async def root():
    """Root endpoint that redirects to the button interface"""
    return JSONResponse({
        "message": "Button State MCP Server",
        "interfaces": {
            "mcp": "/sse",
            "button": "/button",
            "websocket": "/ws"
        }
    })

@app.get("/debug/connections")
async def debug_connections():
    """Debug endpoint to see active connections"""
    return JSONResponse({
        "total_connections": len(manager.active_connections),
        "session_connections": list(manager.session_connections.keys()),
        "has_connections": manager.has_connections()
    })

@app.get("/button")
async def button_interface():
    """Serve the button interface HTML page"""
    session_id = manager.generate_session_id()
    
    # Read the HTML template
    html_path = Path(__file__).parent / "static" / "index.html"
    if not html_path.exists():
        return HTMLResponse("""
        <html>
            <head><title>Button Interface Not Found</title></head>
            <body>
                <h1>Button Interface Not Found</h1>
                <p>The static/index.html file is missing.</p>
            </body>
        </html>
        """)
    
    with open(html_path, 'r') as f:
        html_content = f.read()
    
    # Replace placeholder with actual session ID
    html_content = html_content.replace('SESSION_ID_PLACEHOLDER', session_id)
    
    return HTMLResponse(html_content)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, session_id: str = None):
    """WebSocket endpoint for real-time communication with button interface"""
    # Get session_id from query parameters
    session_id = websocket.query_params.get('session_id')
    logger.info(f"WebSocket connection attempt with session_id='{session_id}'")
    
    await manager.connect(websocket, session_id)
    
    try:
        while True:
            # Receive message from client
            data = await websocket.receive_text()
            
            try:
                message = json.loads(data)
                logger.info(f"Received WebSocket message: {message}")
                
                # Handle different message types
                if message.get('type') == 'button-state-response':
                    # Handle button state response from client
                    request_id = message.get('request_id')
                    state = message.get('state', {})
                    
                    if request_id:
                        handle_state_response(request_id, state)
                    
                elif message.get('type') == 'ping':
                    # Respond to ping
                    await websocket.send_text(json.dumps({'type': 'pong'}))
                    
                else:
                    logger.warning(f"Unknown message type: {message.get('type')}")
                    
            except json.JSONDecodeError:
                logger.error(f"Invalid JSON received: {data}")
            except Exception as e:
                logger.error(f"Error processing WebSocket message: {e}")
                
    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
        manager.disconnect(websocket)

@app.get("/oauth/metadata")
async def oauth_metadata():
    """OAuth metadata endpoint for MCP client discovery"""
    return JSONResponse({
        "authorization_endpoint": "https://example.com/oauth/authorize",
        "token_endpoint": "https://example.com/oauth/token"
    })

# Mount the MCP server to handle SSE - must be AFTER all other routes
app.mount("/", http_app)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8001))
    uvicorn.run(app, host="0.0.0.0", port=port)