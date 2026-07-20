#!/usr/bin/env python3
"""
download.py — idempotent fetch of all raw sources for the v3 dataset layer.

Downloads bulk public extracts into raw/, records sha256 checksums
(raw/checksums.txt) and source URL + retrieval date per file
(raw/sources.json), and deterministically produces trimmed national-level
extracts from the big files so that only small files need to be committed
(raw/.gitignore excludes originals >10MB).

Python 3 stdlib only. Re-running is a no-op for files already present
(delete a file in raw/ to force a re-download). The trim steps are pure
functions of the raw files and are re-run every time (cheap, deterministic).

Sources (all public, fetched with a real User-Agent per BLS policy):
  - Census SUSB 2022:  us_state_6digitnaics_2022.txt (firms/estabs/emp/payroll/
    RECEIPTS by enterprise employment-size class, all NAICS levels 2..6-digit;
    2022 is an Economic Census year so receipts are published)
  - BLS QCEW 2024 annual singlefile (all areas; trimmed to US000 national rows)
  - BLS OEWS May 2024 national industry-specific estimates (oesm24in4.zip,
    xlsx converted to csv with a stdlib xlsx reader)
  - BLS Industry Productivity & Costs (IPS) flat files: labor compensation
    (L02, $M) and sectoral output (T30, $M) by detailed industry
  - BLS ECEC news release (benefits multiplier: total comp / wages, private)
  - Damodaran (NYU Stern) margin table (source document for the hand-curated
    margins.json; not machine-derived)
"""
import csv
import hashlib
import io
import json
import os
import re
import sys
import urllib.request
import zipfile
from datetime import date, timezone
from xml.etree import ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
UA = "rollup-economy-research (lancenta@gmail.com)"

SOURCES = {
    "susb_us_state_6digitnaics_2022.txt":
        "https://www2.census.gov/programs-surveys/susb/tables/2022/us_state_6digitnaics_2022.txt",
    "qcew_2024_annual_singlefile.zip":
        "https://data.bls.gov/cew/data/files/2024/csv/2024_annual_singlefile.zip",
    "oesm24in4.zip":
        "https://www.bls.gov/oes/special-requests/oesm24in4.zip",
    "ip.data.1.AllData":
        "https://download.bls.gov/pub/time.series/ip/ip.data.1.AllData",
    "ip.series":
        "https://download.bls.gov/pub/time.series/ip/ip.series",
    "ip.industry":
        "https://download.bls.gov/pub/time.series/ip/ip.industry",
    "ecec.nr0.htm":
        "https://www.bls.gov/news.release/ecec.nr0.htm",
    "damodaran_margin.html":
        "https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/margin.html",
}

# Originals larger than 10MB — gitignored; the trimmed extracts below are
# committed instead and are pure deterministic filters of these files.
BIG_FILES = [
    "susb_us_state_6digitnaics_2022.txt",   # ~56MB (states); trim: US rows only
    "qcew_2024_annual_singlefile.zip",      # large; trim: area_fips US000 only
    "oesm24in4.zip",                        # ~32MB xlsx; trim: csv conversion
    "ip.data.1.AllData",                    # ~41MB; trim: L02/T30 annual only
]


def fetch(name, url, sources_meta):
    dest = os.path.join(RAW, name)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        print(f"  [skip] {name} (already present)")
        return False
    print(f"  [get ] {name} <- {url}")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    tmp = dest + ".part"
    with urllib.request.urlopen(req, timeout=600) as r, open(tmp, "wb") as f:
        while True:
            chunk = r.read(1 << 20)
            if not chunk:
                break
            f.write(chunk)
    os.replace(tmp, dest)
    sources_meta[name] = {"url": url, "retrieved": date.today().isoformat()}
    print(f"         {os.path.getsize(dest):,} bytes")
    return True


# ---------------------------------------------------------------- xlsx reader
def col_to_idx(ref):
    m = re.match(r"[A-Z]+", ref)
    n = 0
    for ch in m.group():
        n = n * 26 + (ord(ch) - 64)
    return n - 1


def xlsx_to_rows(xlsx_bytes):
    """Minimal stdlib .xlsx reader (single-sheet BLS files). Yields row lists."""
    ns = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
    with zipfile.ZipFile(io.BytesIO(xlsx_bytes)) as z:
        shared = []
        if "xl/sharedStrings.xml" in z.namelist():
            for _, el in ET.iterparse(z.open("xl/sharedStrings.xml")):
                if el.tag == ns + "si":
                    shared.append("".join(t.text or "" for t in el.iter(ns + "t")))
                    el.clear()
        sheets = sorted(n for n in z.namelist()
                        if re.fullmatch(r"xl/worksheets/sheet\d+\.xml", n))
        with z.open(sheets[0]) as sf:
            for _, el in ET.iterparse(sf):
                if el.tag != ns + "row":
                    continue
                row = []
                for c in el.findall(ns + "c"):
                    idx = col_to_idx(c.get("r", "A1"))
                    t = c.get("t")
                    v = c.find(ns + "v")
                    if t == "s":
                        val = shared[int(v.text)] if v is not None else ""
                    elif t == "inlineStr":
                        is_el = c.find(ns + "is")
                        val = "".join(x.text or "" for x in is_el.iter(ns + "t")) if is_el is not None else ""
                    else:
                        val = v.text if v is not None else ""
                    while len(row) <= idx:
                        row.append("")
                    row[idx] = val
                el.clear()
                yield row


# ------------------------------------------------------------------ trim steps
def trim_susb():
    src = os.path.join(RAW, "susb_us_state_6digitnaics_2022.txt")
    out = os.path.join(RAW, "susb_us_2022.csv")
    with open(src, newline="", encoding="latin-1") as f, \
         open(out, "w", newline="", encoding="utf-8") as g:
        rdr = csv.reader(f)
        w = csv.writer(g, lineterminator="\n")
        header = next(rdr)
        w.writerow(header)
        for row in rdr:
            if row and row[0] == "00":       # STATE 00 = United States
                w.writerow(row)
    print(f"  [trim] susb_us_2022.csv ({os.path.getsize(out):,} bytes)")


def trim_qcew():
    src = os.path.join(RAW, "qcew_2024_annual_singlefile.zip")
    out = os.path.join(RAW, "qcew_2024_us000.csv")
    with zipfile.ZipFile(src) as z:
        member = [n for n in z.namelist() if n.lower().endswith(".csv")][0]
        with z.open(member) as f, open(out, "w", newline="", encoding="utf-8") as g:
            txt = io.TextIOWrapper(f, encoding="utf-8", errors="replace")
            header = txt.readline()
            g.write(header.replace("\r\n", "\n"))
            for line in txt:
                if line.startswith('"US000"') or line.startswith("US000"):
                    g.write(line.replace("\r\n", "\n"))
    print(f"  [trim] qcew_2024_us000.csv ({os.path.getsize(out):,} bytes)")


OEWS_KEEP_COLS = ["NAICS", "NAICS_TITLE", "I_GROUP", "OWN_CODE", "OCC_CODE",
                  "OCC_TITLE", "O_GROUP", "TOT_EMP", "A_MEAN"]
OEWS_KEEP_OGROUPS = {"total", "detailed"}   # drop major/minor/broad rollups


def trim_oews():
    src = os.path.join(RAW, "oesm24in4.zip")
    with zipfile.ZipFile(src) as z:
        members = [n for n in z.namelist() if n.lower().endswith(".xlsx")
                   and "owner" not in n.lower()
                   and "file_descriptions" not in n.lower()]
        for m in sorted(members):
            base = os.path.splitext(os.path.basename(m))[0].lower()
            out = os.path.join(RAW, f"oews_{base}.csv")
            if os.path.exists(out) and os.path.getsize(out) > 0:
                print(f"  [skip] oews_{base}.csv (already converted)")
                continue
            print(f"  [trim] converting {m} -> oews_{base}.csv ...")
            with open(out, "w", newline="", encoding="utf-8") as g:
                w = csv.writer(g, lineterminator="\n")
                keep = None
                og_idx = None
                for row in xlsx_to_rows(z.read(m)):
                    if keep is None:                       # header row
                        keep = [row.index(c) for c in OEWS_KEEP_COLS if c in row]
                        og_idx = row.index("O_GROUP")
                        w.writerow([row[i] for i in keep])
                        continue
                    if row[og_idx] not in OEWS_KEEP_OGROUPS:
                        continue
                    w.writerow([row[i] if i < len(row) else "" for i in keep])
            print(f"         {os.path.getsize(out):,} bytes")


def trim_ips():
    series_path = os.path.join(RAW, "ip.series")
    data_path = os.path.join(RAW, "ip.data.1.AllData")
    out = os.path.join(RAW, "ips_L02_T30_annual.csv")
    keep_measures = {"L02", "T30"}     # labor compensation $M / sectoral output $M
    series = {}                        # series_id -> (industry_code, measure_code, seasonal)
    with open(series_path, encoding="utf-8") as f:
        rdr = csv.DictReader(f, delimiter="\t")
        rdr.fieldnames = [c.strip() for c in rdr.fieldnames]
        for row in rdr:
            if row["measure_code"].strip() in keep_measures:
                series[row["series_id"].strip()] = (
                    row["industry_code"].strip(), row["measure_code"].strip(),
                    row["seasonal"].strip())
    with open(data_path, encoding="utf-8") as f, \
         open(out, "w", newline="", encoding="utf-8") as g:
        w = csv.writer(g, lineterminator="\n")
        w.writerow(["series_id", "industry_code", "measure_code", "year", "value"])
        rdr = csv.reader(f, delimiter="\t")
        next(rdr)
        for row in rdr:
            sid = row[0].strip()
            if sid in series and row[2].strip() == "A01":
                ind, meas, _ = series[sid]
                w.writerow([sid, ind, meas, row[1].strip(), row[3].strip()])
    print(f"  [trim] ips_L02_T30_annual.csv ({os.path.getsize(out):,} bytes)")


# --------------------------------------------------------------- housekeeping
def write_gitignore():
    path = os.path.join(RAW, ".gitignore")
    content = "# Originals >10MB — reproduce with ../download.py; the trimmed\n" \
              "# extracts (deterministic filters of these) are committed instead.\n"
    content += "".join(n + "\n" for n in BIG_FILES)
    content += "*.part\n"
    with open(path, "w") as f:
        f.write(content)


def write_checksums():
    path = os.path.join(RAW, "checksums.txt")
    lines = []
    for name in sorted(os.listdir(RAW)):
        if name in (".gitignore", "checksums.txt") or name.endswith(".part"):
            continue
        p = os.path.join(RAW, name)
        if not os.path.isfile(p):
            continue
        h = hashlib.sha256()
        with open(p, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
        lines.append(f"{h.hexdigest()}  {os.path.getsize(p):>12}  {name}")
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"  [ok  ] checksums.txt ({len(lines)} files)")


def main():
    os.makedirs(RAW, exist_ok=True)
    meta_path = os.path.join(RAW, "sources.json")
    sources_meta = {}
    if os.path.exists(meta_path):
        with open(meta_path) as f:
            sources_meta = json.load(f)

    print("== fetch ==")
    for name, url in SOURCES.items():
        try:
            fetch(name, url, sources_meta)
        except Exception as e:
            print(f"  [FAIL] {name}: {e}", file=sys.stderr)
            raise
        # keep url current in metadata even for skipped files
        sources_meta.setdefault(name, {"url": url,
                                       "retrieved": date.today().isoformat()})
        sources_meta[name]["url"] = url
    with open(meta_path, "w") as f:
        json.dump(sources_meta, f, indent=2, sort_keys=True)
        f.write("\n")

    print("== trim ==")
    trim_susb()
    trim_qcew()
    trim_oews()
    trim_ips()

    write_gitignore()
    write_checksums()
    print("done.")


if __name__ == "__main__":
    main()
