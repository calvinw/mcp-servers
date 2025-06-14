#!/bin/bash
set -e
PORT=${PORT:-8080}
echo "🚀 Starting Chainlit app on port $PORT..."

# Copy the packaged config if it doesn't exist locally
if [ ! -d ".chainlit" ]; then
    echo "📋 Copying packaged .chainlit config..."
    cp -r .venv/lib/python3.13/site-packages/chainlit_mcp_client/.chainlit .
fi

uv run chainlit run .venv/lib/python3.13/site-packages/chainlit_mcp_client/app.py --host 0.0.0.0 --port "$PORT"
