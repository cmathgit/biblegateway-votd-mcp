from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("bgw-votd-es")

# Constants
BIBLE_API_BASE = "https://www.biblegateway.com/votd/get/?format=JSON"

# ID: 208, Lang: ES, Version: La Palabra (España)
@mcp.tool()
def get_bible_votd_lpes():
    """Fetches the Verse of the Day for La Palabra (España) (ID 208)."""
    url = f"{BIBLE_API_BASE}&version=208"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 209, Lang: ES, Version: La Palabra (Hispanoamérica)
@mcp.tool()
def get_bible_votd_lah():
    """Fetches the Verse of the Day for La Palabra (Hispanoamérica) (ID 209)."""
    url = f"{BIBLE_API_BASE}&version=209"
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

# ID: 58, Lang: ES, Version: Dios Habla Hoy
@mcp.tool()
def get_bible_votd_dhh():
    """Fetches the Verse of the Day for Dios Habla Hoy (ID 58)."""
    url = f"{BIBLE_API_BASE}&version=58"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 246, Lang: ES, Version: Biblia del Jubileo
@mcp.tool()
def get_bible_votd_bjb():
    """Fetches the Verse of the Day for Biblia del Jubileo (ID 246)."""
    url = f"{BIBLE_API_BASE}&version=246"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 59, Lang: ES, Version: La Biblia de las Américas
@mcp.tool()
def get_bible_votd_lbda():
    """Fetches the Verse of the Day for La Biblia de las Américas (ID 59)."""
    url = f"{BIBLE_API_BASE}&version=59"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 160, Lang: ES, Version: Nueva Biblia de las Américas
@mcp.tool()
def get_bible_votd_nbda():
    """Fetches the Verse of the Day for Nueva Biblia de las Américas (ID 160)."""
    url = f"{BIBLE_API_BASE}&version=160"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 12, Lang: ES, Version: Nueva Biblia Viva
@mcp.tool()
def get_bible_votd_nbv():
    """Fetches the Verse of the Day for Nueva Biblia Viva (ID 12)."""
    url = f"{BIBLE_API_BASE}&version=12"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 159, Lang: ES, Version: Nueva Traducción Viviente
@mcp.tool()
def get_bible_votd_ntv():
    """Fetches the Verse of the Day for Nueva Traducción Viviente (ID 159)."""
    url = f"{BIBLE_API_BASE}&version=159"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 42, Lang: ES, Version: Nueva Versión Internacional
@mcp.tool()
def get_bible_votd_nvi():
    """Fetches the Verse of the Day for Nueva Versión Internacional (ID 42)."""
    url = f"{BIBLE_API_BASE}&version=42"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 174, Lang: ES, Version: Palabra de Dios para Todos
@mcp.tool()
def get_bible_votd_pdpt():
    """Fetches the Verse of the Day for Palabra de Dios para Todos (ID 174)."""
    url = f"{BIBLE_API_BASE}&version=174"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 6, Lang: ES, Version: Reina-Valera Antigua
@mcp.tool()
def get_bible_votd_rvant():
    """Fetches the Verse of the Day for Reina-Valera Antigua (ID 6)."""
    url = f"{BIBLE_API_BASE}&version=6"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 149, Lang: ES, Version: Reina Valera Actualizada
@mcp.tool()
def get_bible_votd_rva():
    """Fetches the Verse of the Day for Reina Valera Actualizada (ID 149)."""
    url = f"{BIBLE_API_BASE}&version=149"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 162, Lang: ES, Version: Reina Valera Contemporánea
@mcp.tool()
def get_bible_votd_rvc():
    """Fetches the Verse of the Day for Reina Valera Contemporánea (ID 162)."""
    url = f"{BIBLE_API_BASE}&version=162"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 60, Lang: ES, Version: Reina-Valera 1960
@mcp.tool()
def get_bible_votd_rv1960():
    """Fetches the Verse of the Day for Reina-Valera 1960 (ID 60)."""
    url = f"{BIBLE_API_BASE}&version=60"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 241, Lang: ES, Version: Reina Valera Revisada
@mcp.tool()
def get_bible_votd_rvr():
    """Fetches the Verse of the Day for Reina Valera Revisada (ID 241)."""
    url = f"{BIBLE_API_BASE}&version=241"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 61, Lang: ES, Version: Reina-Valera 1995
@mcp.tool()
def get_bible_votd_rv1995():
    """Fetches the Verse of the Day for Reina-Valera 1995 (ID 61)."""
    url = f"{BIBLE_API_BASE}&version=61"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 248, Lang: ES, Version: Spanish Blue Red and Gold Letter Edition
@mcp.tool()
def get_bible_votd_sbrg():
    """Fetches the Verse of the Day for Spanish Blue Red and Gold Letter Edition (ID 248)."""
    url = f"{BIBLE_API_BASE}&version=248"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 57, Lang: ES, Version: Traducción en lenguaje actual
@mcp.tool()
def get_bible_votd_tela():
    """Fetches the Verse of the Day for Traducción en lenguaje actual (ID 57)."""
    url = f"{BIBLE_API_BASE}&version=57"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')