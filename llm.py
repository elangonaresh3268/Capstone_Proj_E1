from langchain_community.chat_models import ChatOllama
from dotenv import load_dotenv
import os

load_dotenv()

llm=ChatOllama(
    model=os.getenv("LLAMA_MODEL"),
    temperature=0.2
)


def ask_llama(context,question):
    prompt=f"""
    You are an Insurance Advisor :
    Answer only using the provided context.
    Context:
    {context}
    Question:
    {question}
    """

    response=llm.invoke(prompt)
    return response.content