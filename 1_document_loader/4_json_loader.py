from langchain_community.document_loaders import JSONLoader
from pathlib import Path


file_path = Path("./knowledge_source/apparels.json")

file_path.as_posix()

print(file_path.exists())

# craete the loader

def metadata_func(record:dict, metadata:dict)->dict:
    metadata['product_name'] = record['productName']
    metadata['category'] = record['category']
    metadata['price'] = record['price']
    del metadata['seq_num']
    return metadata
# define the source user content_key
# add url and other content in metadata use metadata_func
json_loader = JSONLoader(file_path=file_path ,jq_schema=".products[]",
                         content_key="Description",
                         metadata_func=metadata_func
                         )



documents = json_loader.load()

print(documents)

# for doc in documents:
#     print(doc.metadata)
#     print(doc.page_content , end="\n\n")

# Add information in  metadata 
 