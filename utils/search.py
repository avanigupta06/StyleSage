from sentence_transformers import SentenceTransformer
from pinecone import Pinecone

model = SentenceTransformer("all-MiniLM-L6-v2")
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("PINECONE_API_KEY")
host = os.getenv("HOST")


pc = Pinecone(api_key=api_key)
index = pc.Index(host=host)

def semantic_search(query, top_k=5):
    query_embedding = model.encode(query).tolist()
    results = index.query(
        namespace="products",
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True
    )
    return results["matches"]