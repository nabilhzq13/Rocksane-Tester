#!/usr/bin/env python3
"""Refresh Rocksane Free from the main Rocksane source (the RockyMate repo).

Usage (Windows: python, elsewhere python3):
    python update.py                  # uses ../RockyMate next to this folder
    python update.py C:\\path\\to\\RockyMate

It runs RockyMate's build.py, copies its everything-unlocked edition
(dist/beta-lens-live.html: live camera, video, Hold type, all nine examples)
here as index.html with the icons, fonts and privacy/terms/support pages,
and names it "Rocksane Free". Then commit and push; GitHub Pages redeploys.
"""
import json, pathlib, shutil, subprocess, sys

here = pathlib.Path(__file__).resolve().parent
src = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else here.parent / "RockyMate"
if not (src / "build.py").exists():
    sys.exit(f"Can't find RockyMate's build.py in {src}. Pass the folder: python update.py PATH_TO_ROCKYMATE")

subprocess.run([sys.executable, "build.py"], cwd=src, check=True)

page = (src / "dist" / "beta-lens-live.html").read_text(encoding="utf-8")
assert "const EDITION='dev';" in page, "expected the unlocked (dev) edition"
page = page.replace("<title>Rocksane</title>", "<title>Rocksane Free</title>", 1)
page = page.replace('name="apple-mobile-web-app-title" content="Rocksane"', 'name="apple-mobile-web-app-title" content="Rocksane Free"', 1)
(here / "index.html").write_text(page, encoding="utf-8", newline="\n")

for f in sorted((src / "web").iterdir()):
    if f.is_dir():
        shutil.copytree(f, here / f.name, dirs_exist_ok=True)
    else:
        shutil.copy2(f, here / f.name)

mf = here / "manifest.webmanifest"
m = json.loads(mf.read_text(encoding="utf-8"))
m = {"id": "./", "name": "Rocksane Free", "short_name": "Rocksane",
     **{k: v for k, v in m.items() if k not in ("id", "name", "short_name")}}
mf.write_text(json.dumps(m, indent=2) + "\n", encoding="utf-8", newline="\n")
(here / ".nojekyll").touch()
print("Updated index.html", round((here / "index.html").stat().st_size / 1024, 1), "KB. Now commit and push.")
