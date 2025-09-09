
import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS

DATA_DIR = os.environ.get("DATA_DIR", "data")
STORE_DIR = os.environ.get("STORE_DIR", "vector_store")
EMB_MODEL = os.environ.get("EMB_MODEL", "all-MiniLM-L6-v2")

def collect_pdfs(folder: str):
    for name in os.listdir(folder):
        if name.lower().endswith(".pdf"):
            yield os.path.join(folder, name)

def load_documents(pdf_paths):
    docs = []
    for p in pdf_paths:
        loader = PyPDFLoader(p)
        docs.extend(loader.load())
    return docs

def chunk_documents(documents, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)

def build_and_save_index(splits, store_path):
    embeddings = SentenceTransformerEmbeddings(model_name=EMB_MODEL)
    vect = FAISS.from_documents(splits, embeddings)
    os.makedirs(store_path, exist_ok=True)
    vect.save_local(store_path)

def main():
    pdfs = list(collect_pdfs(DATA_DIR))
    if not pdfs:
        raise SystemExit(f"No PDFs found in {DATA_DIR}.")
    docs = load_documents(pdfs)
    splits = chunk_documents(docs)
    build_and_save_index(splits, STORE_DIR)
    print(f"✅ Index built and saved to '{STORE_DIR}'")

if __name__ == "__main__":
    main()
