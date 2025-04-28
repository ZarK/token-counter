#!/usr/bin/env python3
"""
ap.py – local ChatGPT-style token counter with a simple UI
-----------------------------------------------------------------------
1. Install deps   :  pip install streamlit tiktoken
2. Run locally    :  streamlit run token_counter_ui.py
"""

import streamlit as st

try:
    import tiktoken
except ImportError:
    st.error("Missing dependency: run  pip install tiktoken")
    st.stop()

# ---------- UI ----------
st.set_page_config(page_title="Token Counter", layout="wide")
st.title("🔢 ChatGPT Token Counter (local)")

# Moved model selection here
model = st.selectbox(
    "Select Model (determines tokenization):",
    ["gpt-3.5-turbo", "gpt-4o-mini", "gpt-4o", "davinci-002", "text-embedding-3-small"],
    index=0,
)

# Main input area – tuned for ~200 k tokens (~800 k characters)
text = st.text_area(
    "Paste or type your text (supports very large inputs):",
    height=500,
    placeholder="Drop up to ~200 000 ChatGPT tokens of text here…",
)

uploaded = st.file_uploader("…or upload a .txt file", type=["txt"])
if uploaded:
    text = uploaded.read().decode("utf-8")
    st.success(f"Loaded {len(text):,} characters from {uploaded.name}")

# ---------- Logic ----------
def count_tokens(text: str, model_name: str) -> int:
    """Counts tokens using the encoding for the specified model."""
    try:
        enc = tiktoken.encoding_for_model(model_name)
        return len(enc.encode(text))
    except Exception as e:
        st.error(f"Error getting encoding for model '{model_name}': {e}")
        st.stop()

if st.button("Count tokens") or (text and not uploaded):
    # Pass the selected model name to count_tokens
    n = count_tokens(text, model)
    st.metric(label="Token count", value=f"{n:,}")
    st.caption(f"≈ {n/1000:.1f} k tokens (using '{model}' encoding)")

st.caption("⚡️ Runs entirely on your machine—no API calls, no data leaves your box.")
