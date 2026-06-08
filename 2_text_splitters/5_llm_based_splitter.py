# What is it?
# LLM-based chunking uses a language model to intelligently determine 
# where to split text based on semantic understanding. The LLM 
# analyzes the document and decides optimal chunk boundaries, 
# potentially generating summaries or extracting key information.
# This is like having an intelligent editor who understands the content 
# and knows exactly where topics begin and end.

# Advantages:
# • Most intelligent and context-aware splitting
# • Can add contextual summaries to chunks
# • Understands semantic boundaries better than rules
# • Can adapt to different document types
# • Improves retrieval quality significantly
# • Can extract key information

# Disadvantages:
# • Very expensive (LLM API calls for every chunk)
# • Slowest processing time
# • Requires API access and costs money
# • Not deterministic (results may vary)
# • Overkill for simple documents
# • Latency issues for large documents
# • Complex to implement and maintain

from langchain_openai import OpenAIEmbeddings
from pydantic import BaseModel
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


text = """Artificial intelligence is transforming technology and shaping the future.
Machine learning algorithms are becoming more sophisticated every day.
Deep learning models can now process vast amounts of data efficiently.
Neural networks are inspired by the human brain's structure.
The best pasta recipes include fresh ingredients and proper cooking techniques.
Italian cuisine emphasizes quality olive oil and regional cheeses.
Authentic carbonara uses guanciale, eggs, pecorino romano, and black pepper.
Cooking pasta al dente ensures the best texture and flavor.
Climate change is affecting ecosystems worldwide.
Rising temperatures are causing glaciers to melt at unprecedented rates.
Scientists warn that immediate action is needed to reduce carbon emissions.
Renewable energy sources offer hope for a sustainable future."""

class Chunk(BaseModel):
    text: str
    summary: str

class Chunker(BaseModel):
    chunks: list[Chunk]

model = ChatOpenAI(model='gpt-5-mini')


llm_chunker = model.with_structured_output(schema=Chunker)

prompt = ChatPromptTemplate(
    messages=[
    ("system", 
     """You are an expert Text Chunker that splits the given text and outputs them as a 
     list of strings. You understand the natural topic boundaries of text and 
     also do not change the existing text. You just split the text where ever applicable.
     Once you create the chunk, you also generate a 1-2 line summary of the chunk also"""),
     
    ("human","Split the given text into chunks\nText: {text}"),
],
input_variables=["text"]
)

model_chain = prompt | llm_chunker


response = model_chain.invoke({"text": text})

print(response)