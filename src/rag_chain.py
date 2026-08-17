
from langchain_community.llms import HuggingFacePipeline
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

def setup_rag_chain(retriever):
    """Initializes the prompt template, LLM, and retrieval chain."""
    system_prompt = (
        "You are an enterprise AI assistant for document retrieval. "
        "Use the following pieces of retrieved context to answer the question accurately. "
        "If the answer is not present in the context, respond with 'Information not found in context.'\n\n"
        "Context:\n{context}"
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    llm = HuggingFacePipeline.from_model_id(
        model_id="google/flan-t5-base",
        task="text2text-generation",
        pipeline_kwargs={"max_new_tokens": 150}
    )

    document_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(retriever, document_chain)
