from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from pprint import pp
from langchain_community.document_loaders.parsers import TesseractBlobParser, RapidOCRBlobParser
from langchain_community.document_loaders import PDFMinerLoader, PDFPlumberLoader


file_path =Path("./knowledge_source/attention_is_all_you_need.pdf")

file_path.as_posix()

                                # Type -1

# # create loader
# mode ="single than its return only a single page "
# mode = "page" than its load page wise pdf

pypdf_loader = PyPDFLoader(file_path=file_path.as_posix(), mode="page")

documents = pypdf_loader.load()
# print("="*50 +'All documents' + "="*50)
# print(documents)

# print("="*50 +'Length of Document' + "="*50)
# print(len(documents))

# print("="*50 +'Documents' + "="*50)
# print(documents)

# print("="*50 +'Metadata' + "="*50)
# pp(documents.metadata)

# print("="*50 +'Page content' + "="*50)
# print(documents.page_content)


                            # Type -2

# create pypdf instance which can extract images but its not working 
 
pypdf_image_loader = PyPDFLoader(
    file_path=file_path,
    mode="single",
    extract_images=True,
    images_inner_format="html-img",
    images_parser=TesseractBlobParser(),
)

documents_with_images = pypdf_image_loader.load()

# print("="*50 +' Document with images ' + "="*50)

# print("="*50 +'Length of Document' + "="*50)
# print(len(documents_with_images))

# print("="*50 +'Documents' + "="*50)
# print(documents_with_images[0])

# print("="*50 +'Metadata' + "="*50)
# pp(documents_with_images[0].metadata)

# print("="*50 +'Page content' + "="*50)
# print(documents_with_images[0].page_content[-700:])


                            # Type -3

# create the miner LOader to extract the pad and tables from pdf

pdfminor_loader = PDFMinerLoader(
    file_path=file_path , mode="page",
    extract_images=True,
    images_parser=RapidOCRBlobParser(),
    images_inner_format="html-img"
    )

documents_with_pdfMiner_images =pdfminor_loader.load()

# print(documents_with_pdfMiner_images[5].page_content)

pdf_plumber_loader =  PDFPlumberLoader(file_path=file_path) 

documents_with_plumber = pdf_plumber_loader.load()
print(documents_with_plumber[0].metadata)
print(documents_with_plumber[0].page_content)
