from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("bgw-votd-it")

# Constants
BIBLE_API_BASE = "https://www.biblegateway.com/votd/get/?format=JSON"

# ID: 244, Lang: IT, Version: La Bibbia della Gioia
@mcp.tool()
def get_bible_votd_lbdg():
    """Fetches the Verse of the Day for La Bibbia della Gioia (ID 244)."""
    url = f"{BIBLE_API_BASE}&version=244"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 3, Lang: IT, Version: Conferenza Episcopale Italiana
@mcp.tool()
def get_bible_votd_cei():
    """Fetches the Verse of the Day for Conferenza Episcopale Italiana (ID 3)."""
    url = f"{BIBLE_API_BASE}&version=3"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 55, Lang: IT, Version: La Nuova Diodati
@mcp.tool()
def get_bible_votd_lnd():
    """Fetches the Verse of the Day for La Nuova Diodati (ID 55)."""
    url = f"{BIBLE_API_BASE}&version=55"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 183, Lang: IT, Version: Nuova Riveduta 1994
@mcp.tool()
def get_bible_votd_nrv1994():
    """Fetches the Verse of the Day for Nuova Riveduta 1994 (ID 183)."""
    url = f"{BIBLE_API_BASE}&version=183"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 170, Lang: IT, Version: Nuova Riveduta 2006
@mcp.tool()
def get_bible_votd_nrv2006():
    """Fetches the Verse of the Day for Nuova Riveduta 2006 (ID 170)."""
    url = f"{BIBLE_API_BASE}&version=170"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')