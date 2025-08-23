# server.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastmcp import FastMCP
import uvicorn

mcp = FastMCP("Authless Demo")

@mcp.tool()
def add_numbers(a: float, b: float) -> dict:
    return {"a": a, "b": b, "result": a + b}

@mcp.tool()
def ping(msg: str = "hello") -> str:
    return f"pong: {msg}"

# Make an ASGI app that serves MCP at /mcp  (you can also choose "/mcp/")
mcp_app = mcp.http_app(path="/mcp")   # <- IMPORTANT

# Your outer FastAPI app; adopt the MCP app's lifespan
app = FastAPI(lifespan=mcp_app.lifespan, title="Authless FastMCP")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Minimal OAuth endpoint (just enough for Claude.ai)
async def oauth_metadata(request: Request):
    base_url = str(request.base_url).rstrip("/")
    return JSONResponse({
        "issuer": base_url
    })

# Add the OAuth metadata route before mounting
app.add_api_route("/.well-known/oauth-authorization-server", oauth_metadata, methods=["GET"])

# Mount the MCP app at root so its path is exactly /mcp
app.mount("/", mcp_app)

# Optional extra routes on the outer app are fine:
@app.get("/healthz")
def health():
    return {"ok": True}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)


