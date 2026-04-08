"""
Abstract interfaces for replaceable components in RAGnarok.

This module defines the contracts that important system components must follow.

Examples:
- BaseEmbedder
- BaseRetriever
- BaseVectorStore
- BaseLLMClient

Responsibilities:
- Make the architecture modular and easy to swap out later.
- Allow v1 to use pretrained tools while keeping the system ready for custom
  models or improved implementations later.
- Reduce coupling between high-level application logic and third-party libraries.

This module should define abstract base classes and method signatures,
not concrete implementations.
"""