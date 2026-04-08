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
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Document:
  """Represents a parsed documentation page or source file."""
  doc_id: str  
  title: str
  source_url: str
  raw_text: str
  local_path: Optional[str] = None

@dataclass
class Chunk:
  """Represents a smaller searchable piece of a document."""
  chunk_id: str 
  doc_id: str  
  title: str
  section_title: Optional[str] = None
  text: str
  source_url: str
  word_count: int = 0

  @dataclass
  class RetrievedChunk:
    """Represents a chunk that was retrieved during search, with score info."""
    chunk: Chunk
    score: float  # Similarity score from the vector search
    rank: int  # Rank position in the search results
  
  @dataclass
  class AnswerResult:
    """Represents the final assistant response, including sources."""
    answer_text: str
    source_chunks: list[RetrievedChunk] = field(default_factory=list)