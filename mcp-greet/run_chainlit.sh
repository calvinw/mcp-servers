#!/bin/bash
set -e
PORT=${PORT:-8080}
echo "🚀 Starting Chainlit app on port $PORT..."

if [ ! -f "app.py" ]; then
    echo "📋 Getting app.py..."
    wget --clobber https://raw.githubusercontent.com/calvinw/chainlit-mcp-client/refs/heads/main/chainlit_mcp_client/app.py
fi

uv sync
uv run chainlit run -w app.py --host 0.0.0.0 --port "$PORT"
