#!/usr/bin/env python3
"""Test script to verify MCP server functionality"""

import json
import subprocess
import sys
import time

def test_mcp_server():
    """Test the MCP server by sending JSON-RPC messages"""
    
    # Start the server process
    cmd = [sys.executable, "server.py"]
    process = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )
    
    try:
        # 1. Initialize the server
        init_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {
                    "name": "test-client",
                    "version": "1.0.0"
                }
            }
        }
        
        print("📤 Sending initialize request...")
        process.stdin.write(json.dumps(init_request) + "\n")
        process.stdin.flush()
        
        # Read response
        response = process.stdout.readline()
        print("📥 Initialize response:", response.strip())
        
        # Send initialized notification
        initialized_notification = {
            "jsonrpc": "2.0",
            "method": "notifications/initialized",
            "params": {}
        }
        
        print("📤 Sending initialized notification...")
        process.stdin.write(json.dumps(initialized_notification) + "\n")
        process.stdin.flush()
        
        # 2. List available tools
        tools_request = {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list",
            "params": {}
        }
        
        print("\n📤 Sending tools/list request...")
        process.stdin.write(json.dumps(tools_request) + "\n")
        process.stdin.flush()
        
        # Read response
        response = process.stdout.readline()
        print("📥 Tools list response:", response.strip())
        
        # Parse and display tools
        try:
            tools_response = json.loads(response)
            if "result" in tools_response and "tools" in tools_response["result"]:
                tools = tools_response["result"]["tools"]
                print(f"\n✅ Found {len(tools)} tools:")
                for tool in tools:
                    print(f"  - {tool['name']}: {tool.get('description', 'No description')}")
            else:
                print("❌ No tools found in response")
        except json.JSONDecodeError:
            print("❌ Failed to parse tools response")
        
        # 3. Test get_connection_status tool
        status_request = {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "get_connection_status",
                "arguments": {}
            }
        }
        
        print("\n📤 Sending get_connection_status request...")
        process.stdin.write(json.dumps(status_request) + "\n")
        process.stdin.flush()
        
        # Read response
        response = process.stdout.readline()
        print("📥 Connection status response:", response.strip())
        
        # Parse and display result
        try:
            status_response = json.loads(response)
            if "result" in status_response and "content" in status_response["result"]:
                content = status_response["result"]["content"]
                if content and len(content) > 0:
                    result = json.loads(content[0]["text"])
                    print(f"✅ Connection status: {result}")
                else:
                    print("❌ No content in status response")
            else:
                print("❌ Invalid status response format")
        except (json.JSONDecodeError, KeyError, IndexError):
            print("❌ Failed to parse status response")
        
        print("\n🎉 MCP server test completed!")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
    finally:
        # Clean up
        process.terminate()
        process.wait()

if __name__ == "__main__":
    test_mcp_server()