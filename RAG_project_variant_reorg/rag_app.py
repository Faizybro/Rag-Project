
import os
from langchain.vectorstores import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

STORE_DIR = os.environ.get("STORE_DIR", "vector_store")
EMB_MODEL = os.environ.get("EMB_MODEL", "all-MiniLM-L6-v2")
RAG_MODEL = os.environ.get("RAG_MODEL", "mistral")

def load_store():
    embeddings = SentenceTransformerEmbeddings(model_name=EMB_MODEL)
    return FAISS.load_local(STORE_DIR, embeddings, allow_dangerous_deserialization=True)

def make_chain(vstore):
    llm = Ollama(model=RAG_MODEL)
    retriever = vstore.as_retriever()
    return RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

def interactive_loop(chain):
    print("RAG Q&A — Reorganized Variant")
    print("Type 'exit' to quit.\n")
    while True:
        q = input("You: ").strip()
        if q.lower() in {"exit", "quit"}:
            break
        ans = chain.run(q)
        print(f"Bot: {ans}\n")

def main():
    vstore = load_store()
    chain = make_chain(vstore)
    interactive_loop(chain)

if __name__ == "__main__":
    main()
