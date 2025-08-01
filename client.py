"""
MCP Client Implementation

This client connects to the MCP Server using FastMCP's Client class.

Features:
- Connect to MCP server via HTTP
- List available tools
- Call tools with parameters
- Handle responses

Usage:
    python client.py [--transport=TRANSPORT]

Options:
    --transport=TRANSPORT    Transport type: 'sse' or 'streamable-http' (default: streamable-http)
                            Uses /sse endpoint for SSE, /mcp for streamable-http

Requires:
    Server running with appropriate transport on localhost:8000

Based on FastMCP: https://github.com/modelcontextprotocol/python-sdk
"""

import argparse
import asyncio
import json
import logging

from fastmcp import Client

# Configure logging to see HTTP messages
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


async def main(transport: str = "streamable-http"):
    """
    Main function demonstrating the FastMCP client usage.
    Connects to server, lists tools, and calls a tool once.

    Args:
        transport: Transport type ('sse' or 'streamable-http')
    """
    # Determine endpoint suffix based on transport type
    endpoint_suffix = "/sse" if transport == "sse" else "/mcp"
    server_url = f"http://localhost:8000{endpoint_suffix}"

    # Create client with server URL
    client = Client(server_url)

    async with client:
        print(f"✓ Connected to MCP Server at {server_url}")

        # List available tools
        print("\n📋 Available Tools:")
        tools = await client.list_tools()
        for tool in tools:
            print(f"\n  Tool: {tool.name}")
            print(f"  Description: {tool.description}")
            if tool.inputSchema:
                params = json.dumps(tool.inputSchema, indent=4)
                print(f"  Parameters: {params}")

        # Call the greet tool once
        print("\n🔧 Calling 'greet' tool with name='Teddy 🐶'...")
        result = await client.call_tool("greet", {"name": "Teddy 🐶"})
        if result.content:
            content = result.content[0]
            response_text = getattr(content, "text", str(content))
            print(f"  Response: {response_text}")

        print("\n✓ Done!")


if __name__ == "__main__":
    """
    Run the FastMCP client example.

    Ensure the server is running:
        python server.py [--transport=sse|streamable-http]
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="MCP Client")
    parser.add_argument(
        "--transport",
        type=str,
        default="streamable-http",
        choices=["sse", "streamable-http"],
        help="Transport type: 'sse' or 'streamable-http' (default: streamable-http)",
    )
    args = parser.parse_args()

    print("=" * 60)
    print(f"FastMCP Client Example ({args.transport})")
    print("=" * 60)

    asyncio.run(main(args.transport))
