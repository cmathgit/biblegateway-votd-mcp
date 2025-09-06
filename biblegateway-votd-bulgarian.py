from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("bgw-votd-bg")

# Constants
BIBLE_API_BASE = "https://www.biblegateway.com/votd/get/?format=JSON"

# ID: 82, Lang: BG, Version: 1940 Bulgarian Bible
@mcp.tool()
def get_bible_votd_v1940bb():
    """Fetches the Verse of the Day for 1940 Bulgarian Bible (ID 82)."""
    url = f"{BIBLE_API_BASE}&version=82"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 249, Lang: BG, Version: Библия, синодално издание
@mcp.tool()
def get_bible_votd_bib():
    """Fetches the Verse of the Day for Библия, синодално издание (ID 249)."""
    url = f"{BIBLE_API_BASE}&version=249"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 216, Lang: BG, Version: Библия, ревизирано издание
@mcp.tool()
def get_bible_votd_bib_rev():
    """Fetches the Verse of the Day for Библия, ревизирано издание (ID 216)."""
    url = f"{BIBLE_API_BASE}&version=216"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 21, Lang: BG, Version: Bulgarian Bible
@mcp.tool()
def get_bible_votd_bulg():
    """Fetches the Verse of the Day for Bulgarian Bible (ID 21)."""
    url = f"{BIBLE_API_BASE}&version=21"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 95, Lang: BG, Version: Библия, нов превод от оригиналните езици (с неканоничните книги)
@mcp.tool()
def get_bible_votd_bib_nov_prevod():
    """Fetches the Verse of the Day for Библия, нов превод от оригиналните езици (с неканоничните книги) (ID 95)."""
    url = f"{BIBLE_API_BASE}&version=95"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 172, Lang: BG, Version: Bulgarian New Testament: Easy-to-Read Version
@mcp.tool()
def get_bible_votd_bulg_nt_etr():
    """Fetches the Verse of the Day for Bulgarian New Testament: Easy-to-Read Version (ID 172)."""
    url = f"{BIBLE_API_BASE}&version=172"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')