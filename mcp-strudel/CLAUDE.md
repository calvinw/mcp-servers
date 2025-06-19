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

This is a Strudel live coding MCP (Model Context Protocol) server that enables Claude to send live coding patterns to a web-based Strudel REPL for real-time music generation.

### Core Components

**server.py** - Main MCP server using FastMCP framework
- Defines Strudel-specific MCP tools:
  - `play_strudel_pattern(code, description)` - Send Strudel code to connected browsers
  - `stop_strudel_playback()` - Stop all playback
  - `get_strudel_status()` - Check connection status  
  - `send_strudel_example(example_type)` - Send preset patterns
- Includes code validation to prevent dangerous patterns
- Runs in STDIO mode for local MCP connections
- Entry point: `mcp.run()`

**sse_server.py** - HTTP/SSE wrapper with WebSocket support
- Creates FastAPI app wrapping the MCP server
- Provides SSE transport at `/sse` endpoint for MCP clients
- WebSocket endpoint at `/ws` for real-time communication with Strudel web interface
- Serves static Strudel player at `/strudel` route
- Includes CORS middleware and OAuth metadata endpoint
- ConnectionManager class handles WebSocket broadcasting to multiple browsers

**app.py** - Chainlit web interface for MCP tool testing
- Full web UI for testing MCP tools with OpenRouter LLM integration
- Supports multiple OpenRouter models (Google, Anthropic, OpenAI, etc.)
- Persistent user settings and tool buttons for quick testing
- Custom action callbacks for executing tools with sample parameters

### Static Web Interface

**static/index.html** - Strudel live coding web interface
- Embeds Strudel web components (`<strudel-repl>`)
- WebSocket client for receiving patterns from MCP server
- Real-time pattern evaluation and playback
- Connection status indicators and message logging

**static/app.js** - WebSocket client implementation
- Connects to `/ws` endpoint for real-time communication
- Handles incoming pattern execution and stop commands
- Automatic reconnection and audio context initialization
- Error reporting back to server for debugging

### Configuration Files

**config.json** - MCP client configuration
- STDIO connection parameters for local MCP client connections
- Points to this directory's server.py as the command entry point

**pyproject.toml** - Python dependencies
- Key dependencies: fastmcp, fastapi, uvicorn, chainlit-mcp-client
- Uses uv for dependency management

### Integration Patterns

- MCP tools communicate with web interface through WebSocket broadcasting
- WebSocket manager is shared between server.py and sse_server.py via `set_websocket_manager()`
- Strudel patterns are validated before execution to prevent code injection
- Multiple browser connections supported for collaborative live coding
- Real-time error reporting from browser back to MCP server for debugging