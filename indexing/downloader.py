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