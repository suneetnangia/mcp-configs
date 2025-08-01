import sys
from typing import Literal

from colorama import Fore, Style, init
from fastmcp import FastMCP

# Initialize colorama for cross-platform color support
init(autoreset=True)

# Check for --stateful flag
stateless = "--stateful" not in sys.argv

# Check for transport option (default to streamable-http)
transport: Literal["sse", "streamable-http"] = "streamable-http"
for arg in sys.argv:
    if arg.startswith("--transport="):
        value = arg.split("=", 1)[1]
        if value in ["sse", "streamable-http"]:
            transport = value  # type: ignore
        break

mcp = FastMCP(
    "My MCP Server",
    stateless_http=stateless
)


@mcp.tool
def greet(name: str) -> str:
    """Greets a person by name with a friendly hello message.

    Args:
        name: The name of the person to greet

    Returns:
        A personalized greeting message
    """
    return f"Hello, {name} from MCP server!"


if __name__ == "__main__":
    mode = "stateful" if not stateless else "stateless"
    print(f"Starting MCP server in {Fore.CYAN}{mode}{Style.RESET_ALL} mode with {Fore.YELLOW}{transport}{Style.RESET_ALL} transport...", flush=True)
    mcp.run(transport=transport)
