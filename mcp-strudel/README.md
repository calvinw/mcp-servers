# MCP Greet  

This project is an example of an MCP server.

## Setup Instructions

1.  **Install dependencies.**
    This project uses `uv` for dependency management. Install the dependencies using the following command, which synchronizes your environment with the `pyproject.toml` and `uv.lock` files:
    ```bash
    uv sync
    ```

2.  **Run the project as local MCP (STDIO).**
    The project can be run as local MCP using server.py:
    ```bash
    uv run python server.py
    ```

3.  **Run the project as remote MCP (SSE).*
    The project can be run as a remote MCP using sse_server.py:
    ```bash
    uv run python sse_server.py
    ```

    A deployed version is here:
    Type: SSE  
    Name: mcp-greet  
    ServerURL: https://mcp-greet-5ea4aa63d7e9.herokuapp.com/sse
