from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("bgw-votd")

# Constants
BIBLE_API_BASE = "https://www.biblegateway.com/votd/get/?format=JSON"

#ID: 9, lang: Eng, King James Version
@mcp.tool()
def get_bible_votd_kjv():
    """Fetches the Verse of the Day for King James Version (ID 9)."""
    url = f"{BIBLE_API_BASE}&version=9"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

#ID: 45, lang: Eng, Amplified Bible
@mcp.tool()
def get_bible_votd_amp():
    """Fetches the Verse of the Day for Amplified Bible (ID 45)."""
    url = f"{BIBLE_API_BASE}&version=45"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

#ID: 65, lang: Eng, The Message
@mcp.tool()
def get_bible_votd_msg():
    """Fetches the Verse of the Day for The Message (ID 65)."""
    url = f"{BIBLE_API_BASE}&version=65"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 251, Lang: EN, Version: Christian Standard Bible
@mcp.tool()
def get_bible_votd_csb():
    """Fetches the Verse of the Day for Christian Standard Bible (ID 251)."""
    url = f"{BIBLE_API_BASE}&version=251"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 47, Lang: EN, Version: English Standard Version
@mcp.tool()
def get_bible_votd_esv():
    """Fetches the Verse of the Day for English Standard Version (ID 47)."""
    url = f"{BIBLE_API_BASE}&version=47"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 31, Lang: EN, Version: New International Version
@mcp.tool()
def get_bible_votd_niv():
    """Fetches the Verse of the Day for New International Version (ID 31)."""
    url = f"{BIBLE_API_BASE}&version=31"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 51, Lang: EN, Version: New Living Translation
@mcp.tool()
def get_bible_votd_nlt():
    """Fetches the Verse of the Day for New Living Translation (ID 51)."""
    url = f"{BIBLE_API_BASE}&version=51"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')