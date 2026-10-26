"""Baja los adjuntos relevantes del Padlet y extrae su texto a .txt."""
import json, os, re, subprocess, sys, urllib.parse, urllib.request, zipfile, html

ROOT = sys.argv[1]
RAW, TXT = os.path.join(ROOT, "raw"), os.path.join(ROOT, "txt")
os.makedirs(RAW, exist_ok=True); os.makedirs(TXT, exist_ok=True)
BASE = "https://padlet.com/api/10/wishes?wall_hashid=board_VEbRn8lgM4OlneaB&page_start="
HDR = {"Accept": "application/json", "X-Requested-With": "XMLHttpRequest", "User-Agent": "Mozilla/5.0"}

ENS, TEORIA, GRUPAL, MAT, P1 = 356099474, 356099476, 366139012, 356099477, 356099471
NO_LIT = re.compile(r"TIPOS_Y_FUNCIONES|CONTEXTO_EN_EL|P_RRAFO_ARGUMENTATIVO|TIPOLOG_A|MACROESTRUCTURAS|Conectores_y_Marcadores|TIPOS_DE_P_RRAFO|SUTILEZAS|INTENCI_N_DEL_AUTOR|Figuras_ret_ricas|ACTOS_LING|EXPLICAR_UN_AN|efectos_en_el_lector|ISOTOP_A|c_mics|Anclaje|crom_tico|Leer_im_genes|c_digo_verbal|c_digo_visual|bocadillos|SEM_NTICA|ENFOQUES|TEXTO_2__ESTRUCTURA", re.I)

def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=HDR), timeout=60).read()

wishes, cur = [], ""
while True:
    j = json.loads(get(BASE + urllib.parse.quote(cur)))
    wishes += [w["attributes"] for w in j["data"]]
    cur = (j.get("meta") or {}).get("next")
    if not cur: break

def wanted(a):
    s, att = a["wall_section_id"], a.get("attachment") or ""
    if "padletusercontent" not in att: return None
    if s in (ENS, GRUPAL): return "ens"
    if s == TEORIA: return "teoria"
    if s in (MAT, P1) and NO_LIT.search(att): return "nolit"
    return None

def strip(x):
    x = re.sub(r"<w:tab/>", "\t", x); x = re.sub(r"</w:tc>", " | ", x)
    x = re.sub(r"</(w:p|a:p|si)>|<a:br/>", "\n", x); x = re.sub(r"<[^>]+>", "", x)
    return re.sub(r"\n{3,}", "\n\n", html.unescape(x)).strip()

def extract(path):
    low = path.lower()
    if low.endswith(".pdf"):
        return subprocess.run(["pdftotext", "-enc", "UTF-8", "-layout", path, "-"], capture_output=True).stdout.decode("utf-8", "replace")
    z = zipfile.ZipFile(path)
    if low.endswith(".docx"): return strip(z.read("word/document.xml").decode("utf-8"))
    if low.endswith(".xlsx"): return strip(z.read("xl/sharedStrings.xml").decode("utf-8"))
    if low.endswith(".pptx"):
        slides = sorted((n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)), key=lambda n: int(re.findall(r"\d+", n)[0]))
        return "\n".join(f"--- diapositiva {re.findall(r'[0-9]+', n)[0]}\n" + strip(z.read(n).decode("utf-8")) for n in slides)
    return ""

for a in wishes:
    grp = wanted(a)
    if not grp: continue
    att = a["attachment"]
    name = urllib.parse.unquote(att.split("?")[0].rsplit("/", 1)[-1])
    raw = os.path.join(RAW, f"{grp}__{name}")
    try:
        with open(raw, "wb") as f: f.write(get(att))
        text = extract(raw)
        title = (a.get("headline") or a.get("subject") or "").strip()
        with open(os.path.join(TXT, f"{grp}__{os.path.splitext(name)[0]}.txt"), "w", encoding="utf-8") as f:
            f.write(f"TÍTULO EN EL PADLET: {title}\n\n{text}")
        print(f"{grp}\t{len(text)}\t{name}")
    except Exception as e:
        print(f"ERROR\t{name}\t{e}")
