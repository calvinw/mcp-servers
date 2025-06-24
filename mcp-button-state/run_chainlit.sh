#!/bin/bash
set -e
PORT=${PORT:-8081}
echo "🚀 Starting Chainlit app on port $PORT..."

# Use current working directory

uv sync

# Copy the packaged config if it doesn't exist locally
if [ ! -d ".chainlit" ]; then
    echo "📋 Copying packaged .chainlit config..."
    cp -r .venv/lib/python3.13/site-packages/chainlit_mcp_client/.chainlit .
fi

if [ ! -d "app.py" ]; then
    echo "📋 Copying packaged app.py..."
    cp -r .venv/lib/python3.13/site-packages/chainlit_mcp_client/app.py .
fi

uv run chainlit run -w app.py --host 0.0.0.0 --port "$PORT"
