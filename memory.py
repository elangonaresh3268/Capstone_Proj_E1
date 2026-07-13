from langchain_core.vectorstores import InMemoryVectorStore


class Memory:

    def __init__(self):
        self.profile ={}
        self.chat_history =[]
        self.vector_store = None
        self.documents = []

memory=Memory()