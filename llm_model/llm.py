from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

load_dotenv()
import os


ollama= ChatOllama(base_url=os.getenv('OLLAMA_BASE_URL'), model=os.getenv('OLLAMA_MODEL_NAME'))
open_ai = ChatOpenAI()

def use_llm():

    LLM_USED = os.getenv('LLM_USED')

    if(LLM_USED=='OLLAMA'):
        return ollama
    else:
        open_ai

llms= use_llm