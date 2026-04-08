"""
Index-building pipeline for RAGnarok.

This module coordinates the full offline preparation process for the documentation
knowledge base.

Responsibilities:
- Load raw documentation files from disk.
- Parse them into structured text.
- Split them into chunks.
- Generate embeddings for those chunks.
- Save chunk metadata and vector data into persistent storage.
- Build the local search index used during query time.

This is a build-time module, not a query-time module.
It prepares the knowledge base ahead of time so the runtime assistant can stay fast
and fully offline.
"""