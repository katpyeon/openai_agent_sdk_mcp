# OpenAI Agent SDK MCP Chatbot

This is an example chatbot application using the OpenAI Agent SDK and an MCP (Model Context Protocol) server.

## Project Overview

This example demonstrates how to build a chatbot application that integrates an MCP (Model Context Protocol) server using the OpenAI Agent SDK and the fastMCP library. The chatbot provides current time information via the MCP server and integrates web search functionality to answer user queries.

## Main Features

- Interactive UI based on Gradio
- Provides current time information via the MCP server
- Natural language processing using the OpenAI Agent SDK
- Integrated web search functionality

## Installation

This project uses Poetry for dependency management.

```bash
# Clone the repository
git clone https://github.com/katpyeon/openai_agent_sdk_mcp.git
cd openai_agent_sdk_mcp

# Install dependencies with Poetry
poetry install
```

## Environment Variable Setup

Create a `.env` file in the project root and set the following variables:

```
PYTHON_PATH=/path/to/your/python
OPENAI_API_KEY=your_openai_api_key
```

## How to Run

```bash
# Run the app in the Poetry environment
poetry run python src/app.py
```

## Project Structure

```
openai-agent-sdk-mcp/
├── src/
│   ├── app.py              # Main application (Gradio UI)
│   ├── time_mcp_server.py  # MCP server providing time information
│   └── __init__.py
├── tests/                  # Test code
├── .env                    # Environment variables (not included in git)
├── poetry.lock             # Poetry dependency lock file
├── pyproject.toml          # Project metadata and dependencies
└── README.md               # Project documentation
```

## License

MIT


---

<a href="https://www.buymeacoffee.com/katpyeon" target="_blank">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="40" />
</a>