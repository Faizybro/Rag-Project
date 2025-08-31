# My RAG Project: PDF Q&A System

This project demonstrates a simple Retrieval-Augmented Generation (RAG) system using LangChain to answer questions based on a set of local PDF documents. The project uses a local open-source LLM via Ollama.

## Features
- **Document Ingestion**: Processes and embeds local PDF files.
- **Efficient Retrieval**: Uses a vector store (FAISS) for fast and relevant document retrieval.
- **Local LLM**: Utilizes a local LLM (e.g., Llama 2 via Ollama) to generate answers.

## Prerequisites
- Python 3.8+
- Git
- Docker (or a direct Ollama installation)

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your_repository_url>
    cd <your_repository_name>
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Install Ollama and pull a model:**
    - Follow the installation guide on the [Ollama website](https://ollama.ai/).
    - Pull a model, for example, `llama2`:
      ```bash
      ollama pull llama2
      ```

4.  **Place your documents:**
    - Add your PDF files to the `data/` directory.

## Usage

1.  **Run the ingestion script:**
    - This will process your PDFs and create the vector store.
    ```bash
    python scripts/ingest_data.py
    ```

2.  **Start the main application:**
    ```bash
    python main.py
    ```
    - The application will prompt you to ask a question.

## Project Structure
- `data/`: Stores the PDF documents.
- `scripts/`: Contains the data ingestion script.
- `main.py`: The core application file for the Q&A system.
- `requirements.txt`: Lists all Python dependencies.
- `README.md`: This file.