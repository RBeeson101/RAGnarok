"""
Main retrieval logic for RAGnarok.

This module is responsible for finding the most relevant documentation chunks
for a user's question.

Responsibilities:
- Accept a user query.
- Pass the query to the embedder.
- Search the vector store using the query embedding.
- Return the top matching chunks, optionally with scores.
- Later, support hybrid retrieval, reranking, metadata filtering, or multi-library search.

This module connects the query to the search system.
It should not handle LLM generation or terminal I/O.
"""