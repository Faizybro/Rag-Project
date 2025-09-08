# 📚 RAG Project — Reorganized Variant

This project is a **Retrieval-Augmented Generation (RAG) system** that allows you to ask questions from your own PDF documents.  
It uses **LangChain**, **FAISS**, and **Ollama** (local LLMs such  Llama 2) to provide answers grounded in your data.

---

## ✨ Features
- **PDF Ingestion** → load and process multiple PDF files.  
- **Vector Store** → FAISS for fast similarity search.  
- **Local LLM** → query with Ollama models (`mistral`, `llama2`, etc.).  
- **Interactive CLI** → ask questions and get answers with citations.

---

## 📂 Project Structure
```
RAG_project_variant_reorg/
├── build_index.py        # build FAISS index from PDFs
├── rag_app.py            # Q&A CLI app
├── requirements.txt      # Python dependencies
├── readme.md             # this file
├── data/                 # put your PDFs here
└── vector_store/         # FAISS index (auto-created)
```

---

## ⚙️ Installation

> 💡 Recommended: Use **Python 3.11** (best compatibility with LangChain + FAISS).  

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/RAG_project_variant_reorg.git
   cd RAG_project_variant_reorg
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    # on Linux/Mac
   venv\Scripts\activate       # on Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install and set up **Ollama**:
   - [Download Ollama](https://ollama.ai)
   - Run Ollama in the background:
     ```bash
     ollama serve
     ```
   - Pull a model (example: mistral):
     ```bash
     ollama pull mistral
     ```

---

## 🚀 Usage

### Step 1: Add your PDFs
Place your `.pdf` files inside the `data/` folder.

### Step 2: Build the index
```bash
python build_index.py
```

This will create the FAISS vector store inside `vector_store/`.

### Step 3: Run the app
```bash
python rag_app.py
```

You can now ask questions interactively:
```
You: What is inside city.pdf?
Bot: <answer>
```

Type `exit` to quit.

---

## ⚡ Environment Variables (Optional)
You can override defaults by setting environment variables:

| Variable     | Default                 | Description |
|--------------|-------------------------|-------------|
| `RAG_MODEL`  | `mistral`               | Ollama LLM model |
| `EMB_MODEL`  | `all-MiniLM-L6-v2`      | Embedding model |
| `STORE_DIR`  | `vector_store`          | Vector store directory |

Example:
```bash
RAG_MODEL=llama2 python rag_app.py
```

---

## 📌 Example
```bash
You: Summarize the Project Proposal.
Bot: The document outlines...
```

---

## 🛠️ Troubleshooting
- If `faiss-cpu` fails to install:
  - Use **Python 3.11**.
  - Or pre-install NumPy first:
    ```bash
    pip install numpy==1.26.4
    pip install -r requirements.txt
    ```
- Ensure **Ollama** is installed and a model (e.g. `mistral`) is pulled.
- Run from inside the project folder.

---

## 📜 License
This project is open-source under the MIT License.  
Feel free to use, modify, and share.

---
