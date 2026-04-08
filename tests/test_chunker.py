"""
Tests for the documentation chunking logic.

This module verifies that parsed documents are split into useful chunks correctly.

Things to test:
- headings and related text stay together when appropriate
- code examples are preserved
- chunk metadata is assigned correctly
- very small or empty chunks are handled properly
- chunk boundaries behave as expected

These tests help ensure that poor chunking does not silently reduce retrieval quality.
"""