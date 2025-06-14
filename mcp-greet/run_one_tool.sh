# Test all tools with MCP Inspector

# 1. Test greet tool
echo "Testing greet tool with name=calvin..."
npx @modelcontextprotocol/inspector --cli --config ./config.json --server mcp-greet --method tools/call --tool-name greet --tool-arg name=calvin 
