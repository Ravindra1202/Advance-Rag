from langchain_text_splitters import CharacterTextSplitter
from langchain_core.documents import Document


text =  """Artificial intelligence is transforming technology and shaping the future. 
Machine learning algorithms are becoming more sophisticated every day.
Deep learning models can now process vast amounts of data efficiently.

Natural language processing has made significant strides in recent years.
Computer vision systems can now identify objects with remarkable accuracy.
Reinforcement learning is enabling robots to learn complex tasks autonomously.

The impact of AI extends across multiple industries including healthcare, finance, and transportation.
Ethical considerations around AI development are becoming increasingly important.
Researchers are working on making AI systems more transparent and explainable."""
# splitters = CharacterTextSplitter(chunk_size=50,
#                                   chunk_overlap=10,
#                                   length_function=len, # it is used for character count based splitter
#                                   separator=""
#                                   )


# chunks = splitters.split_text(text=text)

# print(chunks)

# print(len(chunks))

            # Token base splitting


# token_based_splitter = CharacterTextSplitter.from_tiktoken_encoder(encoding_name="cl100k_base", chunk_size=50, chunk_overlap=10)

# chunks = token_based_splitter.split_text(text=text)

# print(len(chunks))
# print('chunks', chunks)


#               Document base splitting


doc = [Document(page_content=text, metadata ={"source": "AI Text"})]

# print(doc)

spilitter = CharacterTextSplitter(chunk_size=100, chunk_overlap =20 , separator="")

chunks = spilitter.split_documents(documents=doc)

print(len(chunks))

print(chunks)