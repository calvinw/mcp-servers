#!/usr/bin/env python3
"""Integration test for the complete button state system"""

import asyncio
import json
import subprocess
import sys
import time
import websockets
from pathlib import Path

async def test_websocket_integration():
    """Test the complete WebSocket integration"""
    
    # Start the SSE server
    print("🚀 Starting SSE server...")
    sse_process = subprocess.Popen(
        [sys.executable, "sse_server.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Wait for server to start
    await asyncio.sleep(3)
    
    try:
        # Test WebSocket connection
        print("🔌 Testing WebSocket connection...")
        
        # Connect to WebSocket
        session_id = "test1"
        ws_url = f"ws://localhost:8001/ws?session_id={session_id}"
        
        async with websockets.connect(ws_url) as websocket:
            print(f"✅ Connected to WebSocket: {ws_url}")
            
            # Send a ping
            ping_msg = {"type": "ping"}
            await websocket.send(json.dumps(ping_msg))
            
            # Wait for pong
            response = await websocket.recv()
            pong_msg = json.loads(response)
            
            if pong_msg.get("type") == "pong":
                print("✅ WebSocket ping/pong successful")
            else:
                print(f"❌ Unexpected response: {pong_msg}")
            
            # Test MCP server connection
            print("🔧 Testing MCP server integration...")
            
            # Start MCP server
            mcp_process = subprocess.Popen(
                [sys.executable, "server.py"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1
            )
            
            try:
                # Initialize MCP server
                init_request = {
                    "jsonrpc": "2.0",
                    "id": 1,
                    "method": "initialize",
                    "params": {
                        "protocolVersion": "2024-11-05",
                        "capabilities": {},
                        "clientInfo": {"name": "integration-test", "version": "1.0.0"}
                    }
                }
                
                mcp_process.stdin.write(json.dumps(init_request) + "\n")
                mcp_process.stdin.flush()
                
                # Read initialize response
                init_response = mcp_process.stdout.readline()
                print("📥 MCP Initialize response received")
                
                # Send initialized notification
                initialized_notification = {
                    "jsonrpc": "2.0",
                    "method": "notifications/initialized",
                    "params": {}
                }
                
                mcp_process.stdin.write(json.dumps(initialized_notification) + "\n")
                mcp_process.stdin.flush()
                
                # Test connection status
                status_request = {
                    "jsonrpc": "2.0",
                    "id": 2,
                    "method": "tools/call",
                    "params": {
                        "name": "get_connection_status",
                        "arguments": {}
                    }
                }
                
                mcp_process.stdin.write(json.dumps(status_request) + "\n")
                mcp_process.stdin.flush()
                
                # Read status response
                status_response = mcp_process.stdout.readline()
                print("📥 Connection status response received")
                
                # Parse status
                try:
                    status_data = json.loads(status_response)
                    if "result" in status_data and "content" in status_data["result"]:
                        content = status_data["result"]["content"]
                        if content and len(content) > 0:
                            result = json.loads(content[0]["text"])
                            print(f"✅ Connection status: {result}")
                            
                            if result.get("connection_count", 0) > 0:
                                print("✅ WebSocket connection detected by MCP server!")
                            else:
                                print("⚠️  No WebSocket connections detected")
                        else:
                            print("❌ Empty content in status response")
                    else:
                        print("❌ Invalid status response format")
                except (json.JSONDecodeError, KeyError, IndexError) as e:
                    print(f"❌ Failed to parse status response: {e}")
                
                # Test button state request (will timeout since no real UI is clicking)
                print("🔘 Testing button state request...")
                
                # Listen for WebSocket messages
                async def listen_for_messages():
                    try:
                        while True:
                            message = await asyncio.wait_for(websocket.recv(), timeout=2.0)
                            msg_data = json.loads(message)
                            print(f"📨 Received WebSocket message: {msg_data}")
                            
                            if msg_data.get("type") == "get-button-state":
                                # Simulate button state response
                                request_id = msg_data.get("request_id")
                                mock_state = {
                                    "isClicked": True,
                                    "clickCount": 5,
                                    "lastClickTime": int(time.time() * 1000),
                                    "mode": "excited"
                                }
                                
                                response = {
                                    "type": "button-state-response",
                                    "request_id": request_id,
                                    "state": mock_state,
                                    "timestamp": int(time.time() * 1000)
                                }
                                
                                await websocket.send(json.dumps(response))
                                print(f"✅ Sent mock button state response")
                                break
                    except asyncio.TimeoutError:
                        print("⏰ Timeout waiting for WebSocket messages")
                
                # Start listening task
                listen_task = asyncio.create_task(listen_for_messages())
                
                # Test button state tool
                button_request = {
                    "jsonrpc": "2.0",
                    "id": 3,
                    "method": "tools/call",
                    "params": {
                        "name": "get_button_state",
                        "arguments": {"session_id": session_id}
                    }
                }
                
                mcp_process.stdin.write(json.dumps(button_request) + "\n")
                mcp_process.stdin.flush()
                
                # Wait for WebSocket interaction and MCP response
                await listen_task
                
                # Read button state response
                button_response = mcp_process.stdout.readline()
                print("📥 Button state response received")
                
                # Parse button state
                try:
                    button_data = json.loads(button_response)
                    if "result" in button_data and "content" in button_data["result"]:
                        content = button_data["result"]["content"]
                        if content and len(content) > 0:
                            result = json.loads(content[0]["text"])
                            print(f"✅ Button state result: {result}")
                            
                            if result.get("status") == "success":
                                print("🎉 Complete integration test successful!")
                                state = result.get("state", {})
                                print(f"   Button clicked: {state.get('isClicked')}")
                                print(f"   Click count: {state.get('clickCount')}")
                                print(f"   Mode: {state.get('mode')}")
                            else:
                                print(f"⚠️  Button state request failed: {result}")
                        else:
                            print("❌ Empty content in button response")
                    else:
                        print("❌ Invalid button response format")
                except (json.JSONDecodeError, KeyError, IndexError) as e:
                    print(f"❌ Failed to parse button response: {e}")
                
            finally:
                mcp_process.terminate()
                mcp_process.wait()
                
    except Exception as e:
        print(f"❌ Integration test failed: {e}")
    finally:
        # Clean up
        sse_process.terminate()
        sse_process.wait()

if __name__ == "__main__":
    asyncio.run(test_websocket_integration())