from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("bgw-votd-alt-langs")

# Constants
BIBLE_API_BASE = "https://www.biblegateway.com/votd/get/?format=JSON"

# ID: 94, Lang: AMU, Version: Amuzgo de Guerrero
@mcp.tool()
def get_bible_votd_amuzgo_dg():
    """Fetches the Verse of the Day for Amuzgo de Guerrero (ID 94)."""
    url = f"{BIBLE_API_BASE}&version=94"
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

# ID: 132, Lang: AR, Version: Ketab El Hayat
@mcp.tool()
def get_bible_votd_arabic_keh():
    """Fetches the Verse of the Day for Ketab El Hayat (ID 132)."""
    url = f"{BIBLE_API_BASE}&version=132"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 219, Lang: AWA, Version: Awadhi Bible: Easy-to-Read Version
@mcp.tool()
def get_bible_votd_awa_betr():
    """Fetches the Verse of the Day for Awadhi Bible: Easy-to-Read Version (ID 219)."""
    url = f"{BIBLE_API_BASE}&version=219"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 82, Lang: BG, Version: 1940 Bulgarian Bible
@mcp.tool()
def get_bible_votd_1940_bulgarian_b():
    """Fetches the Verse of the Day for 1940 Bulgarian Bible (ID 82)."""
    url = f"{BIBLE_API_BASE}&version=82"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 249, Lang: BG, Version: Библия, синодално издание
@mcp.tool()
def get_bible_votd_bg_bib():
    """Fetches the Verse of the Day for Библия, синодално издание (ID 249)."""
    url = f"{BIBLE_API_BASE}&version=249"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 216, Lang: BG, Version: Библия, ревизирано издание
@mcp.tool()
def get_bible_votd_bg_bib_rev():
    """Fetches the Verse of the Day for Библия, ревизирано издание (ID 216)."""
    url = f"{BIBLE_API_BASE}&version=216"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 21, Lang: BG, Version: Bulgarian Bible
@mcp.tool()
def get_bible_votd_bulgarian_b():
    """Fetches the Verse of the Day for Bulgarian Bible (ID 21)."""
    url = f"{BIBLE_API_BASE}&version=21"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 95, Lang: BG, Version: Библия, нов превод от оригиналните езици (с неканоничните книги)
@mcp.tool()
def get_bible_votd_bib_nov_prevod():
    """Fetches the Verse of the Day for Библия, нов превод от оригиналните езици (с неканоничните книги) (ID 95)."""
    url = f"{BIBLE_API_BASE}&version=95"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 172, Lang: BG, Version: Bulgarian New Testament: Easy-to-Read Version
@mcp.tool()
def get_bible_votd_bulgarian_ntetr():
    """Fetches the Verse of the Day for Bulgarian New Testament: Easy-to-Read Version (ID 172)."""
    url = f"{BIBLE_API_BASE}&version=172"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 90, Lang: CCO, Version: Chinanteco de Comaltepec
@mcp.tool()
def get_bible_votd_chinanteco_dc():
    """Fetches the Verse of the Day for Chinanteco de Comaltepec (ID 90)."""
    url = f"{BIBLE_API_BASE}&version=90"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 196, Lang: CEB, Version: Ang Pulong Sa Dios
@mcp.tool()
def get_bible_votd_a_pulong_sd():
    """Fetches the Verse of the Day for Ang Pulong Sa Dios (ID 196)."""
    url = f"{BIBLE_API_BASE}&version=196"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 229, Lang: CHR, Version: Cherokee New Testament
@mcp.tool()
def get_bible_votd_cherokee_nt():
    """Fetches the Verse of the Day for Cherokee New Testament (ID 229)."""
    url = f"{BIBLE_API_BASE}&version=229"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 265, Lang: CKB, Version: Kurdi Sorani Standard
@mcp.tool()
def get_bible_votd_c_kurdi_ss():
    """Fetches the Verse of the Day for Kurdi Sorani Standard (ID 265)."""
    url = f"{BIBLE_API_BASE}&version=265"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 98, Lang: CKW, Version: Cakchiquel Occidental
@mcp.tool()
def get_bible_votd_cakchiquel_o():
    """Fetches the Verse of the Day for Cakchiquel Occidental (ID 98)."""
    url = f"{BIBLE_API_BASE}&version=98"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 184, Lang: CS, Version: Bible 21
@mcp.tool()
def get_bible_votd_cs_bible_21():
    """Fetches the Verse of the Day for Bible 21 (ID 184)."""
    url = f"{BIBLE_API_BASE}&version=184"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 29, Lang: CS, Version: Slovo na cestu
@mcp.tool()
def get_bible_votd_slovo_nc():
    """Fetches the Verse of the Day for Slovo na cestu (ID 29)."""
    url = f"{BIBLE_API_BASE}&version=29"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 130, Lang: CY, Version: Beibl William Morgan
@mcp.tool()
def get_bible_votd_b_william_m():
    """Fetches the Verse of the Day for Beibl William Morgan (ID 130)."""
    url = f"{BIBLE_API_BASE}&version=130"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 197, Lang: DA, Version: Bibelen på hverdagsdansk
@mcp.tool()
def get_bible_votd_bp_hverdagsdansk():
    """Fetches the Verse of the Day for Bibelen på hverdagsdansk (ID 197)."""
    url = f"{BIBLE_API_BASE}&version=197"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 11, Lang: DA, Version: Dette er Biblen på dansk
@mcp.tool()
def get_bible_votd_dette_ebp_dansk():
    """Fetches the Verse of the Day for Dette er Biblen på dansk (ID 11)."""
    url = f"{BIBLE_API_BASE}&version=11"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 33, Lang: DE, Version: Hoffnung für Alle
@mcp.tool()
def get_bible_votd_hoffnung_fa():
    """Fetches the Verse of the Day for Hoffnung für Alle (ID 33)."""
    url = f"{BIBLE_API_BASE}&version=33"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 10, Lang: DE, Version: Luther Bibel 1545
@mcp.tool()
def get_bible_votd_luther_b1545():
    """Fetches the Verse of the Day for Luther Bibel 1545 (ID 10)."""
    url = f"{BIBLE_API_BASE}&version=10"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 186, Lang: DE, Version: Neue Genfer Übersetzung
@mcp.tool()
def get_bible_votd_n_genfer_uber():
    """Fetches the Verse of the Day for Neue Genfer Übersetzung (ID 186)."""
    url = f"{BIBLE_API_BASE}&version=186"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 187, Lang: DE, Version: Schlachter 1951
@mcp.tool()
def get_bible_votd_schlachter_1951():
    """Fetches the Verse of the Day for Schlachter 1951 (ID 187)."""
    url = f"{BIBLE_API_BASE}&version=187"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 188, Lang: DE, Version: Schlachter 2000
@mcp.tool()
def get_bible_votd_schlachter_2000():
    """Fetches the Verse of the Day for Schlachter 2000 (ID 188)."""
    url = f"{BIBLE_API_BASE}&version=188"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 218, Lang: FI, Version: Raamattu 1933/38
@mcp.tool()
def get_bible_votd_raamattu_1933_38():
    """Fetches the Verse of the Day for Raamattu 1933/38 (ID 218)."""
    url = f"{BIBLE_API_BASE}&version=218"
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

# ID: 199, Lang: HE, Version: Habrit Hakhadasha/Haderekh
@mcp.tool()
def get_bible_votd_h_hakhadasha_h():
    """Fetches the Verse of the Day for Habrit Hakhadasha/Haderekh (ID 199)."""
    url = f"{BIBLE_API_BASE}&version=199"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 81, Lang: HE, Version: The Westminster Leningrad Codex
@mcp.tool()
def get_bible_votd_westminster_l_codex():
    """Fetches the Verse of the Day for The Westminster Leningrad Codex (ID 81)."""
    url = f"{BIBLE_API_BASE}&version=81"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 220, Lang: HI, Version: Hindi Bible: Easy-to-Read Version
@mcp.tool()
def get_bible_votd_hindi_betr():
    """Fetches the Verse of the Day for Hindi Bible: Easy-to-Read Version (ID 220)."""
    url = f"{BIBLE_API_BASE}&version=220"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 262, Lang: HI, Version: Saral Hindi Bible
@mcp.tool()
def get_bible_votd_s_hindi_b():
    """Fetches the Verse of the Day for Saral Hindi Bible (ID 262)."""
    url = f"{BIBLE_API_BASE}&version=262"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 71, Lang: HIL, Version: Ang Pulong Sang Dios
@mcp.tool()
def get_bible_votd_a_pulong_sd():
    """Fetches the Verse of the Day for Ang Pulong Sang Dios (ID 71)."""
    url = f"{BIBLE_API_BASE}&version=71"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 267, Lang: HNE, Version: New Chhattisgarhi Translation (नवां नियम छत्तीसगढ़ी)
@mcp.tool()
def get_bible_votd_n_chhattisgarhi_t():
    """Fetches the Verse of the Day for New Chhattisgarhi Translation (नवां नियम छत्तीसगढ़ी) (ID 267)."""
    url = f"{BIBLE_API_BASE}&version=267"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 62, Lang: HR, Version: Knijga O Kristu
@mcp.tool()
def get_bible_votd_knijga_ok():
    """Fetches the Verse of the Day for Knijga O Kristu (ID 62)."""
    url = f"{BIBLE_API_BASE}&version=62"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 125, Lang: HR, Version: Hrvatski Novi Zavjet – Rijeka 2001
@mcp.tool()
def get_bible_votd_hnz_rijeka_2001():
    """Fetches the Verse of the Day for Hrvatski Novi Zavjet – Rijeka 2001 (ID 125)."""
    url = f"{BIBLE_API_BASE}&version=125"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 277, Lang: HR, Version: Biblija: suvremeni hrvatski prijevod
@mcp.tool()
def get_bible_votd_bs_hrvatski_p():
    """Fetches the Verse of the Day for Biblija: suvremeni hrvatski prijevod (ID 277)."""
    url = f"{BIBLE_API_BASE}&version=277"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 23, Lang: HT, Version: Haitian Creole Version
@mcp.tool()
def get_bible_votd_haitian_creole_v():
    """Fetches the Verse of the Day for Haitian Creole Version (ID 23)."""
    url = f"{BIBLE_API_BASE}&version=23"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 276, Lang: HT, Version: Nouvo Testaman: Vèsyon Kreyòl Fasil
@mcp.tool()
def get_bible_votd_ntv_kreyol_fasil():
    """Fetches the Verse of the Day for Nouvo Testaman: Vèsyon Kreyòl Fasil (ID 276)."""
    url = f"{BIBLE_API_BASE}&version=276"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 175, Lang: HU, Version: Hungarian Bible: Easy-to-Read Version
@mcp.tool()
def get_bible_votd_hungarian_betr():
    """Fetches the Verse of the Day for Hungarian Bible: Easy-to-Read Version (ID 175)."""
    url = f"{BIBLE_API_BASE}&version=175"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 17, Lang: HU, Version: Hungarian Károli
@mcp.tool()
def get_bible_votd_hungarian_k():
    """Fetches the Verse of the Day for Hungarian Károli (ID 17)."""
    url = f"{BIBLE_API_BASE}&version=17"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 194, Lang: HU, Version: Hungarian New Translation
@mcp.tool()
def get_bible_votd_hungarian_nt():
    """Fetches the Verse of the Day for Hungarian New Translation (ID 194)."""
    url = f"{BIBLE_API_BASE}&version=194"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 169, Lang: HWC, Version: Hawai‘i Pidgin
@mcp.tool()
def get_bible_votd_hawaiian_p():
    """Fetches the Verse of the Day for Hawai‘i Pidgin (ID 169)."""
    url = f"{BIBLE_API_BASE}&version=169"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 18, Lang: IS, Version: Icelandic Bible
@mcp.tool()
def get_bible_votd_icelandic_b():
    """Fetches the Verse of the Day for Icelandic Bible (ID 18)."""
    url = f"{BIBLE_API_BASE}&version=18"
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

# ID: 103, Lang: JAC, Version: Jacalteco, Oriental
@mcp.tool()
def get_bible_votd_jac():
    """Fetches the Verse of the Day for Jacalteco, Oriental (ID 103)."""
    url = f"{BIBLE_API_BASE}&version=103"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 104, Lang: KEK, Version: Kekchi
@mcp.tool()
def get_bible_votd_kek():
    """Fetches the Verse of the Day for Kekchi (ID 104)."""
    url = f"{BIBLE_API_BASE}&version=104"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 252, Lang: KO, Version: Korean Living Bible
@mcp.tool()
def get_bible_votd_korean_lb():
    """Fetches the Verse of the Day for Korean Living Bible (ID 252)."""
    url = f"{BIBLE_API_BASE}&version=252"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 4, Lang: LA, Version: Biblia Sacra Vulgata
@mcp.tool()
def get_bible_votd_bs_vulgata():
    """Fetches the Verse of the Day for Biblia Sacra Vulgata (ID 4)."""
    url = f"{BIBLE_API_BASE}&version=4"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 266, Lang: LG, Version: Endagaano Enkadde nʼEndagaano Empya
@mcp.tool()
def get_bible_votd_ee_nedagaano_e():
    """Fetches the Verse of the Day for Endagaano Enkadde nʼEndagaano Empya (ID 266)."""
    url = f"{BIBLE_API_BASE}&version=266"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 24, Lang: MI, Version: Maori Bible
@mcp.tool()
def get_bible_votd_maori_b():
    """Fetches the Verse of the Day for Maori Bible (ID 24)."""
    url = f"{BIBLE_API_BASE}&version=24"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 122, Lang: MK, Version: Macedonian New Testament
@mcp.tool()
def get_bible_votd_macedonian_nt():
    """Fetches the Verse of the Day for Macedonian New Testament (ID 122)."""
    url = f"{BIBLE_API_BASE}&version=122"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 221, Lang: MR, Version: Marathi Bible: Easy-to-Read Version
@mcp.tool()
def get_bible_votd_marathi_betr():
    """Fetches the Verse of the Day for Marathi Bible: Easy-to-Read Version (ID 221)."""
    url = f"{BIBLE_API_BASE}&version=221"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 88, Lang: MVC, Version: Mam, Central
@mcp.tool()
def get_bible_votd_mam_c():
    """Fetches the Verse of the Day for Mam, Central (ID 88)."""
    url = f"{BIBLE_API_BASE}&version=88"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 107, Lang: MVJ, Version: Mam de Todos Santos Chuchumatán
@mcp.tool()
def get_bible_votd_mam_dt_santos_c():
    """Fetches the Verse of the Day for Mam de Todos Santos Chuchumatán (ID 107)."""
    url = f"{BIBLE_API_BASE}&version=107"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 56, Lang: NDS, Version: Reimer 2001
@mcp.tool()
def get_bible_votd_reimer2001():
    """Fetches the Verse of the Day for Reimer 2001 (ID 56)."""
    url = f"{BIBLE_API_BASE}&version=56"
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

# ID: 109, Lang: NGU, Version: Náhuatl de Guerrero
@mcp.tool()
def get_bible_votd_nd_guerrero():
    """Fetches the Verse of the Day for Náhuatl de Guerrero (ID 109)."""
    url = f"{BIBLE_API_BASE}&version=109"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 255, Lang: NL, Version: BasisBijbel
@mcp.tool()
def get_bible_votd_basis_b():
    """Fetches the Verse of the Day for BasisBijbel (ID 255)."""
    url = f"{BIBLE_API_BASE}&version=255"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 30, Lang: NL, Version: Het Boek
@mcp.tool()
def get_bible_votd_het_b():
    """Fetches the Verse of the Day for Het Boek (ID 30)."""
    url = f"{BIBLE_API_BASE}&version=30"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 5, Lang: NO, Version: Det Norsk Bibelselskap 1930
@mcp.tool()
def get_bible_votd_d_norsk_bs1930():
    """Fetches the Verse of the Day for Det Norsk Bibelselskap 1930 (ID 5)."""
    url = f"{BIBLE_API_BASE}&version=5"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 35, Lang: NO, Version: En Levende Bok
@mcp.tool()
def get_bible_votd_e_levende_b():
    """Fetches the Verse of the Day for En Levende Bok (ID 35)."""
    url = f"{BIBLE_API_BASE}&version=35"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 263, Lang: NY, Version: Mawu a Mulungu mu Chichewa Chalero
@mcp.tool()
def get_bible_votd_mawu_mccm():
    """Fetches the Verse of the Day for Mawu a Mulungu mu Chichewa Chalero (ID 263)."""
    url = f"{BIBLE_API_BASE}&version=263"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 223, Lang: OR, Version: Oriya Bible: Easy-to-Read Version
@mcp.tool()
def get_bible_votd_oriya_betr():
    """Fetches the Verse of the Day for Oriya Bible: Easy-to-Read Version (ID 223)."""
    url = f"{BIBLE_API_BASE}&version=223"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 224, Lang: PA, Version: Punjabi Bible: Easy-to-Read Version
@mcp.tool()
def get_bible_votd_punjabi_betr():
    """Fetches the Verse of the Day for Punjabi Bible: Easy-to-Read Version (ID 224)."""
    url = f"{BIBLE_API_BASE}&version=224"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 193, Lang: PL, Version: Nowe Przymierze
@mcp.tool()
def get_bible_votd_nowe_p():
    """Fetches the Verse of the Day for Nowe Przymierze (ID 193)."""
    url = f"{BIBLE_API_BASE}&version=193"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 200, Lang: PL, Version: Słowo Życia
@mcp.tool()
def get_bible_votd_slovo_z():
    """Fetches the Verse of the Day for Słowo Życia (ID 200)."""
    url = f"{BIBLE_API_BASE}&version=200"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 118, Lang: PL, Version: Updated Gdańsk Bible
@mcp.tool()
def get_bible_votd_u_gdansk():
    """Fetches the Verse of the Day for Updated Gdańsk Bible (ID 118)."""
    url = f"{BIBLE_API_BASE}&version=118"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 247, Lang: PPL, Version: Ne Bibliaj Tik Nawat
@mcp.tool()
def get_bible_votd_nebt_nawat():
    """Fetches the Verse of the Day for Ne Bibliaj Tik Nawat (ID 247)."""
    url = f"{BIBLE_API_BASE}&version=247"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 201, Lang: QU, Version: Mushuj Testamento Diospaj Shimi
@mcp.tool()
def get_bible_votd_mushuj_tds():
    """Fetches the Verse of the Day for Mushuj Testamento Diospaj Shimi (ID 201)."""
    url = f"{BIBLE_API_BASE}&version=201"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 111, Lang: QUT, Version: Quiché, Centro Occidental
@mcp.tool()
def get_bible_votd_quiche_co():
    """Fetches the Verse of the Day for Quiché, Centro Occidental (ID 111)."""
    url = f"{BIBLE_API_BASE}&version=111"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 202, Lang: RO, Version: Nouă Traducere În Limba Română
@mcp.tool()
def get_bible_votd_ntl_romana():
    """Fetches the Verse of the Day for Nouă Traducere În Limba Română (ID 202)."""
    url = f"{BIBLE_API_BASE}&version=202"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 14, Lang: RO, Version: Cornilescu 1924 - Revised 2010, 2014
@mcp.tool()
def get_bible_votd_cornilescu1924_r2010_14():
    """Fetches the Verse of the Day for Cornilescu 1924 - Revised 2010, 2014 (ID 14)."""
    url = f"{BIBLE_API_BASE}&version=14"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 40, Lang: SK, Version: Nádej pre kazdého
@mcp.tool()
def get_bible_votd_nadej_pk():
    """Fetches the Verse of the Day for Nádej pre kazdého (ID 40)."""
    url = f"{BIBLE_API_BASE}&version=40"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 206, Lang: SO, Version: Somali Bible
@mcp.tool()
def get_bible_votd_somali():
    """Fetches the Verse of the Day for Somali Bible (ID 206)."""
    url = f"{BIBLE_API_BASE}&version=206"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 1, Lang: SQ, Version: Albanian Bible
@mcp.tool()
def get_bible_votd_albanian():
    """Fetches the Verse of the Day for Albanian Bible (ID 1)."""
    url = f"{BIBLE_API_BASE}&version=1"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 178, Lang: SR, Version: Serbian New Testament: Easy-to-Read Version
@mcp.tool()
def get_bible_votd_serbian_nter():
    """Fetches the Verse of the Day for Serbian New Testament: Easy-to-Read Version (ID 178)."""
    url = f"{BIBLE_API_BASE}&version=178"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 264, Lang: SR, Version: New Serbian Translation
@mcp.tool()
def get_bible_votd_n_serbian_t():
    """Fetches the Verse of the Day for New Serbian Translation (ID 264)."""
    url = f"{BIBLE_API_BASE}&version=264"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 75, Lang: SW, Version: Neno: Bibilia Takatifu
@mcp.tool()
def get_bible_votd_neno_bt():
    """Fetches the Verse of the Day for Neno: Bibilia Takatifu (ID 75)."""
    url = f"{BIBLE_API_BASE}&version=75"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 274, Lang: SW, Version: Agano Jipya: Tafsiri ya Kusoma-Kwa-Urahisi
@mcp.tool()
def get_bible_votd_agano_jtykke():
    """Fetches the Verse of the Day for Agano Jipya: Tafsiri ya Kusoma-Kwa-Urahisi (ID 274)."""
    url = f"{BIBLE_API_BASE}&version=274"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 225, Lang: TA, Version: Tamil Bible: Easy-to-Read Version
@mcp.tool()
def get_bible_votd_tamil_betr():
    """Fetches the Verse of the Day for Tamil Bible: Easy-to-Read Version (ID 225)."""
    url = f"{BIBLE_API_BASE}&version=225"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 179, Lang: TH, Version: Thai New Testament: Easy-to-Read Version
@mcp.tool()
def get_bible_votd_thai_ntetr():
    """Fetches the Verse of the Day for Thai New Testament: Easy-to-Read Version (ID 179)."""
    url = f"{BIBLE_API_BASE}&version=179"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 279, Lang: TH, Version: New Thai Version
@mcp.tool()
def get_bible_votd_n_thai_v():
    """Fetches the Verse of the Day for New Thai Version (ID 279)."""
    url = f"{BIBLE_API_BASE}&version=279"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 203, Lang: TH, Version: Thai New Contemporary Bible
@mcp.tool()
def get_bible_votd_thai_ncb():
    """Fetches the Verse of the Day for Thai New Contemporary Bible (ID 203)."""
    url = f"{BIBLE_API_BASE}&version=203"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 204, Lang: TWI, Version: Nkwa Asem
@mcp.tool()
def get_bible_votd_nkwa_a():
    """Fetches the Verse of the Day for Nkwa Asem (ID 204)."""
    url = f"{BIBLE_API_BASE}&version=204"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 180, Lang: UK, Version: Ukrainian New Testament: Easy-to-Read Version
@mcp.tool()
def get_bible_votd_ukrainian_ntetr():
    """Fetches the Verse of the Day for Ukrainian New Testament: Easy-to-Read Version (ID 180)."""
    url = f"{BIBLE_API_BASE}&version=180"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 27, Lang: UK, Version: Ukrainian Bible
@mcp.tool()
def get_bible_votd_ukrainian_b():
    """Fetches the Verse of the Day for Ukrainian Bible (ID 27)."""
    url = f"{BIBLE_API_BASE}&version=27"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 226, Lang: UR, Version: Urdu Bible: Easy-to-Read Version
@mcp.tool()
def get_bible_votd_urdu_betr():
    """Fetches the Verse of the Day for Urdu Bible: Easy-to-Read Version (ID 226)."""
    url = f"{BIBLE_API_BASE}&version=226"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 113, Lang: USP, Version: Uspanteco
@mcp.tool()
def get_bible_votd_uspanteco():
    """Fetches the Verse of the Day for Uspanteco (ID 113)."""
    url = f"{BIBLE_API_BASE}&version=113"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 207, Lang: VI, Version: Bản Dịch 2011
@mcp.tool()
def get_bible_votd_ban_dich_2011():
    """Fetches the Verse of the Day for Bản Dịch 2011 (ID 207)."""
    url = f"{BIBLE_API_BASE}&version=207"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 181, Lang: VI, Version: Vietnamese Bible: Easy-to-Read Version
@mcp.tool()
def get_bible_votd_vietnamese_betr():
    """Fetches the Verse of the Day for Vietnamese Bible: Easy-to-Read Version (ID 181)."""
    url = f"{BIBLE_API_BASE}&version=181"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 147, Lang: VI, Version: New Vietnamese Bible
@mcp.tool()
def get_bible_votd_new_vietnamese_b():
    """Fetches the Verse of the Day for New Vietnamese Bible (ID 147)."""
    url = f"{BIBLE_API_BASE}&version=147"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

# ID: 268, Lang: YO, Version: Bíbélì Mímọ́ Yorùbá Òde Ònì
@mcp.tool()
def get_bible_votd_b_m_yoruba_oo():
    """Fetches the Verse of the Day for Bíbélì Mímọ́ Yorùbá Òde Ònì (ID 268)."""
    url = f"{BIBLE_API_BASE}&version=268"
    response = httpx.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')