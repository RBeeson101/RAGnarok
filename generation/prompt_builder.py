"""
Prompt construction for RAGnarok.

This module is responsible for building the input that will be sent to the LLM.

Responsibilities:
- Combine the user's question with the retrieved documentation chunks.
- Add system instructions that tell the model how to behave.
- Keep the prompt grounded in the retrieved context.
- Encourage useful answers, examples, and honest uncertainty when needed.
- Later, support different prompt templates for different question types.

This module should not call the model directly.
Its job is only to prepare the text input for generation.
"""