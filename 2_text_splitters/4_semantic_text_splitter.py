# Semantic chunking creates chunks based on the meaning and 
# semantic similarity of the text rather than arbitrary size limits. It 
# starts with an initial chunk and keeps adding sentences as long 
# as they remain semantically similar (measured by cosine 
# similarity of embeddings). When similarity drops below a 
# threshold, a new chunk begins.
# This is like grouping related topics in a conversation - you keep 
# talking about one subject until the topic naturally shifts.

# Advantages:
# • Preserves semantic coherence within chunks
# • More intelligent splitting based on meaning
# • Better retrieval performance in RAG applications
# • Natural topic boundaries
# • Improved context preservation

# Disadvantages:
# • Computationally expensive (requires embeddings for every sentence)
# • Variable chunk sizes can be problematic
# • Slower processing time
# • Requires an embedding model
# • May create very large or very small chunks
# • Difficult to predict chunk count in advance


from langchain_experimental.text_splitter import SemanticChunker

from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from termcolor import COLORS, colored
from random import choice

from dotenv import load_dotenv

load_dotenv()

# below text is taken multiple source like AI, Pasta and Climate change


text = """Artificial intelligence is transforming technology and shaping the future.
Machine learning algorithms are becoming more sophisticated every day.
Deep learning models can now process vast amounts of data efficiently.
Neural networks are inspired by the human brain's structure.
The best pasta recipes include fresh ingredients and proper cooking techniques.
Italian cuisine emphasizes quality olive oil and regional cheeses.
Authentic carbonara uses guanciale, eggs, pecorino romano, and black pepper.
Cooking pasta al dente ensures the best texture and flavor.
Climate change is affecting ecosystems worldwide.
Rising temperatures are causing glaciers to melt at unprecedented rates.
Scientists warn that immediate action is needed to reduce carbon emissions.
Renewable energy sources offer hope for a sustainable future."""

def display_chunks(chunks):
    colors_list = list(COLORS.keys())[2:8]
    print(f"Total Number of Chunks: {len(chunks)}")
    
    for num, chunk in enumerate(chunks, 1):
        print(f"Chunk {num}: Length {len(chunk)} chars")
        print(colored(text=chunk, color=choice(colors_list)), end="\n\n")


chunkers = SemanticChunker(
    embeddings=OpenAIEmbeddings(),
    breakpoint_threshold_amount=0.5,
    breakpoint_threshold_type="percentile"
)

chunks = chunkers.split_text(text=text)

print(len(chunks))

# print(chunks)
display_chunks(chunks)