from langchain_ollama import ChatOllama 
from dotenv import load_dotenv
load_dotenv()
import os

llm = ChatOllama(
    base_url=os.getenv("OLLAMA_BASE_URL"),
    model=os.getenv("OLLAMA_MODEL_NAME"),
)

response = llm.invoke("who is the current pm of india")

print(response)

