# Git hub repo

https://github.com/campusx-official/Advanced_Rag_Codes

# Notes

https://drive.google.com/file/d/1Bzyv-FQDymU8ReF6tcX758XX27ax80Ob/view

# LLM
 1. Limitation
    - Knowledge Cut-off
    - hallucination
    - No source Attribution
    - No access to private data


# What is Rag ( Retrieval-Augmented Generation ) ?
-   Generation -> Use the capability of generative AI to generation
-   Retrival -> Central knowledge base where the all the knowledge is exist( just like   database) to return the similar documents
- Augmented -> To enhance something 
- Retrieval-Augmented Generation (RAG) is a GenAI framework that improves Large Language Model (LLM) outputs by referencing trusted, external knowledge bases—such as internal company documents or databases—before generating a response

# Context Assembly
    Input Prompts. + External Knowledege (External retrived knowledge) 

# How RAG works ?
                    ┌─────────────────────┐
                    │  Knowledge Sources  │
                    │---------------------│
                    │ • PDF Documents     |
                    | • PDF Documents     │
                    │ • Websites          │
                    │ • APIs              │
                    │ • Databases         │
                    │ • CSV / Excel       │
                    │ • User Uploads      │
                    └─────────┬───────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │   Data Processing   │
                    │---------------------│
                    │ • Cleaning          │
                    │ • Parsing           │
                    │ • Metadata Extract  │
                    └─────────┬───────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │      Chunking       │
                    │---------------------│
                    │ • Fixed Chunk       │
                    │ • Semantic Chunk    │
                    │ • Overlapping       │
                    └─────────┬───────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │     Embedding       │
                    │---------------------│
                    │ Convert text into   │
                    │ vector embeddings   │
                    └─────────┬───────────┘
                              │
                              ▼
              ┌────────────────────────────────┐
              │   Vector Database / KB Store   │
              │--------------------------------│
              │ • Pinecone                     │
              │ • ChromaDB                     │
              │ • FAISS                        │
              │ • Weaviate                     │
              │ • MongoDB Atlas Vector Search  │
              └──────────────┬─────────────────┘
                             │
                             ▼
                    ┌─────────────────────┐
                    │      Retrieval      │
                    │---------------------│
                    │ • Similarity Search │
                    │ • Hybrid Search     │
                    │ • Re-ranking        │
                    └─────────┬───────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │   Prompt Building   │
                    │---------------------│
                    │ • User Query        │
                    │ • Retrieved Context │
                    │ • System Prompt     │
                    └─────────┬───────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │    LLM Generation   │
                    │---------------------│
                    │ • GPT               │
                    │ • Gemini            │
                    │ • Claude            │
                    │ • Llama             │
                    └─────────┬───────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │   Final Response    │
                    │---------------------│
                    │ • Answer            │
                    │ • Citations         │
                    │ • Sources           │
                    └─────────────────────┘

# Chunking :
    Chunking is the process of breaking large documents or text into smaller meaningful pieces called chunks before generating embeddings.
    In RAG applications, LLMs cannot efficiently process huge documents directly, so we split them into smaller sections.

# Embedding :
    Embedding is a technique that converts text, images, audio, or other data into numerical vectors (list of numbers) so that AI systems can understand the meaning and similarity between data.
    In RAG applications, embeddings are mainly used to convert text into vectors for semantic search.

# Vector Databse :
    A Vector Database is a special type of database designed to store and search vector embeddings efficiently.

# Retrieval : 
    Retrieval is the process of finding and fetching the most relevant information from the vector database based on the user’s query.
    It is one of the core parts of a RAG (Retrieval-Augmented Generation) system.


# Prompt Building : 
    Prompt Building is the process of creating the final input (prompt) that is sent to the LLM.
        Why Prompt Building is Important
        
        LLMs generate answers based on:

        What you ask
        How you ask
        What context you provide

        Bad prompt:

        Hallucinations
        Wrong answers
        Missing context

        Good prompt:

        Accurate answers
        Better formatting
        Better reasoning

#  Failures of RAG
    1. Retriver ( Retrive from knowledge base)-->>  Not work proper to retrive the context data from knowledge source
    2. Generater (Generate from LLM ) --> have proper context query, LLM can't understand user query

    