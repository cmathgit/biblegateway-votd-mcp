from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("bgw-votd-eng")

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

#ID: 240, lang: Eng, Authorized King James Version
@mcp.tool()
def get_bible_votd_akjv():
    """Fetches the Verse of the Day for Authorized King James Version (ID 240)."""
    url = f"{BIBLE_API_BASE}&version=240"
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

#ID: 52, lang: Eng, Amplified Bible Classic
@mcp.tool()
def get_bible_votd_amp_classic():
    """Fetches the Verse of the Day for Amplified Bible Classic (ID 52)."""
    url = f"{BIBLE_API_BASE}&version=52"
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

#ID: 8, lang: Eng, American Standard Version
@mcp.tool()
def get_bible_votd_asv():
    """Fetches the Verse of the Day for American Standard Version (ID 8)."""
    url = f"{BIBLE_API_BASE}&version=8"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

#ID: 128, lang: Eng, BRG Bible Version
@mcp.tool()
def get_bible_votd_brg():
    """Fetches the Verse of the Day for BRG Bible Version (ID 128)."""
    url = f"{BIBLE_API_BASE}&version=128"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 105, Lang: EN, Version: Common English Bible
@mcp.tool()
def get_bible_votd_ceb():
    """Fetches the Verse of the Day for Common English Bible (ID 105)."""
    url = f"{BIBLE_API_BASE}&version=105"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 46, Lang: EN, Version: Contemporary English Version
@mcp.tool()
def get_bible_votd_cev():
    """Fetches the Verse of the Day for Contemporary English Version (ID 46)."""
    url = f"{BIBLE_API_BASE}&version=46"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 195, Lang: EN, Version: Complete Jewish Bible
@mcp.tool()
def get_bible_votd_cjb():
    """Fetches the Verse of the Day for Complete Jewish Bible (ID 195)."""
    url = f"{BIBLE_API_BASE}&version=195"
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

# ID: 16, Lang: EN, Version: Darby Translation
@mcp.tool()
def get_bible_votd_darby():
    """Fetches the Verse of the Day for Darby Translation (ID 16)."""
    url = f"{BIBLE_API_BASE}&version=16"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 123, Lang: EN, Version: Disciples’ Literal New Testament
@mcp.tool()
def get_bible_votd_dlnt():
    """Fetches the Verse of the Day for Disciples’ Literal New Testament (ID 123)."""
    url = f"{BIBLE_API_BASE}&version=123"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 63, Lang: EN, Version: Douay-Rheims 1899 American Edition
@mcp.tool()
def get_bible_votd_dr_1899_ae():
    """Fetches the Verse of the Day for Douay-Rheims 1899 American Edition (ID 63)."""
    url = f"{BIBLE_API_BASE}&version=63"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 285, Lang: EN, Version: EasyEnglish Bible
@mcp.tool()
def get_bible_votd_eeb():
    """Fetches the Verse of the Day for EasyEnglish Bible (ID 285)."""
    url = f"{BIBLE_API_BASE}&version=285"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 257, Lang: EN, Version: Evangelical Heritage Version
@mcp.tool()
def get_bible_votd_ehv():
    """Fetches the Verse of the Day for Evangelical Heritage Version (ID 257)."""
    url = f"{BIBLE_API_BASE}&version=257"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 173, Lang: EN, Version: Easy-to-Read Version
@mcp.tool()
def get_bible_votd_etrv():
    """Fetches the Verse of the Day for Easy-to-Read Version (ID 173)."""
    url = f"{BIBLE_API_BASE}&version=173"
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

# ID: 166, Lang: EN, Version: English Standard Version Anglicised
@mcp.tool()
def get_bible_votd_esva():
    """Fetches the Verse of the Day for English Standard Version Anglicised (ID 166)."""
    url = f"{BIBLE_API_BASE}&version=166"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 233, Lang: EN, Version: Expanded Bible
@mcp.tool()
def get_bible_votd_exb():
    """Fetches the Verse of the Day for Expanded Bible (ID 233)."""
    url = f"{BIBLE_API_BASE}&version=233"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 86, Lang: EN, Version: Good News Translation
@mcp.tool()
def get_bible_votd_gnv():
    """Fetches the Verse of the Day for Good News Translation (ID 86)."""
    url = f"{BIBLE_API_BASE}&version=86"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 236, Lang: EN, Version: 1599 Geneva Bible
@mcp.tool()
def get_bible_votd_v1599gb():
    """Fetches the Verse of the Day for 1599 Geneva Bible (ID 236)."""
    url = f"{BIBLE_API_BASE}&version=236"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 158, Lang: EN, Version: GOD’S WORD Translation
@mcp.tool()
def get_bible_votd_gwv():
    """Fetches the Verse of the Day for GOD’S WORD Translation (ID 158)."""
    url = f"{BIBLE_API_BASE}&version=158"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 77, Lang: EN, Version: Holman Christian Standard Bible
@mcp.tool()
def get_bible_votd_hcsb():
    """Fetches the Verse of the Day for Holman Christian Standard Bible (ID 77)."""
    url = f"{BIBLE_API_BASE}&version=77"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 232, Lang: EN, Version: International Children’s Bible
@mcp.tool()
def get_bible_votd_icb():
    """Fetches the Verse of the Day for International Children’s Bible (ID 232)."""
    url = f"{BIBLE_API_BASE}&version=232"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 124, Lang: EN, Version: International Standard Version
@mcp.tool()
def get_bible_votd_isv():
    """Fetches the Verse of the Day for International Standard Version (ID 124)."""
    url = f"{BIBLE_API_BASE}&version=124"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 245, Lang: EN, Version: Jubilee Bible 2000
@mcp.tool()
def get_bible_votd_jb2000():
    """Fetches the Verse of the Day for Jubilee Bible 2000 (ID 245)."""
    url = f"{BIBLE_API_BASE}&version=245"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 48, Lang: EN, Version: 21st Century King James Version
@mcp.tool()
def get_bible_votd_v21stckjv():
    """Fetches the Verse of the Day for 21st Century King James Version (ID 48)."""
    url = f"{BIBLE_API_BASE}&version=48"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 165, Lang: EN, Version: Lexham English Bible
@mcp.tool()
def get_bible_votd_leb():
    """Fetches the Verse of the Day for Lexham English Bible (ID 165)."""
    url = f"{BIBLE_API_BASE}&version=165"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 283, Lang: EN, Version: Legacy Standard Bible
@mcp.tool()
def get_bible_votd_lsb():
    """Fetches the Verse of the Day for Legacy Standard Bible (ID 283)."""
    url = f"{BIBLE_API_BASE}&version=283"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 126, Lang: EN, Version: Modern English Version
@mcp.tool()
def get_bible_votd_mev():
    """Fetches the Verse of the Day for Modern English Version (ID 126)."""
    url = f"{BIBLE_API_BASE}&version=126"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 217, Lang: EN, Version: Mounce Reverse Interlinear New Testament
@mcp.tool()
def get_bible_votd_mir():
    """Fetches the Verse of the Day for Mounce Reverse Interlinear New Testament (ID 217)."""
    url = f"{BIBLE_API_BASE}&version=217"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 115, Lang: EN, Version: New American Bible (Revised Edition)
@mcp.tool()
def get_bible_votd_nabr():
    """Fetches the Verse of the Day for New American Bible (Revised Edition) (ID 115)."""
    url = f"{BIBLE_API_BASE}&version=115"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 49, Lang: EN, Version: New American Standard Bible
@mcp.tool()
def get_bible_votd_nasb():
    """Fetches the Verse of the Day for New American Standard Bible (ID 49)."""
    url = f"{BIBLE_API_BASE}&version=49"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 275, Lang: EN, Version: New American Standard Bible 1995
@mcp.tool()
def get_bible_votd_nasb1995():
    """Fetches the Verse of the Day for New American Standard Bible 1995 (ID 275)."""
    url = f"{BIBLE_API_BASE}&version=275"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 280, Lang: EN, Version: New Catholic Bible
@mcp.tool()
def get_bible_votd_ncb():
    """Fetches the Verse of the Day for New Catholic Bible (ID 280)."""
    url = f"{BIBLE_API_BASE}&version=280"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 78, Lang: EN, Version: New Century Version
@mcp.tool()
def get_bible_votd_ncv():
    """Fetches the Verse of the Day for New Century Version (ID 78)."""
    url = f"{BIBLE_API_BASE}&version=78"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 234, Lang: EN, Version: New English Translation
@mcp.tool()
def get_bible_votd_net():
    """Fetches the Verse of the Day for New English Translation (ID 234)."""
    url = f"{BIBLE_API_BASE}&version=234"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 76, Lang: EN, Version: New International Reader's Version
@mcp.tool()
def get_bible_votd_nirv():
    """Fetches the Verse of the Day for New International Reader's Version (ID 76)."""
    url = f"{BIBLE_API_BASE}&version=76"
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

# ID: 64, Lang: EN, Version: New International Version - UK
@mcp.tool()
def get_bible_votd_nivuk():
    """Fetches the Verse of the Day for New International Version - UK (ID 64)."""
    url = f"{BIBLE_API_BASE}&version=64"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 50, Lang: EN, Version: New King James Version
@mcp.tool()
def get_bible_votd_nkjv():
    """Fetches the Verse of the Day for New King James Version (ID 50)."""
    url = f"{BIBLE_API_BASE}&version=50"
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

# ID: 74, Lang: EN, Version: New Life Version
@mcp.tool()
def get_bible_votd_nlv():
    """Fetches the Verse of the Day for New Life Version (ID 74)."""
    url = f"{BIBLE_API_BASE}&version=74"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 250, Lang: EN, Version: New Matthew Bible
@mcp.tool()
def get_bible_votd_nmb():
    """Fetches the Verse of the Day for New Matthew Bible (ID 250)."""
    url = f"{BIBLE_API_BASE}&version=250"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 239, Lang: EN, Version: Names of God Bible
@mcp.tool()
def get_bible_votd_nogb():
    """Fetches the Verse of the Day for Names of God Bible (ID 239)."""
    url = f"{BIBLE_API_BASE}&version=239"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 211, Lang: EN, Version: New Revised Standard Version, Anglicised
@mcp.tool()
def get_bible_votd_nrsva():
    """Fetches the Verse of the Day for New Revised Standard Version, Anglicised (ID 211)."""
    url = f"{BIBLE_API_BASE}&version=211"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 213, Lang: EN, Version: New Revised Standard Version, Anglicised Catholic Edition
@mcp.tool()
def get_bible_votd_nrsvac():
    """Fetches the Verse of the Day for New Revised Standard Version, Anglicised Catholic Edition (ID 213)."""
    url = f"{BIBLE_API_BASE}&version=213"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 212, Lang: EN, Version: New Revised Standard Version Catholic Edition
@mcp.tool()
def get_bible_votd_nrsvac():
    """Fetches the Verse of the Day for New Revised Standard Version Catholic Edition (ID 212)."""
    url = f"{BIBLE_API_BASE}&version=212"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 282, Lang: EN, Version: New Revised Standard Version Updated Edition
@mcp.tool()
def get_bible_votd_nrsvued():
    """Fetches the Verse of the Day for New Revised Standard Version Updated Edition (ID 282)."""
    url = f"{BIBLE_API_BASE}&version=282"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 284, Lang: EN, Version: New Testament for Everyone
@mcp.tool()
def get_bible_votd_nte():
    """Fetches the Verse of the Day for New Testament for Everyone (ID 284)."""
    url = f"{BIBLE_API_BASE}&version=284"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 228, Lang: EN, Version: Orthodox Jewish Bible
@mcp.tool()
def get_bible_votd_ojb():
    """Fetches the Verse of the Day for Orthodox Jewish Bible (ID 228)."""
    url = f"{BIBLE_API_BASE}&version=228"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 164, Lang: EN, Version: J.B. Phillips New Testament
@mcp.tool()
def get_bible_votd_jbp():
    """Fetches the Verse of the Day for J.B. Phillips New Testament (ID 164)."""
    url = f"{BIBLE_API_BASE}&version=164"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 271, Lang: EN, Version: Revised Geneva Translation
@mcp.tool()
def get_bible_votd_rgv():
    """Fetches the Verse of the Day for Revised Geneva Translation (ID 271)."""
    url = f"{BIBLE_API_BASE}&version=271"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 214, Lang: EN, Version: Revised Standard Version
@mcp.tool()
def get_bible_votd_rsv():
    """Fetches the Verse of the Day for Revised Standard Version (ID 214)."""
    url = f"{BIBLE_API_BASE}&version=214"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 215, Lang: EN, Version: Revised Standard Version Catholic Edition
@mcp.tool()
def get_bible_votd_rsvc():
    """Fetches the Verse of the Day for Revised Standard Version Catholic Edition (ID 215)."""
    url = f"{BIBLE_API_BASE}&version=215"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 114, Lang: EN, Version: Living Bible
@mcp.tool()
def get_bible_votd_lb():
    """Fetches the Verse of the Day for Living Bible (ID 114)."""
    url = f"{BIBLE_API_BASE}&version=114"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 146, Lang: EN, Version: Tree of Life Version
@mcp.tool()
def get_bible_votd_tolv():
    """Fetches the Verse of the Day for Tree of Life Version (ID 146)."""
    url = f"{BIBLE_API_BASE}&version=146"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 237, Lang: EN, Version: The Voice
@mcp.tool()
def get_bible_votd_tv():
    """Fetches the Verse of the Day for The Voice (ID 237)."""
    url = f"{BIBLE_API_BASE}&version=237"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 73, Lang: EN, Version: Worldwide English (New Testament)
@mcp.tool()
def get_bible_votd_we():
    """Fetches the Verse of the Day for Worldwide English (New Testament) (ID 73)."""
    url = f"{BIBLE_API_BASE}&version=73"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 235, Lang: EN, Version: World English Bible
@mcp.tool()
def get_bible_votd_web():
    """Fetches the Verse of the Day for World English Bible (ID 235)."""
    url = f"{BIBLE_API_BASE}&version=235"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 53, Lang: EN, Version: Wycliffe Bible
@mcp.tool()
def get_bible_votd_wb():
    """Fetches the Verse of the Day for Wycliffe Bible (ID 53)."""
    url = f"{BIBLE_API_BASE}&version=53"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 15, Lang: EN, Version: Young's Literal Translation
@mcp.tool()
def get_bible_votd_ylt():
    """Fetches the Verse of the Day for Young's Literal Translation (ID 15)."""
    url = f"{BIBLE_API_BASE}&version=15"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')