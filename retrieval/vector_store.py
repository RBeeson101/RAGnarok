"""
Vector storage and similarity search for RAGnarok.

This module manages the storage and lookup of embeddings for documentation chunks.

Responsibilities:
- Store chunk embeddings and associated identifiers.
- Save and load the vector index from disk.
- Perform nearest-neighbor or similarity search for query embeddings.
- Return matching chunk identifiers and search scores.
- Later, support different vector backends if needed.

This module should focus only on vector indexing and similarity search.
It should not know how prompts are built or how answers are generated.
"""