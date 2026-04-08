"""
Utility script for downloading a small PyTorch documentation subset.

This script is meant for the very first stage of development, where only a few
handpicked pages are needed to test the pipeline.

Responsibilities:
- Read a predefined list of PyTorch documentation URLs.
- Download each page.
- Save them to the raw data directory.
- Make it easy to create a tiny local corpus before building the full pipeline.

This script is intentionally small and focused.
It is for quick setup and testing, not full crawling.
"""
from pathlib import Path
import sys

# Adjust the import path to include the project root so we can import from config and indexing.downloader
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from config import PYTORCH_URLS, RAW_DIR
from indexing.downloader import DocsDownloader

def main() -> None:
    print("Starting download of PyTorch documentation subset...")
    print("Saving raw files to: ", RAW_DIR)

    downloader = DocsDownloader(output_dir=RAW_DIR)
    manifest = downloader.download_pages(PYTORCH_URLS)

    print(f"Downloaded {len(manifest)} files:")
    for item in manifest:
        print(f"- {item['source_url']} -> {item['local_path']} (status: {item['status_code']})")

    print("Download complete. Manifest saved to: ", RAW_DIR / "manifest.json")

if __name__ == "__main__":
    main()