# SSE Transport: HTTP Messages

## Overview

This document details the HTTP messages for the SSE (Server-Sent Events) transport configuration.

## Messages

### 3.1 Initial SSE Connection (GET)

**Client Request:**

```http
GET /sse HTTP/1.1
Host: localhost:8000
```

**Server Response:**

```http
HTTP/1.1 200 OK
date: Fri, 12 Dec 2025 13:39:57 GMT
server: uvicorn
cache-control: no-store
connection: keep-alive
x-accel-buffering: no
content-type: text/event-stream; charset=utf-8
transfer-encoding: chunked
```

**SSE Event - Endpoint:**

```
event: endpoint
data: http://localhost:8000/messages/?session_id=1beded10f1764848be4e028989c149e8
```

### 3.2 Initialize Request (POST)

**Client Request:**

```http
POST /messages/?session_id=1beded10f1764848be4e028989c149e8 HTTP/1.1
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
HTTP/1.1 202 Accepted
date: Fri, 12 Dec 2025 13:39:57 GMT
server: uvicorn
content-length: 8
```

**SSE Event - Message:**

```json
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": {
    "protocolVersion": "2025-11-25",
    "capabilities": {
      "experimental": {
        "tasks": {
          "list": {},
          "cancel": {},
          "requests": {
            "tools": {"call": {}},
            "prompts": {"get": {}},
            "resources": {"read": {}}
          }
        }
      },
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

### 3.3 Initialized Notification (POST)

**Client Request:**

```http
POST /messages/?session_id=1beded10f1764848be4e028989c149e8 HTTP/1.1
Host: localhost:8000
Content-Type: application/json

{
  "jsonrpc": "2.0",
  "method": "notifications/initialized",
  "params": null
}
```

**Server Response:**

```http
HTTP/1.1 202 Accepted
date: Fri, 12 Dec 2025 13:39:57 GMT
server: uvicorn
content-length: 8
```

### 3.4 List Tools Request (POST)

**Client Request:**

```http
POST /messages/?session_id=1beded10f1764848be4e028989c149e8 HTTP/1.1
Host: localhost:8000
Content-Type: application/json

{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": null
}
```

**Server Response:**

```http
HTTP/1.1 202 Accepted
date: Fri, 12 Dec 2025 13:39:57 GMT
server: uvicorn
content-length: 8
```

**SSE Event - Message:**

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
POST /messages/?session_id=1beded10f1764848be4e028989c149e8 HTTP/1.1
Host: localhost:8000
Content-Type: application/json

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
HTTP/1.1 202 Accepted
date: Fri, 12 Dec 2025 13:39:57 GMT
server: uvicorn
content-length: 8
```

**SSE Event - Message:**

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

### Server Logs

```
INFO:     127.0.0.1:58902 - "GET /sse HTTP/1.1" 200 OK
INFO:     127.0.0.1:58908 - "POST /messages/?session_id=1beded10f1764848be4e028989c149e8 HTTP/1.1" 202 Accepted
INFO:     127.0.0.1:58908 - "POST /messages/?session_id=1beded10f1764848be4e028989c149e8 HTTP/1.1" 202 Accepted
INFO:     127.0.0.1:58908 - "POST /messages/?session_id=1beded10f1764848be4e028989c149e8 HTTP/1.1" 202 Accepted
INFO:     127.0.0.1:58908 - "POST /messages/?session_id=1beded10f1764848be4e028989c149e8 HTTP/1.1" 202 Accepted
```
