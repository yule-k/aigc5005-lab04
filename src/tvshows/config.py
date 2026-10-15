#URL, timeout, output path

from pathlib import Path

URL = "https://api.tvmaze.com/shows?page=0"
TIMEOUT = 10
OUTPUT = Path("data/processed/summary.json")