from annotated_types import doc
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from pathlib import Path
import os
load_dotenv()

project_root =Path.cwd()

pdf_path =project_root /'4_vector_stores'/'beyond-chatbots-ai-agents-next-real-shift.pdf'

collection_name ="rag_pipline"
persist_directory = project_root / "4_vector_stores" /"chroma_langchain_db"

print("pdf_path" , pdf_path)
print("collection_name" , collection_name)
print("persist_directory" , persist_directory)

documents_loader = PyPDFLoader(file_path=str(pdf_path))

documents = documents_loader.load()

print('Length of documents :' , len(documents))
# print('first documents :' , documents[0])
# print('first page content :' , documents[0].page_content)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks_documents = text_splitter.split_documents(documents)

# print("Total chunks created :", len(chunks_documents))
# print("First chunks :" , chunks_documents[0])
# print("First chunks :" , chunks_documents[1])

embedding = OllamaEmbeddings(model="embeddinggemma:latest")

# vector_store = Chroma.from_documents(
#     embedding=embedding,
#     collection_name=collection_name,
#     persist_directory=persist_directory,
#     documents=chunks_documents
# )

vector_store = Chroma(
    collection_name=collection_name,
    embedding_function=embedding,
    persist_directory=persist_directory
)

def print_documents(title, docs):
    """Print retrieved documents using page metadata and a text preview."""
    print(title)
    for index, doc in enumerate(docs, start=1):
        print(f"{index}. page={doc.metadata.get('page')} | source={doc.metadata.get('source')}")
        print(f"   content={doc.page_content}")
    print()

query = "How do AI agents use tools and memory"

# results = vector_store.similarity_search(query=query, k=3)
results = vector_store.similarity_search_with_score(query, k=5)

for doc, score in results:
    print('score: ', score)
    print("content:", doc.page_content)

# print("length of retrived documents: ", print_documents(query, results))
# print("length of retrived documents: ", results[1].page_content)
# print("length of retrived 1st documents: ", results[0])
# print("length of retrived 2nd documents: ", results[1])

# for doc in results:
#     # print('score', score)
#     print("retrive doc", doc)
#     print("===="*50 +"\n")

 
