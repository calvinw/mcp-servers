from fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("MyGreetServer")

@mcp.tool()
def add_numbers(a: float = 10.0, b: float = 5.0) -> dict:
    """Add two numbers"""
    return {"a": a, "b": b, "result": a + b}

@mcp.tool()
def greet(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}! Nice to meet you."

@mcp.tool()
def greet_warmly(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}! So great to see you."

@mcp.tool()
def get_sample_markdown_table() -> str:
    """Markdown table."""
    return f"""
    | Header 1 | Header 2 |
    |----------|----------|
    | Cell 1   | Cell 2   |
    | Cell 3   | Cell 4   |
    """

if __name__ == "__main__":
    # Run the MCP server in stdio mode
    mcp.run()
