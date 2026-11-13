"""Download the BDG2 files this project needs into data/raw/.

Run from the repo root:  python scripts/download_data.py
"""
from pathlib import Path

import requests

OWNER_REPO = "buds-lab/building-data-genome-project-2"
BRANCH = "master"
PATHS = {
    "electricity_cleaned.csv": "data/meters/cleaned/electricity_cleaned.csv",
    "metadata.csv": "data/metadata/metadata.csv",
    "weather.csv": "data/weather/weather.csv",
}
RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"


def fetch(url: str, dest: Path) -> None:
    with requests.get(url, stream=True, timeout=60) as r:
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=1 << 20):
                f.write(chunk)


def is_lfs_pointer(path: Path) -> bool:
    """Large files in a repo can be Git LFS pointers: tiny text stubs."""
    if path.stat().st_size > 2000:
        return False
    return path.read_text(errors="ignore").startswith("version https://git-lfs")


def download(name: str, repo_path: str) -> None:
    dest = RAW_DIR / name
    if dest.exists():
        print(f"Skipping {name} (already downloaded)")
        return
    print(f"Downloading {name} ...")
    raw_url = f"https://raw.githubusercontent.com/{OWNER_REPO}/{BRANCH}/{repo_path}"
    try:
        fetch(raw_url, dest)
        if is_lfs_pointer(dest):
            print("  File is stored with Git LFS, retrying via the media server ...")
            media_url = f"https://media.githubusercontent.com/media/{OWNER_REPO}/{BRANCH}/{repo_path}"
            fetch(media_url, dest)
    except requests.HTTPError as err:
        dest.unlink(missing_ok=True)
        print(f"  Failed: {err}. Check the filename in the repo on GitHub.")
        return
    print(f"  Saved {dest.name} ({dest.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    for file_name, path in PATHS.items():
        download(file_name, path)