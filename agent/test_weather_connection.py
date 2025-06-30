#!/usr/bin/env python3
"""
Test script to verify weather server MCP connection
"""

from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os

async def test_weather_connection():
    """Test if we can connect to the weather server via MCP"""
    
    # Same configuration as in agent.py
    config = {
        "weather": {
            "command": "python",
            "args": [os.path.join(os.path.dirname(__file__), "weather_server.py")],
            "transport": "stdio"
        }
    }
    
    print("🧪 Testing Weather Server MCP Connection...")
    print("=" * 50)
    
    try:
        async with MultiServerMCPClient(config) as client:
            # Get available tools
            tools = client.get_tools()
            print(f"✅ Connection successful!")
            print(f"📋 Available tools: {len(tools)}")
            
            # List all weather tools
            weather_tools = []
            for tool in tools:
                print(f"  • {tool.name}: {tool.description}")
                if "weather" in tool.name.lower():
                    weather_tools.append(tool)
            
            if weather_tools:
                print(f"\n🌤️  Found {len(weather_tools)} weather tools!")
                
                # Test calling a weather tool
                print("\n🧪 Testing get_current_weather tool...")
                try:
                    # Find the get_current_weather tool
                    weather_tool = None
                    for tool in tools:
                        if tool.name == "get_current_weather":
                            weather_tool = tool
                            break
                    
                    if weather_tool:
                        # Call the tool with Tokyo as test city
                        result = await client.call_tool(
                            weather_tool.name,
                            {"city": "Tokyo"}
                        )
                        print(f"📍 Weather result for Tokyo:")
                        print(result.content[0].text if result.content else "No content")
                    else:
                        print("❌ get_current_weather tool not found")
                        
                except Exception as tool_error:
                    print(f"❌ Error calling weather tool: {tool_error}")
            else:
                print("⚠️  No weather tools found!")
                
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        print("\n🔍 Troubleshooting:")
        print("  1. Check if weather_server.py exists")
        print("  2. Check if weather server process is running")
        print("  3. Check if fastmcp is properly installed")

if __name__ == "__main__":
    asyncio.run(test_weather_connection()) 