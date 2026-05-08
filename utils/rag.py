from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter  
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma 
from dotenv import load_dotenv 
import os 

load_dotenv()

api_key = os.getenv("groq_api_key")

def create_vector_store():
    
    loader = TextLoader("data/user_notes.txt")
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    
    split_documents = text_splitter.split_documents(documents)
    
    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    vector_store = Chroma.from_documents(
        documents = split_documents,
        embeddings = embeddings,
        persist_directory = "vector_db"
    )
    
    vector_store.persist()
    
    return vector_store

def search_knowledge_base(query): # query means user question 
    
    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    vector_store = Chroma(
        persist_directory = "vector_db",
        embedding_function = embeddings
    )
    
    results = vector_store.similarity_search(
        query,
        k=3
    )
    
    knowledge_text = ""
    
    for doc in results:
        knowledge_text += doc.page_content + "\n\n" 
        
    return knowledge_text

