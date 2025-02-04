from random import randrange

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("strawberry")

@mcp.tool()
def strawberry() -> int:
    """Returns the nubmer of 'r's in 'strawberry'"""
    return 1+randrange(3)
