"""rag.py

Utilities for loading documents, building an in-memory vector store
and retrieving contextual text for a user question. This module is
used by the Streamlit app to implement a simple RAG (retrieval-augmented
generation) workflow.

Functions:
- load_document(file_path): load text from PDF/DOCX/TXT
- build_vector_store(file_path): split and store embeddings in memory
- retrieve(question): perform similarity search against the in-memory store
- get_context(question): return joined page content for the top documents
"""

from pathlib import Path
from langchain_community.document_loaders import (PyPDFLoader,TextLoader,Docx2txtLoader)

from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_core.vectorstores import InMemoryVectorStore 
from dotenv import load_dotenv
from langchain_community.embeddings import OllamaEmbeddings
import os
from memory import memory

load_dotenv()

embedding_model=OllamaEmbeddings(model=os.getenv("EMBEDDING_MODEL"))

def load_document(file_path: str):
    """Load a document from disk and return LangChain document objects.

    Supports PDF, DOCX and TXT based on file suffix. Raises an
    Exception for unsupported types.
    """
    suffix = Path(file_path).suffix.lower()
    if suffix == ".pdf":
        loader = PyPDFLoader(file_path)
    elif suffix == ".docx":
        loader = Docx2txtLoader(file_path)
    elif suffix == ".txt":
        loader = TextLoader(file_path)
    else:
        raise Exception("Unsupported file type")

    return loader.load()


def build_vector_store(file_path: str):
    """Create an in-memory vector store from a document file.

    Splits the document into chunks, computes embeddings and stores them
    in `memory.vector_store`. Returns the number of chunks created.
    """
    documents = load_document(file_path)
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(documents)
    vector_store = InMemoryVectorStore(embedding=embedding_model)
    vector_store.add_documents(chunks)
    memory.vector_store = vector_store
    memory.documents = chunks
    return len(chunks)


def retrieve(question: str, k: int = 4):
    """Return the top-k similar document chunks for a question.

    If no vector store exists yet, returns an empty list.
    """
    if memory.vector_store is None:
        return []

    docs = memory.vector_store.similarity_search(question, k=k)
    return docs


def get_context(question: str):
    """Build a simple textual context by joining retrieved chunks.

    Returns a single string suitable for inclusion in prompts sent to
    the LLM.
    """
    docs = retrieve(question)
    context = "\n]\n".join(
        doc.page_content
        for doc in docs
    )

    return context