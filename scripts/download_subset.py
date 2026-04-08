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