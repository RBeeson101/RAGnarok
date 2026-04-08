from app.cli import run_cli
"""
Main entry point for RAGnarok.

This file is the top-level launcher for the project. It can later be used to
start the application in different modes, such as:
- chat mode
- build/index mode
- test/debug mode

For now, this file can stay very small and simply call the terminal chat flow
or another script entry point.

This file should NOT contain the actual retrieval, parsing, or generation logic.
It should only connect the high-level pieces together and start the program.
"""

def main() -> None:
    run_cli()


if __name__ == "__main__":
    main()