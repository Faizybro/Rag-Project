# RAG Project — Reorganized Variant

This variant preserves the original functionality but **renames** files, **tweaks** structure, and **refactors** variable/function names so it looks different while behaving the same.

## New structure

```
RAG_project_variant_reorg/
├─ build_index.py         # replaces ingest_data.py
├─ rag_app.py             # replaces main.py
├─ requirements.txt
├─ data/                  # your PDFs
└─ vector_store/          # FAISS index (index.faiss + index.pkl after building)
```

## Quickstart

1. Create a virtual environment and install requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Build the FAISS index from PDFs in `./data`:
   ```bash
   python build_index.py
   ```

3. Run the QA app (requires an Ollama model like `mistral` or `llama3` to be available locally):
   ```bash
   python rag_app.py
   ```

### Environment variables (optional)

- `RAG_MODEL` — Chat model name for Ollama (default: `mistral`).
- `EMB_MODEL` — SentenceTransformer embedding model (default: `all-MiniLM-L6-v2`).
- `STORE_DIR` — Vector store directory (default: `vector_store`).
