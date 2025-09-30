import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client(Settings(persist_directory=".chroma_store", anonymized_telemetry=False))

collection = client.get_or_create_collection("learnify")

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def add_document(doc_id, text):
    embedding = model.encode([text])[0].tolist()
    collection.add(
        ids=[str(doc_id)],
        documents=[text],
        embeddings=[embedding]
    )

def query_rag(question: str) -> str:
    embedding = model.encode([question])[0].tolist()
    results = collection.query(
        query_embeddings=[embedding],
        n_results=3
    )

    context = "\n".join(results["documents"][0])

    final_prompt = f"""You are an expert tutor. Answer the following question:
Question: {question}
Use this additional context to help:
{context}
Answer clearly and concisely.
"""

    response = groq_client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": final_prompt}],
        temperature=0.6,
    )

    return response.choices[0].message.content
