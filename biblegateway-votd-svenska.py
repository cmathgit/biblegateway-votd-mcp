from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("bgw-votd-sv")

# Constants
BIBLE_API_BASE = "https://www.biblegateway.com/votd/get/?format=JSON"

## ID: 44, Lang: SV, Version: nuBibeln (Swedish Contemporary Bible)
@mcp.tool()
def get_bible_votd_n_swedish_cb():
    """Fetches the Verse of the Day for nuBibeln (Swedish Contemporary Bible) (ID 44)."""
    url = f"{BIBLE_API_BASE}&version=44"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 185, Lang: SV, Version: Svenska Folkbibeln
@mcp.tool()
def get_bible_votd_svenska_f():
    """Fetches the Verse of the Day for Svenska Folkbibeln (ID 185)."""
    url = f"{BIBLE_API_BASE}&version=185"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 148, Lang: SV, Version: Svenska Folkbibeln 2015
@mcp.tool()
def get_bible_votd_svenska_f2015():
    """Fetches the Verse of the Day for Svenska Folkbibeln 2015 (ID 148)."""
    url = f"{BIBLE_API_BASE}&version=148"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 7, Lang: SV, Version: Svenska 1917
@mcp.tool()
def get_bible_votd_svenska_1917():
    """Fetches the Verse of the Day for Svenska 1917 (ID 7)."""
    url = f"{BIBLE_API_BASE}&version=7"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 272, Lang: SV, Version: Swedish New Living Bible (Nya Levande Bibeln)
@mcp.tool()
def get_bible_votd_swedish_nlb():
    """Fetches the Verse of the Day for Swedish New Living Bible (Nya Levande Bibeln) (ID 272)."""
    url = f"{BIBLE_API_BASE}&version=272"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')