"""LLM helpers for invoking the local Ollama-backed LLM.

This module wraps the `ChatOllama` client and exposes a simple
`ask_llama(context, question)` helper used by the Streamlit app.
"""

from langchain_community.chat_models import ChatOllama
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOllama(
    model=os.getenv("LLAMA_MODEL"),
    temperature=0.2
)


def ask_llama(context: str, question: str) -> str:
    """Send a prompt to the LLM that includes the provided context.

    The function builds a constrained prompt that instructs the model
    to answer using only the supplied context. Returns the raw text
    content of the model response.
    """
    prompt = f"""
    You are an Insurance Advisor :
    Answer only using the provided context.
    Context:
    {context}
    Question:
    {question}
    """

    response = llm.invoke(prompt)
    return response.content