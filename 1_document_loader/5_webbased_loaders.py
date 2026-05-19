import os

os.environ["USER_AGENT"] = "Mozilla/5.0"

from langchain_community.document_loaders import WebBaseLoader, RecursiveUrlLoader
from bs4 import BeautifulSoup

url = "https://docs.langchain.com/oss/python/integrations/document_loaders/web_base"
url2 = "https://docs.langchain.com/oss/python/integrations/document_loaders/pypdfloader"
url3 = "https://docs.langchain.com/oss/python/integrations/document_loaders/pdfminer"


# loader = WebBaseLoader(web_paths=[url, url2, url3], verify_ssl=True)

# documents = loader.load()
# print(len(documents))

# soup = BeautifulSoup(documents[0].page_content, features="html.parser")

# # Extract clean text
# text = soup.get_text(separator=" ", strip=True)

# # Remove multiple spaces/newlines
# clean_text = " ".join(text.split())

# print(clean_text)

# Recursive loader 


url="https://docs.langchain.com/oss/python/integrations/document_loaders" 
def custom_extractor(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")  # better parser
    return soup.get_text()

recursive_loader = RecursiveUrlLoader(url=url , max_depth=2, extractor=custom_extractor)

# print(len(documents))

# for i in range(10):
#     print("\n\n"+"---"*50+"\n\n")
#     print(documents[i].page_content)


# documents = recursive_loader.load()

#                         Lazy_load 

# lazy load retun the generator object and we can iterate over it to get the documents one by one.
# it works like yield in python and it will load the documents one by one when we iterate over it.
#  This is useful when we have a large number of documents and we don't want to load them all at
#  once in memory. 
documents  = recursive_loader.lazy_load()

counter = 0
for doc in documents:

    if(counter ==100):
        break
    print("\n\n"+"---"*50+"\n\n")
    print(doc.page_content[:500])
    print(doc.metadata)
    counter +=1
