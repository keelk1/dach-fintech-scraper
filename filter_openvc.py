#!/usr/bin/env python3
import csv, pandas as pd, re

INPUT_FILE  = "OpenVC.csv"
OUTPUT_FILE = "investors_ch_top10.csv"

# ─────────── utils ───────────
def normalize(col: str) -> str:
    return col.replace("\ufeff", "").strip().lower().replace(" ", "_")

def hq_is_switzerland(hq: str) -> bool:
    return bool(hq) and "switzerland" in hq.lower()

def is_vc_or_cvc(t: str) -> bool:
    return t and t.strip().lower() in {"vc", "cvc", "corporate vc"}

def cheque_to_int(raw: str) -> int:
    """Convertit '100000', '100k', '2 M', '' → int"""
    if not raw:
        return 0
    raw = raw.lower().replace(",", "").strip()
    if "k" in raw:
        return int(float(raw.replace("k", "")) * 1_000)
    if "m" in raw:
        return int(float(raw.replace("m", "")) * 1_000_000)
    digits = re.sub(r"[^\d]", "", raw)
    return int(digits) if digits else 0

# ───────── filtre + tri ─────────
def select_top10(path: str):
    out = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        col = {normalize(c): c for c in reader.fieldnames}

        for row in reader:
            if (
                hq_is_switzerland(row.get(col["global_hq"], "")) and
                is_vc_or_cvc(row.get(col["investor_type"], ""))
            ):
                cheque_min = cheque_to_int(row.get(col["first_cheque_minimum"], ""))
                out.append(
                    {
                        "name":   row.get(col["investor_name"]),
                        "website":row.get(col["website"]),
                        "hq":     row.get(col["global_hq"]),
                        "type":   row.get(col["investor_type"]),
                        "first_cheque_min": cheque_min,
                    }
                )

    # tri décroissant et top-10
    out_sorted = sorted(out, key=lambda x: x["first_cheque_min"], reverse=True)[:10]
    return out_sorted

# ─────────── main ────────────
def main():
    df = pd.DataFrame(select_top10(INPUT_FILE))
    df.to_csv(OUTPUT_FILE, index=False)
    print(df)

if __name__ == "__main__":
    main()