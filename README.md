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


## Getting Started
## Prerequisites
- Ensure you have Python 3.10 or higher installed.

## Installation
Clone the repository:

```Bash
git clone [https://github.com/Neelamjaahnavi/enterprise-rag-system.git](https://github.com/Neelamjaahnavi/enterprise-rag-system.git)
cd enterprise-rag-system
```
Install dependencies:

```Bash
pip install -r requirements.txt
```

## Running the Pipeline
Run the main execution script to build the vector store and run a sample query:

```Bash
python main.py
```
## Example Output
Plaintext
- [+] Loading and chunking document...
- [+] Building vector store with ChromaDB...
- [+] Initializing RAG Pipeline...

- [?] Query: What is the equipment reimbursement limit?

- [=] Response:
Expenses for ergonomic office furniture and peripheral hardware are capped at $500 per calendar year.

## License

Distributed under the MIT License.
