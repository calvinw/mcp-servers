# Button State MCP Server

A simple MCP server demonstrating WebSocket communication between an MCP tool and a web interface with Zustand state management.

## Features

- **MCP Tools**: `get_button_state()` and `get_connection_status()`
- **Web Interface**: Simple button with Zustand state management
- **WebSocket Communication**: Real-time state retrieval from web interface
- **Session Management**: Unique session IDs for multiple clients

## Quick Start

1. **Install dependencies**:
   ```bash
   uv sync
   ```

2. **Run the SSE server** (includes WebSocket support):
   ```bash
   uv run python sse_server.py
   ```

3. **Open the button interface**:
   - Go to `http://localhost:8001/button`
   - Click the button to change state
   - Use additional controls to test different states

4. **Test MCP tools**:
   - Use an MCP client to call `get_button_state()`
   - The tool will retrieve the current Zustand state via WebSocket

## Architecture

### Core Components

- **server.py**: MCP server with `get_button_state()` tool
- **sse_server.py**: FastAPI server with WebSocket support
- **static/index.html**: Web interface with Zustand state management

### State Structure

```json
{
  "isClicked": false,
  "clickCount": 0,
  "lastClickTime": null,
  "mode": "normal"
}
```

### WebSocket Communication

1. MCP tool calls `get_button_state()`
2. Server sends WebSocket message to web interface
3. Web interface responds with current Zustand state
4. Server returns state to MCP client

## Usage Example

```python
# Call the MCP tool
result = await get_button_state()

# Result contains current state:
{
  "status": "success",
  "state": {
    "isClicked": true,
    "clickCount": 5,
    "lastClickTime": 1640995200000,
    "mode": "excited"
  },
  "request_id": "...",
  "timestamp": 1640995200000
}
```

This demonstrates how MCP servers can retrieve real-time state from web interfaces using WebSocket communication.