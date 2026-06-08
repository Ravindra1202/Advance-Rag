from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import  Document



text = """Artificial intelligence is transforming technology and shaping the future.

Machine learning algorithms are becoming more sophisticated every day. 
Deep learning models can now process vast amounts of data efficiently.

Natural language processing has made significant strides in recent years.
Transformers architecture revolutionized the field in 2017.
Models like GPT and BERT have set new benchmarks.

Computer vision systems can now identify objects with remarkable accuracy.
Convolutional neural networks excel at image recognition tasks.
Self-driving cars rely heavily on advanced computer vision.

The impact of AI extends across multiple industries including healthcare, finance, and transportation.
Ethical considerations around AI development are becoming increasingly important.
Researchers are working on making AI systems more transparent and explainable."""


text2 = """Hi how are you
My name is Rahul

I am teaching RAG
We are Learning about RAG"""

#  in that case it will try to split the text based on the separator list and 
# if it is not able to split it will try to split based on the chunk size and chunk overlap

splitters = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap =20,
    # separators=[ "\n\n" , '\n', ' '] # this is first split it into paragraphs and than into line after that split into space bsed
    separators=[ "\n\n" , '\n']
)

# chunks = splitters.split_text(text=text)

# print(len(chunks))

# print(chunks)

# Load Document in recursive character text splitter

list_of_text = [text, text2]
doc=[]

for text in list_of_text:
    doc.append(Document(page_content=text, metadata={"source" :"AI Text"}))


chunks = splitters.split_documents(documents=doc)

print(len(chunks))

print(chunks)


