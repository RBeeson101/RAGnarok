"""
Wrapper for the local language model used by RAGnarok.

This module provides a clean interface for interacting with the local LLM.

Responsibilities:
- Load or connect to the local model runtime.
- Accept a prompt string and generate a response.
- Hide library-specific details from the rest of the codebase.
- Later, support model settings such as temperature, max tokens, or context size.

This module should isolate all direct interaction with the model backend so that
the rest of the project does not depend on one specific LLM library.
"""