# Token Counter UI

A simple, local Streamlit application to count tokens for various OpenAI models using the `tiktoken` library. It accepts text input via a text area or file upload.

Users select the desired OpenAI model name (e.g., `gpt-4o`, `gpt-3.5-turbo`) via a dropdown in the main UI, which determines the tokenization used.

- **Framework**: Streamlit
- **Core Logic**: `tiktoken`
- **Environment**: Python `.venv` managed with `uv`
