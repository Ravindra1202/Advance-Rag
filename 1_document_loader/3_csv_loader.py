from langchain_community.document_loaders import CSVLoader
from pathlib import Path

file_path =Path("./knowledge_source/organizations.csv")
print(file_path.exists())

file_path.as_posix()

# source_column is the source of the metadata from the column
# metadata_columns is the list of metadata wich is show the metadata in the list
# content_columns is the which data you need to vectorise 
csv_loaders = CSVLoader(file_path=file_path, source_column="Industry" , metadata_columns=['Website', 'Founded', 'Number of employees'], content_columns=['Description', 'Organization Id'])

documents = csv_loaders.load()

print(len(documents))

print(documents[0].metadata)
print(documents[0].page_content)
