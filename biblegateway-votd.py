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

# ID: 198, Lang: ES, Version: Nueva Versión Internacional (Castilian)
@mcp.tool()
def get_bible_votd_nvic():
    """Fetches the Verse of the Day for Nueva Versión Internacional (Castilian) (ID 198)."""
    url = f"{BIBLE_API_BASE}&version=198"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 171, Lang: AR, Version: Arabic Bible: Easy-to-Read Version
@mcp.tool()
def get_bible_votd_arabic_betr():
    """Fetches the Verse of the Day for Arabic Bible: Easy-to-Read Version (ID 171)."""
    url = f"{BIBLE_API_BASE}&version=171"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 253, Lang: JA, Version: Japanese Living Bible
@mcp.tool()
def get_bible_votd_japanese_lb():
    """Fetches the Verse of the Day for Japanese Living Bible (ID 253)."""
    url = f"{BIBLE_API_BASE}&version=253"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 222, Lang: NE, Version: Nepali Bible: Easy-to-Read Version
@mcp.tool()
def get_bible_votd_nepali_betr():
    """Fetches the Verse of the Day for Nepali Bible: Easy-to-Read Version (ID 222)."""
    url = f"{BIBLE_API_BASE}&version=222"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 278, Lang: GU, Version: Gujarati: પવિત્ર બાઈબલ
@mcp.tool()
def get_bible_votd_pavitra_b():
    """Fetches the Verse of the Day for Gujarati: પવિત્ર બાઈબલ Pavitra Baibal (ID 278)."""
    url = f"{BIBLE_API_BASE}&version=278"
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

# ID: 191, Lang: ZH, Version: Chinese Union Version Modern Punctuation (Simplified)
@mcp.tool()
def get_bible_votd_chinese_uvmps():
    """Fetches the Verse of the Day for Chinese Union Version Modern Punctuation (Simplified) (ID 191)."""
    url = f"{BIBLE_API_BASE}&version=191"
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

# ID: 168, Lang: FR, Version: Nouvelle Edition de Genève – NEG1979
@mcp.tool()
def get_bible_votd_neg1979():
    """Fetches the Verse of the Day for Nouvelle Edition de Genève – NEG1979 (ID 168)."""
    url = f"{BIBLE_API_BASE}&version=168"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')