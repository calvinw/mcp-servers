#!/bin/bash
set -e
PORT=${PORT:-8080}
echo "🚀 Starting Chainlit app on port $PORT..."

if [ ! -f "app.py" ]; then
    echo "📋 Getting app.py..."
    wget --clobber https://raw.githubusercontent.com/calvinw/chainlit-mcp-client/refs/heads/main/chainlit_mcp_client/app.py
fi

if [ ! -f "chainlit.md" ]; then
    echo "📋 Getting chainlit.md..."
    wget --clobber https://raw.githubusercontent.com/calvinw/chainlit-mcp-client/refs/heads/main/chainlit_mcp_client/chainlit.md
fi

if [ ! -d ".chainlit" ]; then
    echo "📁 Creating .chainlit directory..."
    mkdir -p .chainlit
fi

if [ ! -f ".chainlit/config.toml" ]; then
    echo "⚙️ Getting config.toml..."
    wget --clobber https://raw.githubusercontent.com/calvinw/chainlit-mcp-client/refs/heads/main/chainlit_mcp_client/.chainlit/config.toml -O .chainlit/config.toml
fi

uv sync
uv run chainlit run -w app.py --host 0.0.0.0 --port "$PORT"
