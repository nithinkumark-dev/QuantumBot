import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS  # ✅ updated
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

VECTORSTORE_DIR = "vectorstore_index"

def create_vector_store():
    if os.path.exists(VECTORSTORE_DIR):
        return
    loader = TextLoader("story.txt", encoding='utf-8')  # ✅ fix encoding
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(VECTORSTORE_DIR)

def get_similar_docs(query, k=3):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
    vectorstore = FAISS.load_local(VECTORSTORE_DIR, embeddings, allow_dangerous_deserialization=True)
    docs = vectorstore.similarity_search(query, k=k)
    return "\n\n".join([doc.page_content for doc in docs])
