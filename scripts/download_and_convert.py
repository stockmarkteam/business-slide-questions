import os
from hashlib import sha256
from pathlib import Path

import requests
from pdf2image import convert_from_path
from requests.adapters import HTTPAdapter, Retry
from tqdm import tqdm

pdf_urls_file = "pdf_urls.txt"
pdf_dir = Path("downloads/pdfs")
img_dir = Path("downloads/pngs")
pdf_dir.mkdir(parents=True, exist_ok=True)
img_dir.mkdir(parents=True, exist_ok=True)

session = requests.Session()
retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retries))
session.mount("http://", HTTPAdapter(max_retries=retries))


def hashed_pdf_name(url: str) -> str:
    return sha256(url.encode()).hexdigest() + ".pdf"


def download_pdf(url: str, dest: Path) -> bool:
    try:
        r = session.get(url, stream=True, timeout=60)
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                f.write(chunk)
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        with open("failed_urls.txt", "a") as fail_log:
            fail_log.write(url + "\n")
        return False


def convert_to_png(pdf_path: Path, out_dir: Path):
    try:
        images = convert_from_path(pdf_path)
        for i, img in enumerate(images):
            out_file = out_dir / f"{pdf_path.stem}_page_{i + 1:03}.png"
            img.save(out_file, "PNG")
    except Exception as e:
        print(f"Conversion failed for {pdf_path}: {e}")


with open(pdf_urls_file) as f:
    urls = [line.strip() for line in f if line.strip()]

for url in tqdm(urls, desc="Downloading and Converting"):
    pdf_name = hashed_pdf_name(url)
    pdf_path = pdf_dir / pdf_name
    if not pdf_path.exists():
        if not download_pdf(url, pdf_path):
            continue
    convert_to_png(pdf_path, img_dir)
