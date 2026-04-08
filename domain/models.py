"""
Core data models used throughout RAGnarok.

This module defines the main structured objects passed between parts of the system.

Examples of models that belong here:
- Document: a parsed documentation page or source file
- Chunk: a smaller searchable piece of a document
- RetrievedChunk: a chunk plus retrieval score or rank information
- AnswerResult: the final assistant response plus optional sources

Responsibilities:
- Provide clean, reusable representations of the data in the pipeline.
- Make it easier for modules to communicate using structured objects instead
  of loose dictionaries.
- Keep the shape of the data consistent across indexing, retrieval, and generation.

This module should not contain heavy processing logic.
It should mainly define dataclasses or simple containers.
"""