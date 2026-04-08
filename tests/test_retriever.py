"""
Tests for the retrieval pipeline.

This module checks that queries can be embedded, searched against the vector store,
and mapped back to the expected documentation chunks.

Things to test:
- retrieval returns results in the expected format
- top results are relevant for simple sample queries
- vector store integration works correctly
- missing or empty queries are handled safely
- later, hybrid retrieval and reranking behavior

These tests help confirm that the assistant is finding the right context before
generation happens.
"""