import ollama

from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

text = "Artificial intelligence is transforming technology and shaping the future."

ollama_embedder = OllamaEmbeddings(
    model="embeddinggemma:latest",
    # dimensions=512 #by default 768
    )

embedding_query = ollama_embedder.embed_query(text=text)

loaders = PyPDFLoader(file_path = "./Openclaw_Research_Report.pdf", mode ="page")

documents = loaders.load()

print("Total Documents: ", len(documents))

chunker = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)

chunks = chunker.split_documents(documents)

print("Total Chunks: " , len(chunks))

text_documents = [doc.page_content for doc in chunks]
print("Total text documents: " , len(text_documents))

embedding_documents = ollama_embedder.embed_documents(
    texts=text_documents,
)

print("embedding_documents", len(embedding_documents))

print("dimension of embedding_documents", len(embedding_documents[0]))


