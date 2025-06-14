# Test all tools with MCP Inspector
echo "Listing all available tools..."
npx @modelcontextprotocol/inspector --cli --config ./config.json --server mcp-greet --method tools/list 

# 1. Test greet tool
echo "Testing greet tool with name=Alice..."
npx @modelcontextprotocol/inspector --cli --config ./config.json --server mcp-greet --method tools/call --tool-name greet --tool-arg name="Alice" 

# 3. Test get_sample_markdown_table tool (no arguments)
echo "Testing get_sample_markdown_table tool (no arguments)..."
npx @modelcontextprotocol/inspector --cli --config ./config.json --server mcp-greet --method tools/call --tool-name get_sample_markdown_table 

# 4. Test add_numbers tool with default values
echo "Testing add_numbers tool with default values..."
npx @modelcontextprotocol/inspector --cli --config ./config.json --server mcp-greet --method tools/call --tool-name add_numbers 

# 5. Test add_numbers tool with custom values
echo "Testing add_numbers tool with custom values (a=25.5, b=17.3)..."
npx @modelcontextprotocol/inspector --cli --config ./config.json --server mcp-greet --method tools/call --tool-name add_numbers --tool-arg a=25.5 --tool-arg b=17.3 
