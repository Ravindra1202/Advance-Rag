from langchain_community.document_loaders import TextLoader

from pathlib import Path

file_path = Path('./knowledge_source/transformers.txt')

print(file_path)
print(file_path.exists())

# define loader

loader = TextLoader(file_path=file_path, encoding="utf-8")

documents = loader.load()

print( type(documents))
print(type(documents[0]))

print("="*50 +'documents' + "="*50)
print(documents)

print("="*50 +'documents' + "="*50)
print(documents[0])

print("="*50 +'Metadata' + "="*50)
print(documents[0].metadata)

print("="*50 +'Page content' + "="*50)
print(documents[0].page_content)

print("="*50 +'length of Document' + "="*50)
print(len(documents))