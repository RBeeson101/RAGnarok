"""
Build script for the PyTorch documentation index used by RAGnarok.

This script runs the end-to-end build pipeline for v1.

Responsibilities:
- Download or load the local PyTorch docs subset.
- Parse the raw documentation files.
- Chunk the parsed content.
- Generate embeddings for the chunks.
- Build and save the vector index and chunk metadata.

This script is intended to be run manually during development whenever the
knowledge base needs to be rebuilt.
"""