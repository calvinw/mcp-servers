import os
import sys
from fastmcp import FastMCP
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

if __name__ == "__main__":
    # Check command line argument for transport type
    transport = sys.argv[1] if len(sys.argv) > 1 else "http"
    
    if transport == "stdio":
        print("Greet Service - Running as MCP server (stdio)")
        mcp.run()
    else:  # http
        port = int(os.environ.get("PORT", 8080))
        print(f"Greet Service - MCP endpoint: http://localhost:{port}/mcp")
        
        # Create the HTTP app
        http_app = mcp.http_app(transport="http", path="/mcp")
        uvicorn.run(http_app, host="0.0.0.0", port=port)
