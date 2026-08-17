from src.loader import load_and_chunk_document
from src.vectorstore import build_or_load_vectorstore
from src.rag_chain import setup_rag_chain

def main():
    data_path = "data/company_policy.txt"

    print("[+] Loading and chunking document...")
    chunks = load_and_chunk_document(data_path)

    print("[+] Building vector store with ChromaDB...")
    vectorstore = build_or_load_vectorstore(chunks)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    print("[+] Initializing RAG Pipeline...")
    rag_chain = setup_rag_chain(retriever)

    query = "What is the equipment reimbursement limit?"
    print(f"\n[?] Query: {query}")

    response = rag_chain.invoke({"input": query})
    print("\n[=] Response:")
    print(response["answer"])

if __name__ == "__main__":
    main()
