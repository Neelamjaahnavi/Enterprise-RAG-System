
import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def build_or_load_vectorstore(chunks, persist_dir: str = "./chroma_db"):
    """Generates embeddings and stores them in a local ChromaDB instance."""
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    if os.path.exists(persist_dir) and len(os.listdir(persist_dir)) > 0:
        vectorstore = Chroma(
            persist_directory=persist_dir,
            embedding_function=embedding_model
        )
    else:
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embedding_model,
            persist_directory=persist_dir
        )
    return vectorstore
