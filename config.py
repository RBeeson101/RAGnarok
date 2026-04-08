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
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent # Assumes config.py is at the root of the project

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw" / "pytorch"
PROCESSED_DIR = DATA_DIR / "processed" / "pytorch"
INDEX_DIR = DATA_DIR / "indexes" / "pytorch"

# PyTorch source URLs for the first small docs subset
PYTORCH_URLS = [
    "https://docs.pytorch.org/docs/stable/index.html",
    "https://docs.pytorch.org/docs/stable/torch.html",
    "https://docs.pytorch.org/docs/stable/tensors.html",
    "https://docs.pytorch.org/docs/stable/generated/torch.add.html",
    "https://docs.pytorch.org/docs/stable/generated/torch.Tensor.add.html",
]

# Chunking settings
CHUNK_TARGET_WORDS = 250
CHUNK_MIN_WORDS = 120
CHUNK_MAX_WORDS = 400
CHUNK_OVERLAP_WORDS = 40

#retrieval settings
TOP_K_Results = 5


# Downloader settings.
REQUEST_TIMEOUT_SECONDS = 20
USER_AGENT = "RAGnarok/0.1 (offline-doc-assistant)"

# Embedder and local LLM settings will be added here later as needed.


