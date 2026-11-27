#!/usr/bin/env python3
"""Kopiert das Farm-Spiel nach farm/ (Wortkasten-Modus) – nur die benutzten Bilder.
Aufruf: python3 tools/build_farm.py <Pfad zum Farm-Ordner mit index.html und assets/>"""
import re, shutil, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
SRC = Path(sys.argv[1]).resolve()
html = (SRC / "index.html").read_text(encoding="utf-8")
assert html.count("<script>") >= 1
html = html.replace("<script>", "<script>window.WORTKASTEN=1</script>\n<script>", 1)
out = ROOT / "farm"
if out.exists(): shutil.rmtree(out)
(out / "assets").mkdir(parents=True)
(out / "index.html").write_text(html, encoding="utf-8")
used = sorted(set(re.findall(r"assets/([A-Za-z0-9_.-]+\.(?:png|jpg))", html)))
for f in used:
    shutil.copy2(SRC / "assets" / f, out / "assets" / f)
print(f"farm/ gebaut: {len(used)} Bilder")
