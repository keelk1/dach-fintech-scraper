# Swiss VC / CVC Ticket-Size Scraper

This tiny script shows I can **pull raw data, clean it, filter it, sort it, and ship it** – exactly what an early-stage fund needs for fast deal-flow research.

| What it does | Why it matters to you |
|--------------|-----------------------|
| Reads the open-licensed **OpenVC** investors CSV (local copy in the repo) | Uses public data, no licensing headache |
| Keeps only 🇨🇭 **Swiss-HQ** funds whose *Investor type* is **VC** or **Corporate VC** | Focus on funds that can actually co-invest with you |
| Parses messy ticket strings (`500 k`, `2 M`, `100000`) → integers | Turns marketing fluff into sortable numbers |
| Ranks by the **largest “first cheque min”** and exports the Top-10 | Instantly tells you who can lead / anchor a pre-seed round |

## Quick start

```bash
# 1 – set up once
python3 -m venv venv && source venv/bin/activate
pip install pandas

# 2 – run
python filter_openvc.py     # prints table + writes investors_ch_top10.csv
