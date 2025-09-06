from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("bgw-votd-fr")

# Constants
BIBLE_API_BASE = "https://www.biblegateway.com/votd/get/?format=JSON"

# ID: 32, Lang: FR, Version: La Bible du Semeur
@mcp.tool()
def get_bible_votd_lbds():
    """Fetches the Verse of the Day for La Bible du Semeur (ID 32)."""
    url = f"{BIBLE_API_BASE}&version=32"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 2, Lang: FR, Version: Louis Segond
@mcp.tool()
def get_bible_votd_ls():
    """Fetches the Verse of the Day for Louis Segond (ID 2)."""
    url = f"{BIBLE_API_BASE}&version=2"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 168, Lang: FR, Version: Nouvelle Edition de Genève – NEG1979
@mcp.tool()
def get_bible_votd_neg1979():
    """Fetches the Verse of the Day for Nouvelle Edition de Genève – NEG1979 (ID 168)."""
    url = f"{BIBLE_API_BASE}&version=168"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 167, Lang: FR, Version: Segond 21
@mcp.tool()
def get_bible_votd_s21():
    """Fetches the Verse of the Day for Segond 21 (ID 167)."""
    url = f"{BIBLE_API_BASE}&version=167"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')