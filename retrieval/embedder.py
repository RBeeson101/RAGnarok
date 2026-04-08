"""
Embedding interface and implementation wrapper for RAGnarok.

This module is responsible for converting text into vector embeddings.

Responsibilities:
- Embed documentation chunks during index-building time.
- Embed user queries during runtime.
- Hide the specific embedding library behind a clean interface.
- Ensure that documents and queries are embedded in a consistent way.
- Later, allow easy replacement of the pretrained embedder with a custom model.

This module should only deal with text-to-vector conversion.
It should not store vectors or perform retrieval by itself.
"""