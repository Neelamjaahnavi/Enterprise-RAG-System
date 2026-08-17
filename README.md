# Enterprise-RAG-System
A Retrieval-Augmented Generation (RAG) system built to ingest, chunk, embed, and query dense corporate documents, providing precise, hallucination-free answers using local LLMs.

# Enterprise Document Q&A System (RAG)

An end-to-end, modular Retrieval-Augmented Generation (RAG) architecture built to query enterprise documents without relying on paid external API keys. This system processes corporate text files, generates dense vector embeddings, stores them in ChromaDB, and uses local LLM inference to provide accurate, context-grounded answers.

## Architecture Overview
[ Unstructured Data ] -> [ Chunking ] -> [ HuggingFace Embeddings ]
|
v
[ User Query ] -> [ ChromaDB Vector Search ] -> [ Top Context ] -> [ Local LLM ] -> [ Answer ]

## Features

- **Document Ingestion & Splitting:** Intelligent text chunking using `RecursiveCharacterTextSplitter` to optimize context window performance.
- **Vector Storage:** Persistent local vector database using **ChromaDB**.
- **Local Embeddings:** Free, lightweight embeddings via HuggingFace's `all-MiniLM-L6-v2`.
- **Hallucination Prevention:** Custom system prompt engineering forcing the LLM to reply only with factual data present in the context.
- **Offline Inference:** Local pipeline execution using `google/flan-t5-base`.

## Directory Structure

```text
enterprise-rag-system/
├── data/
│   └── company_policy.txt      # Sample corporate document dataset
├── src/
│   ├── __init__.py             # Package initializer
│   ├── loader.py               # Document loading & text splitting module
│   ├── vectorstore.py          # Vector embedding & ChromaDB management
│   └── rag_chain.py            # LangChain RAG pipeline & LLM setup
├── .gitignore                  # Git ignore file
├── README.md                   # Project documentation
├── main.py                     # Main execution entrypoint
└── requirements.txt            # Python dependencies
```
## Tech Stack

- **Orchestration:** LangChain
- **Vector Store:** ChromaDB
- **Embeddings:** HuggingFace `sentence-transformers` (`all-MiniLM-L6-v2`)
- **LLM Pipeline:** HuggingFace `google/flan-t5-base`
- **Language:** Python 3.10+


Ensure you have Python 3.10 or higher installed.

