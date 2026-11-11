"""Genera le pagine ponte di AI Video Artist: aivideoartistofficial.github.io/<nome>
Per aggiungere o cambiare un link: modifica LINKS, lancia `python -I genera_link.py`, poi commit e push.
I link vecchi nei video restano validi: cambia solo la destinazione."""
from pathlib import Path

LINKS = {
    "higgsfield": ("Higgsfield", "https://higgsfield.ai/?fpr=aiuniverso"),
    "pixverse": ("PixVerse", "https://motivaiprivatelimited.sjv.io/QYNRZ3"),
    "elevenlabs": ("ElevenLabs", "https://try.elevenlabs.io/fbsz4mwj1b6w"),
    "hailuo": ("Hailuo AI", "https://hailuoai.pxf.io/9VxNq5"),
    "vidogrid": ("VidoGrid", "https://vidogrid.ai"),
}

PAGINA = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<meta name="referrer" content="no-referrer-when-downgrade">
<title>{nome} | AI Video Artist</title>
<meta http-equiv="refresh" content="0; url={url}">
<link rel="canonical" href="{url}">
<script>location.replace({url_js});</script>
<style>body{{margin:0;min-height:100vh;display:grid;place-items:center;background:#0B0F2E;color:#e8ecff;font:16px system-ui,sans-serif;text-align:center}}a{{color:#30E0F5}}</style>
</head><body><p>Opening {nome}&hellip;<br><a href="{url}" rel="sponsored">Click here if nothing happens</a></p></body></html>
"""

HOME = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>AI Video Artist</title>
<meta http-equiv="refresh" content="0; url=https://www.youtube.com/@AIVideoArtistOfficial">
</head><body><a href="https://www.youtube.com/@AIVideoArtistOfficial">AI Video Artist on YouTube</a></body></html>
"""

root = Path(__file__).parent
for slug, (nome, url) in LINKS.items():
    (root / f"{slug}.html").write_text(PAGINA.format(nome=nome, url=url, url_js=repr(url)), encoding="utf-8")
    print(f"https://aivideoartistofficial.github.io/{slug}  ->  {url}")
(root / "index.html").write_text(HOME, encoding="utf-8")
(root / "404.html").write_text(HOME, encoding="utf-8")
(root / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
