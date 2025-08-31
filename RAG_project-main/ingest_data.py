import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS

# Define the paths
data_path = 'data'
vector_db_path = 'faiss_index'

# Load the documents
documents = []
for file in os.listdir(data_path):
    if file.endswith('.pdf'):
        loader = PyPDFLoader(os.path.join(data_path, file))
        documents.extend(loader.load())

# Split the documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

# Create embeddings
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Create a FAISS vector store
vector_store = FAISS.from_documents(chunks, embeddings)

# Save the vector store
vector_store.save_local(vector_db_path)

print("Vector store created successfully!")
print(f"Number of document chunks: {len(chunks)}")