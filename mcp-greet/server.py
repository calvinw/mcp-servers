# server.py
import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastmcp import FastMCP

# ---- MCP server + tools ----
mcp = FastMCP("Authless Demo")

@mcp.tool()
def add_numbers(a: float, b: float) -> dict:
    return {"a": a, "b": b, "result": a + b}

@mcp.tool()
def ping(msg: str = "hello") -> str:
    return f"pong: {msg}"

# Serve MCP at /mcp/ (trailing slash helps avoid proxy 307s)
inner = mcp.http_app(path="/mcp/")

# ---- Outer FastAPI ----
app = FastAPI(lifespan=inner.lifespan, title="Authless FastMCP")
app.router.redirect_slashes = False

# Apply CORS to the mounted inner app
inner_with_cors = CORSMiddleware(
    inner,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- Helpers for PRM ----
def _public_base(request: Request) -> str:
    proto = request.headers.get("x-forwarded-proto") or request.url.scheme
    host  = request.headers.get("x-forwarded-host") or request.headers.get("host") or request.url.netloc
    return f"{proto}://{host}"

def _resource_id(request: Request) -> str:
    # MUST match your MCP endpoint exactly; we chose /mcp/
    return f"{_public_base(request)}/mcp/"

# ---- Your existing OAS metadata (kept exactly, added before mount) ----
async def oauth_metadata(request: Request):
    base_url = str(request.base_url).rstrip("/")
    return JSONResponse({"issuer": base_url})

app.add_api_route(
    "/.well-known/oauth-authorization-server",
    oauth_metadata,
    methods=["GET"],
)

app.add_api_route(
    "/.well-known/oauth-authorization-server/mcp",
    oauth_metadata,
    methods=["GET"],
)

app.add_api_route(
    "/.well-known/oauth-authorization-server/mcp/",
    oauth_metadata,
    methods=["GET"],
)

# ---- Add PRM (authless) and DCR stub BEFORE mounting ----
async def prm_scoped(request: Request):
    return JSONResponse({
        "resource": _resource_id(request),
        "bearer_methods_supported": [],  # authless: no bearer methods
        "scopes_supported": [],
        # omit "authorization_servers" to signal no OAuth for this resource
    })

async def prm_root(request: Request):
    return JSONResponse({
        "resource": _public_base(request),
        "bearer_methods_supported": [],
        "scopes_supported": [],
    })

async def dcr_noop():
    return Response(status_code=204)

# PRM at both with/without trailing slash
app.add_api_route("/.well-known/oauth-protected-resource/mcp/", prm_scoped, methods=["GET"])
app.add_api_route("/.well-known/oauth-protected-resource/mcp", prm_scoped, methods=["GET"])
app.add_api_route("/.well-known/oauth-protected-resource/mcp/", prm_scoped, methods=["GET"])
# Optional host-level PRM
app.add_api_route("/.well-known/oauth-protected-resource", prm_root, methods=["GET"])

# No-op dynamic client registration
app.add_api_route("/register", dcr_noop, methods=["POST"])

# ---- Mount MCP app last so final path is exactly /mcp/ ----
app.mount("/", inner_with_cors)

# Health (optional)
@app.get("/healthz")
def health():
    return {"ok": True, "server": "Authless FastMCP"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
