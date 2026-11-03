#!/usr/bin/env python3
"""
Build this repo from Who Actually Makes' live open data (owner, 3 Nov 2026).

Reads https://whoactuallymakes.com/data/catalog.json, downloads every dataset (JSON + CSV), checks each file's
SHA-256 against the catalog, and writes data/, catalog.json, README.md, datapackage.json, CITATION.cff and
.zenodo.json. The site is the source; this repo is a mirror with a history. Run by the `wam-opendata` job on the
site-jobs server, which commits and pushes only when a data file changed.

    python3 build.py [repo-dir]     prints one line: OK changed=<n> | OK unchanged | FAIL <why>
"""
import csv
import hashlib
import io
import json
import os
import sys
import time
import urllib.request

SITE = "https://whoactuallymakes.com"
CATALOG = SITE + "/data/catalog.json"
REPO = "https://github.com/jeremiahsay/whoactuallymakes-data"
UA = "whoactuallymakes-data-mirror/1.0 (+https://github.com/jeremiahsay/whoactuallymakes-data)"
ORCID = "https://orcid.org/0009-0009-2025-7691"
DOI = "10.5281/zenodo.23920936"  # Zenodo concept DOI: all versions (first release v2026-11-03 = 10.5281/zenodo.23920937)
FRICTIONLESS = {"text": "string", "date": "string", "url": "string", "number": "number", "boolean": "boolean"}


def get(url, tries=3):
    """Fetch url; retry a dropped connection twice (the site's edge sometimes closes one)."""
    for n in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception:  # noqa: BLE001
            if n == tries - 1:
                raise
            time.sleep(5 * (n + 1))


def fail(why):
    print("FAIL " + why)
    sys.exit(1)


def write(path, data):
    """Write bytes or text; return True when the file changed."""
    if isinstance(data, str):
        data = data.encode("utf-8")
    try:
        with open(path, "rb") as f:
            if f.read() == data:
                return False
    except FileNotFoundError:
        pass
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path + ".tmp", "wb") as f:
        f.write(data)
    os.replace(path + ".tmp", path)
    return True


def kb(n):
    return f"{max(1, round(n / 1024))} KB"


def cell(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def main():
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(__file__))
    try:
        cat = json.loads(get(CATALOG))
    except Exception as e:  # noqa: BLE001
        fail(f"catalog: {e}")
    if cat.get("schema") != "wam-data/v1" or not cat.get("datasets"):
        fail("catalog: unexpected schema")

    # Refuse a sudden big drop (a half-built catalog must not wipe history).
    old_cat = os.path.join(root, "catalog.json")
    if os.path.exists(old_cat):
        before = json.load(open(old_cat)).get("records", 0)
        if before and cat["records"] < before * 0.8:
            fail(f"records fell from {before} to {cat['records']}; not mirrored")

    files = {}
    for d in cat["datasets"]:
        for fmt in ("json", "csv"):
            meta = d["files"][fmt]
            try:
                body = get(meta["url"])
            except Exception as e:  # noqa: BLE001
                fail(f"{d['id']}.{fmt}: {e}")
            if hashlib.sha256(body).hexdigest() != meta["sha256"]:
                fail(f"{d['id']}.{fmt}: SHA-256 differs from the catalog (site mid-update?); try next run")
            files[f"data/{d['id']}.{fmt}"] = body

    changed = sum(write(os.path.join(root, p), b) for p, b in files.items())
    # Remove files for datasets the catalog no longer lists.
    keep = set(files)
    for name in os.listdir(os.path.join(root, "data")):
        if f"data/{name}" not in keep:
            os.remove(os.path.join(root, "data", name))
            changed += 1
    version = max(d["updated"] for d in cat["datasets"])
    meta = 0
    if changed:  # the catalog's own "generated" date moves daily; only rewrite it with the data
        meta += write(old_cat, json.dumps(cat, ensure_ascii=False, indent=1) + "\n")
    meta += write(os.path.join(root, "README.md"), readme(cat, version, files))
    meta += write(os.path.join(root, "datapackage.json"), json.dumps(datapackage(cat, version, files), ensure_ascii=False, indent=1) + "\n")
    meta += write(os.path.join(root, "CITATION.cff"), citation(cat, version))
    meta += write(os.path.join(root, ".zenodo.json"), json.dumps(zenodo(cat, version), ensure_ascii=False, indent=1) + "\n")
    if not changed and not meta:
        print("OK unchanged")
        return
    print(f"OK changed={changed} version={version} records={cat['records']}")


def readme(cat, v, files):
    L = []
    a = L.append
    a("# Who Actually Makes: open data")
    a("")
    a(f"[![DOI](https://zenodo.org/badge/DOI/{DOI}.svg)](https://doi.org/{DOI})")
    a("")
    a("Who makes store-brand products, from public records. Every list behind "
      "[Who Actually Makes](https://whoactuallymakes.com/): which company each Kirkland Signature product traces to, "
      "the companies behind store brands and the labels they're on record for, every NHTSA tire plant code, what tire "
      "makers and carmakers say about tire age, and the evidence, sources, corrections and update schedule behind it all.")
    a("")
    a(f"**{cat['count']} datasets · {cat['records']:,} records · version {v}** · JSON and CSV (UTF-8) · "
      f"[CC BY 4.0]({cat['licence']['url']}) · Live copy and API: {cat['url']}")
    a("")
    a("Each answer on the site carries a stamp (confirmed, documented, reported or unverified) and links to the "
      "record it rests on. The evidence file keeps the exact quote, the date it was read and a SHA-256 fingerprint "
      "of the document, so anyone can check a row against its source. How the stamps work: "
      "https://whoactuallymakes.com/how-we-know/")
    a("")
    a("## Datasets")
    a("")
    a("| Dataset | Records | Updated | Files | On the site |")
    a("|---|---:|---|---|---|")
    for d in cat["datasets"]:
        j, c = f"data/{d['id']}.json", f"data/{d['id']}.csv"
        a(f"| [{cell(d['title'])}](#{d['id']}) | {d['records']:,} | {d['updated']} | "
          f"[JSON]({j}) ({kb(len(files[j]))}) · [CSV]({c}) ({kb(len(files[c]))}) | "
          f"[{d['page']}]({SITE}{d['page']}) |")
    a("")
    for d in cat["datasets"]:
        a(f'<a id="{d["id"]}"></a>')
        a("")
        a(f"### {d['title']}")
        a("")
        a(d["what"])
        a("")
        a(f"- **Limits:** {d['limits']}")
        a(f"- **Kept fresh:** {d['refresh']}")
        a(f"- **Rights:** {d['rights']}")
        if d.get("based_on"):
            n = len(d["based_on"])
            a(f"- **Based on:** {n} public source{'s' if n != 1 else ''}, listed in `catalog.json` (`based_on`)")
        a(f"- **Files:** `data/{d['id']}.json`, `data/{d['id']}.csv` · live: {d['files']['json']['url']}")
        a("")
        a("<details><summary>The " + str(len(d["fields"])) + " fields</summary>")
        a("")
        a("| Field | Type | What it holds |")
        a("|---|---|---|")
        for f in d["fields"]:
            a(f"| `{f['name']}` | {f['type']} | {cell(f['about'])} |")
        a("")
        a("</details>")
        a("")
    a("## Use it")
    a("")
    a("```python")
    a("import pandas as pd")
    a('plants = pd.read_csv("https://raw.githubusercontent.com/jeremiahsay/whoactuallymakes-data/main/data/tire-plants.csv")')
    a("```")
    a("")
    a(f"For the always-current copy, read from the site instead: `{SITE}/data/<dataset>.json`. "
      "The catalog (`catalog.json`, also live at /data/catalog.json) lists every file with its size and SHA-256. "
      "`datapackage.json` describes the CSVs for Frictionless Data tools.")
    a("")
    a("## Licence and credit")
    a("")
    a(f"Our rows are licensed [CC BY 4.0]({cat['licence']['url']}): free to reuse, commercially too. "
      f"Credit: **{cat['credit']}**, with a link to {cat['url']}. Quoted words in the evidence and source columns belong "
      "to their publishers. Most records are US government work, in the public domain in the US. See each dataset's "
      "Rights line. To cite it, use the DOI https://doi.org/" + DOI + " (all versions; Zenodo also gives each release its own DOI) "
      "or `CITATION.cff` (GitHub's \"Cite this repository\").")
    a("")
    a("## Corrections")
    a("")
    a("Spotted a wrong row? Tell us at https://whoactuallymakes.com/contact/#wrong. Every change to a published "
      "answer is logged in `data/corrections.csv` and at https://whoactuallymakes.com/corrections/.")
    a("")
    a("## About this repository")
    a("")
    a("The site is the source. This repository mirrors it daily by script (`build.py`): each file is checked against "
      "the catalog's SHA-256 before it is committed, so the git history is a dated record of every change. "
      "Who Actually Makes is published by Numbers Publishing Pte. Ltd., Singapore "
      "(https://numbers.sg/company/), and edited by [Jeremiah Say](https://whoactuallymakes.com/about/) "
      f"([ORCID]({ORCID})).")
    a("")
    return "\n".join(L)


def datapackage(cat, v, files):
    res = []
    for d in cat["datasets"]:
        p = f"data/{d['id']}.csv"
        header = next(csv.reader(io.StringIO(files[p].decode("utf-8-sig"))))
        fields = {f["name"]: f for f in d["fields"]}
        res.append({
            "name": d["id"],
            "path": p,
            "title": d["title"],
            "description": d["what"],
            "format": "csv",
            "mediatype": "text/csv",
            "encoding": "utf-8",
            "bytes": len(files[p]),
            "hash": "sha256:" + hashlib.sha256(files[p]).hexdigest(),
            "schema": {"fields": [
                {"name": h, "type": FRICTIONLESS.get(fields.get(h, {}).get("type"), "string"),
                 **({"format": "uri"} if fields.get(h, {}).get("type") == "url" else {}),
                 "description": fields.get(h, {}).get("about", "")}
                for h in header
            ]},
            "sources": [{"title": u, "path": u} for u in d.get("based_on", [])],
        })
    return {
        "name": "whoactuallymakes-data",
        "id": "https://doi.org/" + DOI,
        "title": cat["title"],
        "description": "Who makes store-brand products, from public records: Kirkland Signature makers, companies behind store brands, NHTSA tire plant codes, tire age guidance, and the evidence behind each answer.",
        "homepage": cat["url"],
        "version": v,
        "licenses": [{"name": "CC-BY-4.0", "path": cat["licence"]["url"], "title": "Creative Commons Attribution 4.0"}],
        "contributors": [
            {"title": "Jeremiah Say", "path": ORCID, "role": "author"},
            {"title": "Who Actually Makes", "path": SITE + "/", "role": "publisher"},
        ],
        "keywords": keywords(cat),
        "resources": res,
    }


def keywords(cat):
    k = ["store brands", "private label", "open data", "public records", "manufacturer"]
    for d in cat["datasets"]:
        for w in d.get("keywords", []):
            if w.lower() not in [x.lower() for x in k]:
                k.append(w)
    return k[:24]


def citation(cat, v):
    return f'''cff-version: 1.2.0
message: "If you use this data, please cite it as below and link to {cat['url']}"
type: dataset
title: "{cat['title']}"
version: "{v}"
date-released: "{v}"
license: CC-BY-4.0
doi: "{DOI}"
url: "{cat['url']}"
repository: "{REPO}"
keywords:
''' + "".join(f'  - "{w}"\n' for w in keywords(cat)[:12]) + f'''authors:
  - family-names: Say
    given-names: Jeremiah
    orcid: "{ORCID}"
    website: "{SITE}/about/"
  - name: Who Actually Makes
    website: "{SITE}/"
'''


def zenodo(cat, v):
    return {
        "title": cat["title"] + " (store-brand makers, tire plant codes, tire age guidance)",
        "upload_type": "dataset",
        "description": "Who makes store-brand products, from public records: which company each Kirkland Signature product traces to, the companies behind store brands and the labels they are on record for, every NHTSA tire plant code, what tire makers and carmakers say about tire age, and the evidence (quote, date read, SHA-256), sources, corrections and update schedule behind each answer. JSON and CSV. Live copy and API: " + cat["url"],
        "creators": [{"name": "Say, Jeremiah", "orcid": ORCID.rsplit("/", 1)[1], "affiliation": "Numbers Publishing Pte. Ltd."}],
        "license": "cc-by-4.0",
        "version": v,
        "keywords": keywords(cat),
        "related_identifiers": [{"identifier": cat["url"], "relation": "isIdenticalTo", "resource_type": "dataset"}],
    }


if __name__ == "__main__":
    main()
