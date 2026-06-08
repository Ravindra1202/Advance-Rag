import ollama

from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

text = "Artificial intelligence is transforming technology and shaping the future."

embedding_query = ollama.embed(
    # base_url="http://localhost:11434",
    model="embeddinggemma:latest",
    input=text,
    # dimensions=512 #by default 768
    )

print("Length of Embedding query: ", len(embedding_query["embeddings"]))
print("Embedding query: ", embedding_query["embeddings"])
print("Embedding query: ", len(embedding_query["embeddings"][0]))


loaders = PyPDFLoader(file_path = "./Openclaw_Research_Report.pdf", mode ="page")

documents = loaders.load()

print("Total Documents: ", len(documents))

chunker = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)

chunks = chunker.split_documents(documents)

print("Total Chunks: " , len(chunks))

text_documents = [doc.page_content for doc in chunks]
print("Total text documents: " , len(text_documents))

embedding_documents = ollama.embed(
    input=text_documents,
    model="embeddinggemma:latest",
)

print("embedding_documents", len(embedding_documents['embeddings']))


