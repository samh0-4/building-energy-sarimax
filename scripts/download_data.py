"""Download the BDG2 files needed for this project into data/raw/."""
from pathlib import Path
from urllib.request import urlretrieve

BASE = "https://media.githubusercontent.com/media/buds-lab/building-data-genome-project-2/master/data"
FILES = {
    "metadata.csv": "metadata/metadata.csv",
    "electricity_cleaned.csv": "meters/cleaned/electricity_cleaned.csv",
    "weather.csv": "weather/weather.csv",
}

raw = Path(__file__).resolve().parent.parent / "data" / "raw"
raw.mkdir(parents=True, exist_ok=True)

for name, path in FILES.items():
    print(f"Downloading {name}...")
    urlretrieve(f"{BASE}/{path}", raw / name)
    print(f"  saved ({(raw / name).stat().st_size / 1e6:.1f} MB)")

print("Done.")