# HTTP Streamable - Stateful: HTTP Messages

## Overview

This document details the HTTP messages for the HTTP Streamable Stateful transport configuration.

## Messages

### 3.1 Initialize Request (POST)

**Client Request:**

```http
POST /mcp HTTP/1.1
Host: localhost:8000
Content-Type: application/json

{
  "jsonrpc": "2.0",
  "id": 0,
  "method": "initialize",
  "params": {
    "protocolVersion": "2025-11-25",
    "capabilities": {
      "experimental": {
        "tasks": {}
      }
    },
    "clientInfo": {
      "name": "mcp",
      "version": "0.1.0"
    }
  }
}
```

**Server Response:**

```http
HTTP/1.1 200 OK
date: Fri, 12 Dec 2025 13:42:01 GMT
server: uvicorn
cache-control: no-cache, no-transform
connection: keep-alive
content-type: text/event-stream
mcp-session-id: c1a48a90797c48f8b4ae35c399b9df3f
x-accel-buffering: no
transfer-encoding: chunked
```

**SSE Message:**

```json
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": {
    "protocolVersion": "2025-11-25",
    "capabilities": {
      "experimental": {},
      "prompts": {"listChanged": true},
      "resources": {"subscribe": false, "listChanged": true},
      "tools": {"listChanged": true}
    },
    "serverInfo": {
      "name": "My MCP Server",
      "version": "2.14.0"
    }
  }
}
```

### 3.2 Initialized Notification (POST)

**Client Request:**

```http
POST /mcp HTTP/1.1
Host: localhost:8000
Content-Type: application/json
mcp-session-id: c1a48a90797c48f8b4ae35c399b9df3f

{
  "jsonrpc": "2.0",
  "method": "notifications/initialized",
  "params": null
}
```

**Server Response:**

```http
HTTP/1.1 202 Accepted
date: Fri, 12 Dec 2025 13:42:01 GMT
server: uvicorn
content-type: application/json
mcp-session-id: c1a48a90797c48f8b4ae35c399b9df3f
content-length: 0
```

### 3.3 GET SSE Stream Connection

**Client Request:**

```http
GET /mcp HTTP/1.1
Host: localhost:8000
mcp-session-id: c1a48a90797c48f8b4ae35c399b9df3f
```

**Server Response:**

```http
HTTP/1.1 200 OK
date: Fri, 12 Dec 2025 13:42:01 GMT
server: uvicorn
cache-control: no-cache, no-transform
connection: keep-alive
content-type: text/event-stream
mcp-session-id: c1a48a90797c48f8b4ae35c399b9df3f
x-accel-buffering: no
transfer-encoding: chunked
```

### 3.4 List Tools Request (POST)

**Client Request:**

```http
POST /mcp HTTP/1.1
Host: localhost:8000
Content-Type: application/json
mcp-session-id: c1a48a90797c48f8b4ae35c399b9df3f

{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": null
}
```

**Server Response:**

```http
HTTP/1.1 200 OK
date: Fri, 12 Dec 2025 13:42:01 GMT
server: uvicorn
cache-control: no-cache, no-transform
connection: keep-alive
content-type: text/event-stream
mcp-session-id: c1a48a90797c48f8b4ae35c399b9df3f
x-accel-buffering: no
transfer-encoding: chunked
```

**SSE Message:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "greet",
        "description": "Greets a person by name with a friendly hello message.\n\nArgs:\n    name: The name of the person to greet\n\nReturns:\n    A personalized greeting message",
        "inputSchema": {
          "properties": {"name": {"type": "string"}},
          "required": ["name"],
          "type": "object"
        },
        "outputSchema": {
          "properties": {"result": {"type": "string"}},
          "required": ["result"],
          "type": "object",
          "x-fastmcp-wrap-result": true
        },
        "_meta": {"_fastmcp": {"tags": []}}
      }
    ]
  }
}
```

### 3.5 Call Tool Request (POST)

**Client Request:**

```http
POST /mcp HTTP/1.1
Host: localhost:8000
Content-Type: application/json
mcp-session-id: c1a48a90797c48f8b4ae35c399b9df3f

{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "greet",
    "arguments": {"name": "Teddy 🐶"},
    "_meta": {"progressToken": 2}
  }
}
```

**Server Response:**

```http
HTTP/1.1 200 OK
date: Fri, 12 Dec 2025 13:42:01 GMT
server: uvicorn
cache-control: no-cache, no-transform
connection: keep-alive
content-type: text/event-stream
mcp-session-id: c1a48a90797c48f8b4ae35c399b9df3f
x-accel-buffering: no
transfer-encoding: chunked
```

**SSE Message:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Hello, Teddy 🐶 from MCP server!"
      }
    ],
    "structuredContent": {
      "result": "Hello, Teddy 🐶 from MCP server!"
    },
    "isError": false
  }
}
```

### 3.6 Session Termination (DELETE)

**Client Request:**

```http
DELETE /mcp HTTP/1.1
Host: localhost:8000
mcp-session-id: c1a48a90797c48f8b4ae35c399b9df3f
```

**Server Response:**

```http
HTTP/1.1 200 OK
date: Fri, 12 Dec 2025 13:42:01 GMT
server: uvicorn
content-type: application/json
mcp-session-id: c1a48a90797c48f8b4ae35c399b9df3f
content-length: 0
```

### Server Logs

```
INFO:     127.0.0.1:46386 - "POST /mcp HTTP/1.1" 200 OK
INFO:     127.0.0.1:46390 - "POST /mcp HTTP/1.1" 202 Accepted
INFO:     127.0.0.1:46396 - "GET /mcp HTTP/1.1" 200 OK
INFO:     127.0.0.1:46406 - "POST /mcp HTTP/1.1" 200 OK
INFO:     127.0.0.1:46412 - "POST /mcp HTTP/1.1" 200 OK
INFO:     127.0.0.1:46420 - "DELETE /mcp HTTP/1.1" 200 OK
```
