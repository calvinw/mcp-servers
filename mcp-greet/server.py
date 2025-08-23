# server.py
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse  # <-- fixes NameError
from fastmcp import FastMCP

# 1) Create MCP server and tools
mcp = FastMCP("Authless Demo")

@mcp.tool()
def add_numbers(a: float, b: float) -> dict:
    return {"a": a, "b": b, "result": a + b}

@mcp.tool()
def ping(msg: str = "hello") -> str:
    return f"pong: {msg}"

# 2) Build inner ASGI app that exposes MCP at /mcp (no trailing slash)
inner = mcp.http_app(path="/mcp")  # choose "/mcp/" only if you will ALWAYS use a trailing slash

# 3) OUTER FastAPI owns lifespan of the inner MCP app
app = FastAPI(lifespan=inner.lifespan, title="Authless FastMCP")

# IMPORTANT: turn off slash redirects to avoid 307 between /mcp and /mcp/
app.router.redirect_slashes = False

# 4) Apply CORS to the *mounted* app (outer middleware won't apply to mounted apps)
inner_with_cors = CORSMiddleware(
    inner,
    allow_origins=["*"],  # authless; lock down if you want later
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 5) Mount the MCP app at root so the final path is exactly /mcp
app.mount("/", inner_with_cors)

# Optional: health check
@app.get("/healthz")
def health():
    return {"ok": True, "server": "Authless FastMCP"}

# Optional: if you keep an OAuth metadata endpoint around, this fixes your JSONResponse error
@app.get("/.well-known/oauth-authorization-server")
def oauth_metadata():
    # For authless you don't need real OAuth; safe to delete this route.
    return JSONResponse({
        "issuer": "https://your-domain.example",
        "authorization_endpoint": "https://example.invalid/noop",
        "token_endpoint": "https://example.invalid/noop",
        "scopes_supported": []
    })

if __name__ == "__main__":
    # 0.0.0.0 so containers/VMs expose it; change port as needed
    uvicorn.run(app, host="0.0.0.0", port=8080)

