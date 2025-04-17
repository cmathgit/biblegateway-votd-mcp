from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("bgw-votd-grc")

# Constants
BIBLE_API_BASE = "https://www.biblegateway.com/votd/get/?format=JSON"

# ID: 161, Lang: GRC, Version: SBL Greek New Testament
@mcp.tool()
def get_bible_votd_sbl_gnt():
    """Fetches the Verse of the Day for SBL Greek New Testament (ID 161)."""
    url = f"{BIBLE_API_BASE}&version=161"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 270, Lang: GRC, Version: Tyndale House Greek New Testament
@mcp.tool()
def get_bible_votd_th_gnt():
    """Fetches the Verse of the Day for Tyndale House Greek New Testament (ID 270)."""
    url = f"{BIBLE_API_BASE}&version=270"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 69, Lang: GRC, Version: 1550 Stephanus New Testament
@mcp.tool()
def get_bible_votd_v1550_snt():
    """Fetches the Verse of the Day for 1550 Stephanus New Testament (ID 69)."""
    url = f"{BIBLE_API_BASE}&version=69"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 70, Lang: GRC, Version: 1894 Scrivener New Testament
@mcp.tool()
def get_bible_votd_v1894_snt():
    """Fetches the Verse of the Day for 1894 Scrivener New Testament (ID 70)."""
    url = f"{BIBLE_API_BASE}&version=70"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 68, Lang: GRC, Version: 1881 Westcott-Hort New Testament
@mcp.tool()
def get_bible_votd_v1881_whnt():
    """Fetches the Verse of the Day for 1881 Westcott-Hort New Testament (ID 68)."""
    url = f"{BIBLE_API_BASE}&version=68"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')