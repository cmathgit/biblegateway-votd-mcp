from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("bgw-votd-ru")

# Constants
BIBLE_API_BASE = "https://www.biblegateway.com/votd/get/?format=JSON"

# ID: 119, Lang: RU, Version: Священное Писание (Восточный Перевод)
@mcp.tool()
def get_bible_votd_spv():
    """Fetches the Verse of the Day for Священное Писание (Восточный Перевод) (ID 119)."""
    url = f"{BIBLE_API_BASE}&version=119"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 121, Lang: RU, Version: Священное Писание (Восточный перевод), версия с «Аллахом»
@mcp.tool()
def get_bible_votd_spv_v2():
    """Fetches the Verse of the Day for Священное Писание (Восточный перевод), версия с «Аллахом» (ID 121)."""
    url = f"{BIBLE_API_BASE}&version=121"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 120, Lang: RU, Version: Священное Писание (Восточный перевод), версия для Таджикистана
@mcp.tool()
def get_bible_votd_spv_v3():
    """Fetches the Verse of the Day for Священное Писание (Восточный перевод), версия для Таджикистана (ID 120)."""
    url = f"{BIBLE_API_BASE}&version=120"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 177, Lang: RU, Version: Russian New Testament: Easy-to-Read Version
@mcp.tool()
def get_bible_votd_rntetr():
    """Fetches the Verse of the Day for Russian New Testament: Easy-to-Read Version (ID 177)."""
    url = f"{BIBLE_API_BASE}&version=177"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 39, Lang: RU, Version: New Russian Translation
@mcp.tool()
def get_bible_votd_nrt():
    """Fetches the Verse of the Day for New Russian Translation (ID 39)."""
    url = f"{BIBLE_API_BASE}&version=39"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 13, Lang: RU, Version: Russian Synodal Version
@mcp.tool()
def get_bible_votd_rsv():
    """Fetches the Verse of the Day for Russian Synodal Version (ID 13)."""
    url = f"{BIBLE_API_BASE}&version=13"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')