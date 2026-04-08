"""
Documentation downloader for RAGnarok.

This module handles collecting documentation pages and saving them locally so
the assistant can operate fully offline.

Responsibilities:
- Download raw documentation pages from chosen source URLs.
- Save the raw HTML or source text to the project's data directory.
- Keep track of where each file came from, such as original URL and filename.
- Start with a small fixed subset of PyTorch docs for v1.
- Later, possibly expand to larger crawls or full-library snapshots.

This module should only handle acquisition of source documents.
It should not parse, chunk, embed, or answer questions.
"""
from __future__ import annotations

from config import REQUEST_TIMEOUT_SECONDS, USER_AGENT
from pathlib import Path
import requests
import re
import json

class DocsDownloader:
    """Handles downloading documentation pages and saving them locally."""
    def __init__ (self, output_dir: Path) -> None:
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True);

    def download_pages(self, urls: list[str]) -> list[dict]:
        """Downloads the pages from the given URLs and returns a manifest describing the downloaded files."""
        manifest: list[dict] = []
        for url in urls:
            entry = self.download_page(url)
            manifest.append(entry)
        
        self.write_manifest(manifest)
        return manifest
    
    def download_page(self, url: str) -> dict:
        """downloads a single url and saves it as an HTML file."""
        response = requests.get(
            url,
            timeout=REQUEST_TIMEOUT_SECONDS,
            headers={"User-Agent": USER_AGENT}
        )
        response.raise_for_status()  # Raise an error for bad responses
        filename = self._url_to_filename(url)
        output_path = self.output_dir / filename
        output_path.write_text(response.text, encoding='utf-8') # Save the raw HTML content to a file
        
        return{
            "source_url": url,
            "local_path": str(output_path),
            "status_code": response.status_code
        }
    
    def write_manifest(self, manifest: list[dict]) -> None:
        """Writes the manifest of downloaded files to a JSON file."""
        manifest_path = self.output_dir / "manifest.json"
        manifest_path.write_text(
            json.dumps(manifest, indent=2),
            encoding='utf-8'
        )
    
    @staticmethod
    def _url_to_filename(url: str) -> str:
        """
        Convert a docs URL into a stable local filename.

        Example:
        https://docs.pytorch.org/docs/stable/generated/torch.add.html
        -> generated__torch.add.html
        """
        # Remove the base URL and keep the path
        path = re.sub(r'^https?://[^/]+/', '', url)
        path = re.sub(r'^docs/stable/', '', path)
        # Replace slashes with double underscores
        filename = path.replace('/', '__')
        return filename