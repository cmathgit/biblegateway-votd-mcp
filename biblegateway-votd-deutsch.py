from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("bgw-votd-de")

# Constants
BIBLE_API_BASE = "https://www.biblegateway.com/votd/get/?format=JSON"

# ID: 33, Lang: DE, Version: Hoffnung für Alle
@mcp.tool()
def get_bible_votd_hoffnung():
    """Fetches the Verse of the Day for Hoffnung für Alle (ID 33)."""
    url = f"{BIBLE_API_BASE}&version=33"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 10, Lang: DE, Version: Luther Bibel 1545
@mcp.tool()
def get_bible_votd_luther1545():
    """Fetches the Verse of the Day for Luther Bibel 1545 (ID 10)."""
    url = f"{BIBLE_API_BASE}&version=10"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 186, Lang: DE, Version: Neue Genfer Übersetzung
@mcp.tool()
def get_bible_votd_negenuber():
    """Fetches the Verse of the Day for Neue Genfer Übersetzung (ID 186)."""
    url = f"{BIBLE_API_BASE}&version=186"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 187, Lang: DE, Version: Schlachter 1951
@mcp.tool()
def get_bible_votd_schl1951():
    """Fetches the Verse of the Day for Schlachter 1951 (ID 187)."""
    url = f"{BIBLE_API_BASE}&version=187"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 188, Lang: DE, Version: Schlachter 2000
@mcp.tool()
def get_bible_votd_schl2000():
    """Fetches the Verse of the Day for Schlachter 2000 (ID 188)."""
    url = f"{BIBLE_API_BASE}&version=188"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')