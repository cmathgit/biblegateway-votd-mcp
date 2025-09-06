from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("bgw-votd-tl")

# Constants
BIBLE_API_BASE = "https://www.biblegateway.com/votd/get/?format=JSON"

# ID: 152, Lang: TL, Version: Ang Biblia (1978)
@mcp.tool()
def get_bible_votd_ang_b_1978():
    """Fetches the Verse of the Day for Ang Biblia (1978) (ID 152)."""
    url = f"{BIBLE_API_BASE}&version=152"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 151, Lang: TL, Version: Ang Biblia, 2001
@mcp.tool()
def get_bible_votd_ang_b_2001():
    """Fetches the Verse of the Day for Ang Biblia, 2001 (ID 151)."""
    url = f"{BIBLE_API_BASE}&version=151"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 242, Lang: TL, Version: Ang Dating Biblia (1905)
@mcp.tool()
def get_bible_votd_ang_db_1905():
    """Fetches the Verse of the Day for Ang Dating Biblia (1905) (ID 242)."""
    url = f"{BIBLE_API_BASE}&version=242"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 273, Lang: TL, Version: Ang Salita ng Dios (Tagalog Contemporary Bible)
@mcp.tool()
def get_bible_votd_ang_sndt_cb():
    """Fetches the Verse of the Day for Ang Salita ng Dios (Tagalog Contemporary Bible) (ID 273)."""
    url = f"{BIBLE_API_BASE}&version=273"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 153, Lang: TL, Version: Ang Bagong Tipan: Filipino Standard Version
@mcp.tool()
def get_bible_votd_ang_bt_filipino_sv():
    """Fetches the Verse of the Day for Ang Bagong Tipan: Filipino Standard Version (ID 153)."""
    url = f"{BIBLE_API_BASE}&version=153"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 150, Lang: TL, Version: Magandang Balita Biblia
@mcp.tool()
def get_bible_votd_magandang_bb():
    """Fetches the Verse of the Day for Magandang Balita Biblia (ID 150)."""
    url = f"{BIBLE_API_BASE}&version=150"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 154, Lang: TL, Version: Magandang Balita Biblia (with Deuterocanon)
@mcp.tool()
def get_bible_votd_magandang_bb_w_deut():
    """Fetches the Verse of the Day for Magandang Balita Biblia (with Deuterocanon) (ID 154)."""
    url = f"{BIBLE_API_BASE}&version=154"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 43, Lang: TL, Version: Ang Salita ng Diyos
@mcp.tool()
def get_bible_votd_ang_snd():
    """Fetches the Verse of the Day for Ang Salita ng Diyos (ID 43)."""
    url = f"{BIBLE_API_BASE}&version=43"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')