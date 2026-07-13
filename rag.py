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

def load_document(file_path:str):
    suffix=Path(file_path).suffix.lower()
    if suffix==".pdf":
        loader=PyPDFLoader(file_path)
    elif suffix==".docx":
        loader=Docx2txtLoader(file_path)
    elif suffix ==".txt":
        loader=TextLoader(file_path)
    else:
        raise Exception("Unsupported file type")
    
    return loader.load()


def build_vector_store(file_path:str):
    documents=load_document(file_path)
    splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    chunks=splitter.split_documents(documents)
    vector_store=InMemoryVectorStore(embedding=embedding_model)
    vector_store.add_documents(chunks)
    memory.vector_store=vector_store
    memory.documents=chunks
    return len(chunks)


def retrieve(question:str,k:int=4):
    if memory.vector_store is None:
        return []
    
    docs=memory.vector_store.similarity_search(question,k=k)
    return docs


def get_context(question:str):
    docs=retrieve(question)
    context="\n]\n".join(
        doc.page_content
        for doc in docs
    )

    return context