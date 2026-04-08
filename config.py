"""
Central configuration for RAGnarok.

This file stores project-wide settings and paths so they are not hardcoded
throughout the codebase.

Responsibilities:
- Define important filesystem paths, such as where raw docs, processed docs,
  and vector indexes are stored.
- Store PyTorch source URLs or seed URLs for the first small docs subset.
- Hold chunking settings, such as target chunk size and overlap.
- Hold retrieval settings, such as top-k search results.
- Later, store model configuration for the embedder and local LLM.

This file should NOT contain business logic.
It should only define constants, simple settings, and reusable path values.
"""