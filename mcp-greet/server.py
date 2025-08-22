import os
import sys
from fastmcp import FastMCP
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Create MCP server
mcp = FastMCP("MyGreetServer")

@mcp.tool()
def add_numbers(a: float = 10.0, b: float = 5.0) -> dict:
    """Add two numbers"""
    return {"a": a, "b": b, "result": a + b}

@mcp.tool()
def greet(name: str = "Calvin") -> str:
    """Greet someone by name."""
    return f"Hello, {name}! Nice to meet you."
    
@mcp.tool()
def get_some_sample_markdown() -> str:
    """Some sample markdown."""
    return f"""
    This is *Italic*   
    This is **Bold**  
    This is some LaTeX $x=434$  

    - First 
    - Second 

    | Header 1 | Header 2 |
    |----------|----------|
    | Cell 1   | Cell 2   |
    | Cell 3   | Cell 4   |
    """

# Minimal OAuth endpoint (just enough for Claude.ai)
async def oauth_metadata(request: Request):
    base_url = str(request.base_url).rstrip("/")
    return JSONResponse({
        "issuer": base_url
    })

# Create the ASGI app for SSE transport
http_app = mcp.http_app(transport="http", path='/mcp')

# Create a FastAPI app and mount the MCP server
app = FastAPI(lifespan=http_app.lifespan)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Access-Control-Allow-Origin
    allow_methods=["GET", "POST", "OPTIONS"],  # Access-Control-Allow-Methods
    allow_headers=["Content-Type", "Authorization", "x-api-key"],  # Access-Control-Allow-Headers
    expose_headers=["Content-Type", "Authorization", "x-api-key"],  # Access-Control-Expose-Headers
    max_age=86400  # Access-Control-Max-Age (in seconds)
)

# Add the OAuth metadata route before mounting
app.add_api_route("/.well-known/oauth-authorization-server", oauth_metadata, methods=["GET"])

# Mount the MCP server
app.mount("/", http_app)

if __name__ == "__main__":
    # Check command line argument for transport type
    transport = sys.argv[1] if len(sys.argv) > 1 else "sse"
    
    if transport == "stdio":
        print("Greet Service - Running as MCP server (stdio)")
        mcp.run()
    else:  # sse
        port = int(os.environ.get("PORT", 8080))
        print(f"Greet Service - MCP endpoint: http://localhost:{port}/mcp")
        uvicorn.run("server:app", host="0.0.0.0", port=port, reload=True)
