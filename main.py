from fastmcp import FastMCP

# Create a server instance with a descriptive name
mcp = FastMCP(name="My First MCP Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Adds two integer numbers together."""
    return a + b

@mcp.resource("resource://config")
def get_config() -> dict:
    """Provides the application's configuration."""
    return {"version": "1.0", "author": "MyTeam"}

@mcp.resource("greetings://{name}")
def personalized_greeting(name: str) -> str:
    """Generates a personalized greeting for the given name."""
    return f"Hello, {name}! Welcome to the MCP server."

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8000)