# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands

### Development Setup
- Install dependencies: `uv sync` (run in individual project directories)
- Run local MCP server: `uv run python server.py`
- Run remote MCP server: `uv run python sse_server.py`
- Run Chainlit web interface: `./run_chainlit.sh` or `uv run chainlit run -w app.py --host 0.0.0.0 --port 8080`

### Deployment
- Deploy to Heroku: `./deploy_heroku.sh` (in project directories)

## Repository Architecture

This is a collection of MCP (Model Context Protocol) server examples. Each subdirectory contains a complete MCP server implementation.

### Project Structure

**Root Level** - Contains multiple MCP server examples
- Each subdirectory is a standalone MCP server project
- Projects use `uv` for Python dependency management

**mcp-greet/** - Example MCP server with multiple interfaces
- **server.py** - Core MCP server using FastMCP framework
- **sse_server.py** - HTTP/SSE wrapper for remote access
- **app.py** - Chainlit web interface for testing MCP tools
- **config.json** - MCP client configuration for local connections

### MCP Server Patterns

**Core Server (server.py)**
- Uses FastMCP framework for MCP protocol handling
- Tools defined with `@mcp.tool()` decorator
- Runs in STDIO mode: `mcp.run()`
- Entry point for local MCP client connections

**SSE Server (sse_server.py)**
- FastAPI wrapper around core MCP server
- Provides `/sse` endpoint for HTTP/SSE transport
- Enables remote MCP client connections
- Includes CORS middleware and OAuth metadata

**Web Interface (app.py)**
- Chainlit-based web UI for interactive testing
- Integrates with OpenRouter for LLM functionality
- Provides tool buttons for quick testing
- Handles user settings persistence

### Key Dependencies

- **fastmcp** - MCP server framework
- **fastapi** - HTTP server for SSE transport
- **chainlit-mcp-client** - Web interface for MCP tools
- **uvicorn** - ASGI server

### Development Workflow

1. Each MCP server project is self-contained
2. Use `uv sync` to install dependencies in project directories
3. Test locally with `server.py` for STDIO mode
4. Test remotely with `sse_server.py` for HTTP/SSE mode
5. Use `app.py` for interactive web-based testing