# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands

### Development Setup
- Install dependencies: `uv sync`
- Run as local MCP (STDIO): `uv run python server.py`
- Run as remote MCP (SSE): `uv run python sse_server.py`
- Run Chainlit web interface: `./run_chainlit.sh` or `uv run chainlit run -w app.py --host 0.0.0.0 --port 8080`

### Testing
No specific test framework is configured in this project.

## Architecture Overview

This is an MCP (Model Context Protocol) server implementation with multiple interfaces:

### Core Components

**server.py** - Main MCP server using FastMCP framework
- Defines MCP tools: `add_numbers()`, `greet()`, `get_some_sample_markdown()`
- Runs in STDIO mode for local MCP connections
- Entry point: `mcp.run()`

**sse_server.py** - HTTP/SSE wrapper for remote MCP access
- Creates FastAPI app wrapping the MCP server
- Provides SSE (Server-Sent Events) transport at `/sse` endpoint
- Includes CORS middleware and OAuth metadata endpoint
- Deployed version available on Heroku

**app.py** - Chainlit web interface for interacting with MCP tools
- Full web UI for testing MCP tools with OpenRouter LLM integration
- Handles user settings persistence, tool calling, and streaming responses
- Supports multiple OpenRouter models (Google, Anthropic, OpenAI, etc.)
- Tool buttons for quick testing with sample parameters

### Configuration Files

**config.json** - MCP client configuration for connecting to this server
- Defines STDIO connection parameters
- Used by MCP clients to connect to the local server

**pyproject.toml** - Uses uv for dependency management
- Key dependencies: fastmcp, fastapi, uvicorn, chainlit-mcp-client

### Key Patterns

- MCP tools are defined using `@mcp.tool()` decorator in server.py
- The FastMCP framework handles MCP protocol details automatically
- SSE server wraps the core MCP server for HTTP access
- Chainlit app provides rich web interface with LLM integration and persistent user settings