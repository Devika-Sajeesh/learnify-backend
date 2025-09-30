import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")  # lightweight, good enough

index = faiss.IndexFlatL2(384)  # 384 = vector size of MiniLM
stored_questions = []  # list of original texts
stored_user_ids = []

def add_question(text, user_id):
    embedding = model.encode([text])[0]
    index.add(np.array([embedding], dtype=np.float32))
    stored_questions.append(text)
    stored_user_ids.append(user_id)

def search_similar(query, k=3):
    embedding = model.encode([query])[0]
    D, I = index.search(np.array([embedding], dtype=np.float32), k)
    return [(stored_questions[i], stored_user_ids[i]) for i in I[0]]
