from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("bgw-votd-pt")

# Constants
BIBLE_API_BASE = "https://www.biblegateway.com/votd/get/?format=JSON"

# ID: 116, Lang: PT, Version: Almeida Revista e Corrigida 2009
@mcp.tool()
def get_bible_votd_arec2009():
    """Fetches the Verse of the Day for Almeida Revista e Corrigida 2009 (ID 116)."""
    url = f"{BIBLE_API_BASE}&version=116"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 117, Lang: PT, Version: Nova Traduҫão na Linguagem de Hoje 2000
@mcp.tool()
def get_bible_votd_ntlh():
    """Fetches the Verse of the Day for Nova Traduҫão na Linguagem de Hoje 2000 (ID 117)."""
    url = f"{BIBLE_API_BASE}&version=117"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 36, Lang: PT, Version: Nova Versão Internacional
@mcp.tool()
def get_bible_votd_nvi():
    """Fetches the Verse of the Day for Nova Versão Internacional (ID 36)."""
    url = f"{BIBLE_API_BASE}&version=36"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 260, Lang: PT, Version: Nova Versão Transformadora
@mcp.tool()
def get_bible_votd_nvt():
    """Fetches the Verse of the Day for Nova Versão Transformadora (ID 260)."""
    url = f"{BIBLE_API_BASE}&version=260"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 37, Lang: PT, Version: O Livro
@mcp.tool()
def get_bible_votd_ol():
    """Fetches the Verse of the Day for O Livro (ID 37)."""
    url = f"{BIBLE_API_BASE}&version=37"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 176, Lang: PT, Version: Portuguese New Testament: Easy-to-Read Version
@mcp.tool()
def get_bible_votd_pnter():
    """Fetches the Verse of the Day for Portuguese New Testament: Easy-to-Read Version (ID 176)."""
    url = f"{BIBLE_API_BASE}&version=176"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')