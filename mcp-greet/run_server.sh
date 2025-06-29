#!/bin/bash
set -e

echo "🚀 Starting SSE server..."

# Sync dependencies
uv sync

# Start SSE server
echo "🔧 Starting SSE server on port 8000..."
uv run python server.py
