"""
Terminal interface for RAGnarok.

This module handles the interactive command-line loop for v1.

Responsibilities:
- Display a prompt to the user.
- Read user input from the terminal.
- Pass the question to the assistant coordinator.
- Print the final response cleanly.
- Repeat until the user exits.
- Later, optionally support commands like 'quit', 'help', or 'sources'.

This module should only handle terminal interaction and presentation.
It should not contain retrieval logic, prompt construction, or model code.
"""