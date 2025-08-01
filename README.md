# MCP Server Confguration Options

## Features

- **MCP Server**: Implements the Model Context Protocol with a greeting tool
- **FastMCP Framework**: Built using the FastMCP library for simplified development

## Project Structure

```
mcp-configs/
├── .vscode/
│   └── tasks.json              # VS Code tasks configuration
├── server.py                   # Main MCP server implementation
├── client.py                   # MCP client implementation
├── pyproject.toml              # Python project configuration & dependencies
├── Makefile                    # Common development tasks
└── README.md                   # This file
```

## Getting Started

1. Open this project in VS Code
2. Install the "Dev Containers" extension if not already installed
3. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) and select "Dev Containers: Reopen in Container"
4. Wait for the container to build and dependencies to install automatically

## Running the Server

Start the server:

```bash
make run-server
# or
python server.py
```

The server will start on `http://localhost:8000`

## Running the Client

Test the server with the client:

### For HTTP Streamable transport:
```bash
make run-client-http-streamable
# or
python client.py --transport=streamable-http
```

### For SSE transport:
```bash
make run-client-sse
# or
python client.py --transport=sse
```

The client connects to the server at the appropriate endpoint (`/mcp` for streamable-http, `/sse` for SSE), lists available tools, and calls the greet tool.

## Available Tools

**greet** - Greets a person by name

Parameters: `name` (string, required)

Example: `greet("Alice")` returns `"Hello, Alice from MCP server!"`

## Development

### Commands

- `make run-server-stateful-http-streamable` - Run the MCP server (stateful, HTTP streamable)
- `make run-server-stateless-http-streamable` - Run the MCP server (stateless, HTTP streamable)
- `make run-server-sse` - Run the MCP server (SSE transport)
- `make run-client-http-streamable` - Run the MCP client (HTTP streamable)
- `make run-client-sse` - Run the MCP client (SSE)
- `make format` - Format code with Ruff
- `make lint` - Lint code with Ruff
- `make clean` - Remove temporary files

### Adding Tools

Add new tools by decorating functions with `@mcp.tool`:

```python
@mcp.tool
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers."""
    return a + b
```

## Using with AI Tools

You can connect AI assistants like Claude or other MCP-compatible clients to this server:

1. The server supports two transport types:
   - **SSE**: `http://localhost:8000/sse` (Server-Sent Events)
   - **HTTP Streamable**: `http://localhost:8000/mcp` (Stateful or Stateless)
2. Configure your MCP client to point to the appropriate endpoint
3. Use `--transport=sse` or `--transport=streamable-http` when starting the server
4. The client can discover and call available tools dynamically
