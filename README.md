# RAGnarok

An offline RAG-based documentation assistant for software libraries.

RAGnarok lets users ask natural-language questions about a library offline, and retrieves the most relevant documentation chunks, and generates answers using a fully local language model.
The long-term goal is to build a handheld, offline documentation companion that can run on embedded hardware such as a Raspberry Pi with a screen, battery pack, and voice input.

## Overview

When developers learn a library, they often need more than keyword search. They want to ask things like:

- What does this do?
- How do I do this?
- How does this work?
- What can I use this for?

RAGnarok is designed to answer those kinds of questions by combining local retrieval with local generation. Instead of depending on cloud APIs or internet access,
the system works entirely offline using a local snapshot of documentation and locally hosted models.

The first version focuses on a single library: **PyTorch**.

## Goals

Build pipeline:
raw docs -> parsed docs -> chunks -> chunk embeddings -> saved index

Query pipeline:
user question -> query embedding -> similarity search -> top chunks -> query + chunks -> LLM -> response

- Run fully offline
- Answer natural-language questions about a software library
- Retrieve relevant documentation chunks before generating a response
- Start simple with pretrained components
- Gradually replace pretrained parts with models I train or fine-tune myself
- Eventually support embedded deployment on a Raspberry Pi
- Expand from one library to multiple libraries over time

## V1 Scope

Version 1 includes:

- Offline execution
- Terminal-only interface
- Support for one library only: **PyTorch**
- A local snapshot of documentation
- Retrieval + answer generation
- A pretrained embedding model
- A local LLM

Version 1 does **not** include:

- Voice input
- GUI
- Multi-library support
- Custom-trained retrieval or generation models

## How It Works

At a high level, RAGnarok follows a standard Retrieval-Augmented Generation pipeline:

1. A user asks a question in natural language.
2. The system embeds the question.
3. The retriever searches a local index of documentation chunks.
4. The most relevant chunks are selected.
5. A local language model generates an answer using the retrieved context.
6. The answer is returned in the terminal.

This makes the system more grounded in the documentation and more useful than raw keyword search alone.

## Why This Project

This project is meant to explore:

- Offline AI systems
- Documentation retrieval
- Local language model inference
- Practical RAG system design
- Long-term model replacement and improvement
- Edge deployment constraints

It also serves as a stepping stone toward an easily portable assistant for developers who want reliable answers without needing internet access.

## Planned Architecture

### Documentation Ingestion
- Collect a local snapshot of PyTorch documentation
- Parse and clean the docs
- Split content into chunks
- Store chunk metadata for retrieval

### Retrieval
- Use a pretrained embedder to generate vector representations
- Store embeddings in a local vector index
- Retrieve the most relevant chunks for each query

### Generation
- Run a local LLM
- Feed retrieved chunks into the model as context
- Generate answers grounded in the docs

### Interface
- Terminal-based Command Line Interface for V1
- Simple question/answer interaction loop
- Minimal setup and local execution

## Roadmap

### V1
- Single-library support
- PyTorch only
- Local documentation snapshot
- Offline retrieval and generation
- Terminal interface

### V2
- Better chunking and ranking
- Source citations or linked chunks
- Improved prompting
- Faster local inference
- Cleaner CLI workflow

### V3
- Multi-library support
- Library selection and routing
- Better indexing strategy
- More robust local packaging

### Long-Term
- Replace pretrained components with self-trained or fine-tuned models
- Optimize for edge hardware
- Deploy on Raspberry Pi
- Add screen, battery pack, and voice input
- Build a handheld offline documentation assistant

## Example Questions

- What does `torch.nn.Module` do?
- How do I create a tensor in PyTorch?
- How does autograd work?
- What can I use DataLoader for?
- When should I use `torch.no_grad()`?

## Current Constraints

RAGnarok is intentionally narrow in its first version.

Current limitations:
- Only works with one library
- Depends on a local snapshot rather than live docs
- Uses pretrained models
- Runs in the terminal only
- Does not yet support speech or a visual interface

These constraints keep the initial build manageable while leaving room for later expansion.

## Future Improvements

- Better ingestion pipeline for documentation
- Smarter chunking and retrieval
- Response grounding and citation support
- Custom fine-tuned embedding model
- Custom fine-tuned local LLM
- Multi-library retrieval
- Embedded deployment optimizations
- Voice-driven interaction

## Status

Early-stage project.  
Currently focused on building the first offline terminal-based prototype for PyTorch documentation.

## License

This project is licensed under the MIT License. See the "LICENSE" file for details.