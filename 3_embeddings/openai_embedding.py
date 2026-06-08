from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

import os
load_dotenv()

openai_small_embedding = OpenAIEmbeddings(model= "text-embedding-3-small")
openai_large_embedding = OpenAIEmbeddings(model= "text-embedding-3-large")

query = "What is Gen AI?"

# embedding_large = openai_large_embedding.embed_query(query)

# embedding_small = openai_small_embedding.embed_query(query)




# print("large embedding length: " , len(embedding_large))
# print("small embedding length: " , len(embedding_small))

loaders = PyPDFLoader(file_path = "./Openclaw_Research_Report.pdf", mode ="page")

documents = loaders.load()

print("Total Documents: ", len(documents))

chunker = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)

chunks = chunker.split_documents(documents)

print("Total Chunks: " , len(chunks))

text_documents = [doc.page_content for doc in chunks]

print("Total text documents: " , len(text_documents))

documents_with_large_embedding = openai_large_embedding.embed_documents(text_documents)

print("Length of documents with large embedding: " , len(documents_with_large_embedding))
print(documents_with_large_embedding[0:3])