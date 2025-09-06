from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("bgw-votd-zh")

# Constants
BIBLE_API_BASE = "https://www.biblegateway.com/votd/get/?format=JSON"

# ID: 205, Lang: ZH, Version: Chinese Contemporary Bible (Simplified)
@mcp.tool()
def get_bible_votd_chinese_cbs():
    """Fetches the Verse of the Day for Chinese Contemporary Bible (Simplified) (ID 205)."""
    url = f"{BIBLE_API_BASE}&version=205"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 254, Lang: ZH, Version: Chinese Contemporary Bible (Traditional)
@mcp.tool()
def get_bible_votd_chinese_cbt():
    """Fetches the Verse of the Day for Chinese Contemporary Bible (Traditional) (ID 254)."""
    url = f"{BIBLE_API_BASE}&version=254"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 243, Lang: ZH, Version: Chinese New Version (Simplified)
@mcp.tool()
def get_bible_votd_chinese_nvs():
    """Fetches the Verse of the Day for Chinese New Version (Simplified) (ID 243)."""
    url = f"{BIBLE_API_BASE}&version=243"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 227, Lang: ZH, Version: Chinese New Version (Traditional)
@mcp.tool()
def get_bible_votd_chinese_nvt():
    """Fetches the Verse of the Day for Chinese New Version (Traditional) (ID 227)."""
    url = f"{BIBLE_API_BASE}&version=227"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 189, Lang: ZH, Version: Chinese Standard Bible (Simplified)
@mcp.tool()
def get_bible_votd_chinese_sbs():
    """Fetches the Verse of the Day for Chinese Standard Bible (Simplified) (ID 189)."""
    url = f"{BIBLE_API_BASE}&version=189"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 190, Lang: ZH, Version: Chinese Standard Bible (Traditional)
@mcp.tool()
def get_bible_votd_chinese_sbt():
    """Fetches the Verse of the Day for Chinese Standard Bible (Traditional) (ID 190)."""
    url = f"{BIBLE_API_BASE}&version=190"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 22, Lang: ZH, Version: Chinese Union Version (Traditional)
@mcp.tool()
def get_bible_votd_chinese_uvt():
    """Fetches the Verse of the Day for Chinese Union Version (Traditional) (ID 22)."""
    url = f"{BIBLE_API_BASE}&version=22"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 191, Lang: ZH, Version: Chinese Union Version Modern Punctuation (Simplified)
@mcp.tool()
def get_bible_votd_chinese_uvmps():
    """Fetches the Verse of the Day for Chinese Union Version Modern Punctuation (Simplified) (ID 191)."""
    url = f"{BIBLE_API_BASE}&version=191"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 192, Lang: ZH, Version: Chinese Union Version Modern Punctuation (Traditional)
@mcp.tool()
def get_bible_votd_chinese_uvmpt():
    """Fetches the Verse of the Day for Chinese Union Version Modern Punctuation (Traditional) (ID 192)."""
    url = f"{BIBLE_API_BASE}&version=192"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 80, Lang: ZH, Version: Chinese Union Version (Simplified)
@mcp.tool()
def get_bible_votd_chinese_uvs():
    """Fetches the Verse of the Day for Chinese Union Version (Simplified) (ID 80)."""
    url = f"{BIBLE_API_BASE}&version=80"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 182, Lang: ZH, Version: Chinese New Testament: Easy-to-Read Version
@mcp.tool()
def get_bible_votd_chinese_ntetr():
    """Fetches the Verse of the Day for Chinese New Testament: Easy-to-Read Version (ID 182)."""
    url = f"{BIBLE_API_BASE}&version=182"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 258, Lang: ZH, Version: Revised Chinese Union Version (Simplified Script) Shen Edition
@mcp.tool()
def get_bible_votd_chinese_uvsse():
    """Fetches the Verse of the Day for Revised Chinese Union Version (Simplified Script) Shen Edition (ID 258)."""
    url = f"{BIBLE_API_BASE}&version=258"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 259, Lang: ZH, Version: Revised Chinese Union Version (Traditional Script) Shen Edition
@mcp.tool()
def get_bible_votd_chinese_uvtse():
    """Fetches the Verse of the Day for Revised Chinese Union Version (Traditional Script) Shen Edition (ID 259)."""
    url = f"{BIBLE_API_BASE}&version=259"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')