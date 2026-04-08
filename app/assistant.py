"""
High-level assistant coordinator for RAGnarok.

This module is responsible for the main runtime flow of the documentation
assistant. It sits above retrieval and generation and coordinates the pieces.

Responsibilities:
- Accept a user question from the CLI or another interface.
- Send the question to the retriever to get the most relevant documentation chunks.
- Pass the question and retrieved chunks to the prompt builder / answer generator.
- Return the final answer in a clean format.
- Later, possibly manage short conversation state for follow-up questions.

This module should not directly parse raw HTML, build indexes, or manage low-level
vector math. Its job is orchestration: connect the main components together.
"""