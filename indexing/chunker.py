"""
Chunking logic for RAGnarok documentation sources.

This module splits parsed documentation into smaller searchable units called chunks.

Responsibilities:
- Take parsed documents or sections and break them into useful pieces.
- Preserve meaningful structure, such as headings, explanations, and nearby code blocks.
- Avoid splitting important context unnecessarily.
- Attach metadata to each chunk, such as page title, section title, and source URL.
- Later, support chunk size and overlap settings from config.

This module is important because chunk quality strongly affects retrieval quality.
It should focus on producing chunks that are both searchable and informative.
"""