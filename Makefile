# Makefile for Python MCP Server

.PHONY: help install run-server-stateful-http-streamable run-server-stateless-http-streamable run-server-sse run-client-http-streamable run-client-sse format lint clean

help:
	@echo "Available commands:"
	@echo "  install                              Install dependencies"
	@echo "  install-dev                          Install dependencies including dev tools"
	@echo "  run-server-stateful-http-streamable  Run the MCP server (stateful, streamable-http)"
	@echo "  run-server-stateless-http-streamable Run the MCP server (stateless, streamable-http)"
	@echo "  run-server-sse                       Run the MCP server (stateless, SSE)"
	@echo "  run-client-http-streamable           Run the MCP client (HTTP streamable)"
	@echo "  run-client-sse                       Run the MCP client (SSE)"
	@echo "  format                               Format code with ruff"
	@echo "  lint                                 Lint code with ruff"
	@echo "  clean                                Clean up temporary files"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

run-server-stateful-http-streamable:
	python server.py --stateful

run-server-stateless-http-streamable:
	python server.py

run-server-sse:
	python server.py --transport=sse

run-client-http-streamable:
	python client.py --transport=streamable-http

run-client-sse:
	python client.py --transport=sse

format:
	ruff format .

lint:
	ruff check .

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type f -name ".coverage" -delete
