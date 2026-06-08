from annotated_types import doc
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()

from uuid import uuid4
from pathlib import Path

project_root = Path.cwd()

print(project_root)

collection_name ="demo"
persist_directory = project_root / "4_vector_stores" /"chroma_langchain_db"

print("collection_name :", collection_name)

print("persist_directory: ", persist_directory)

if(persist_directory.exists()):
    print("Exist file")
else:
    print("NO chroma directory  exist")

embeddings = OllamaEmbeddings(model="embeddinggemma:latest")
 

vector_store = Chroma(
    collection_name=collection_name,
    embedding_function=embeddings,
    persist_directory=str(persist_directory)
)

print("vector store ready")

documents_example = [
    {
        "id": "1",
        "topic": "AI",
        "doc_number": 1,
        "content": "Artificial intelligence helps machines perform tasks that usually need human reasoning."
    },
    {
        "id": "2",
        "topic": "AI",
        "doc_number": 2,
        "content": "AI systems can analyze patterns in data to support predictions and automation."
    },
    {
        "id": "3",
        "topic": "AI",
        "doc_number": 3,
        "content": "Responsible AI development includes fairness, transparency, and safety checks."
    },
    {
        "id": "4",
        "topic": "RAG",
        "doc_number": 4,
        "content": "RAG improves answer quality by retrieving relevant context before the language model generates a response."
    },
    {
        "id": "5",
        "topic": "RAG",
        "doc_number": 5,
        "content": "A retriever in a RAG pipeline finds relevant chunks before the language model generates an answer."
    },
    {
        "id": "6",
        "topic": "RAG",
        "doc_number": 6,
        "content": "Vector stores are important in RAG because they make semantic search over embeddings efficient."
    },
    {
        "id": "7",
        "topic": "LLM",
        "doc_number": 7,
        "content": "LLMs generate text by predicting likely next tokens from patterns learned during training."
    },
    {
        "id": "8",
        "topic": "LLM",
        "doc_number": 8,
        "content": "Well-written prompts help an LLM stay focused, follow instructions, and produce better outputs."
    }
]

documents = [
    Document(
    id=str(uuid4()),
    page_content=item['content'],
    metadata={
        "topic":item['topic'],
        "document_number":item['doc_number']
    }
    )
    for item in documents_example
    ]

# documents_ids = vector_store.add_documents(documents=documents)

# print('documents_ids' , documents_ids)

# for doc_id in documents_ids:
#     print(doc_id)

# print("total inserted documents:" , len(documents_ids))

# get_row_record = vector_store.get()
get_row_record = vector_store.get(include=['embeddings','metadatas', 'documents'])


# print("get_row_record", get_row_record)
# print("IDS", get_row_record['ids'])
# print("IDS", get_row_record['metadatas'])
# print("IDS", get_row_record['embeddings'])
# print("documents :", get_row_record['documents'])

# selected_documents = vector_store.get_by_ids(['82f1279e-f1fe-4a0a-a762-7a9c102ea361'])


# print("selected_documents" , selected_documents)

query = "how does RAG help an LLM answer question using outside knowledge"

search_result = vector_store.similarity_search(query, k=3)

print("search_result" , search_result)

search_with_score = vector_store.asimilarity_search_with_score(query, k=2)
print("search_with_score" , search_with_score)