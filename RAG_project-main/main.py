from langchain.llms import Ollama
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

# Define the paths
vector_db_path = 'faiss_index'

# Load the embeddings and vector store
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = FAISS.load_local(vector_db_path, embeddings, allow_dangerous_deserialization=True)

# Set up the LLM
ollama_llm = Ollama(model="llama2")

# Create the RAG chain
qa_chain = RetrievalQA.from_chain_type(
    llm=ollama_llm,
    chain_type="stuff",
    retriever=vector_store.as_retriever(),
    return_source_documents=True
)

# Main loop for Q&A
print("Ready to answer questions. Type 'exit' to quit.")
while True:
    query = input("Enter your question: ")
    if query.lower() == 'exit':
        break
    
    result = qa_chain({"query": query})
    print("\n--- Answer ---")
    print(result['result'])
    print("\n--- Sources ---")
    for doc in result['source_documents']:
        print(f"Source: {doc.metadata['source']}")