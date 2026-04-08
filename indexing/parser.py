"""
Documentation parser for RAGnarok.

This module converts raw downloaded documentation into cleaner structured content
that is easier to chunk and index.

Responsibilities:
- Read raw HTML or source files from disk.
- Extract useful text such as titles, headings, paragraphs, and code blocks.
- Remove navigation clutter, repeated page chrome, and irrelevant boilerplate.
- Produce a cleaner document representation for downstream chunking.
- Later, support source-specific parsing rules if needed.

This module should focus on turning messy raw docs into clean structured content.
It should not handle embeddings, retrieval, or LLM generation.
"""