from fastapi import APIRouter, Depends, HTTPException
from app.core.jwt import get_current_user
from app.models.user import User
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.models.question import Question
from app.services.vectorstore import add_question, search_similar
from groq import Groq
import os
from dotenv import load_dotenv
from app.services.rag import add_document, query_rag

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
router = APIRouter()

@router.post("/ask")
def ask_question(q: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    question = Question(user_id=current_user.id, question_text=q)
    db.add(question)
    db.commit()
    db.refresh(question)

    add_question(q, current_user.id)

    return {"message": "Question stored successfully", "id": question.id}

@router.get("/similar")
def get_similar_questions(query: str):
    results = search_similar(query)
    return {"similar": results}

@router.get("/ai-answer")
def get_ai_answer(query: str):
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": f"Answer this question clearly:\n\n{query}"}],
            temperature=0.7,
        )
        return {"answer": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/rag/add")
def add_to_rag(doc_id: int, text: str):
    add_document(doc_id, text)
    return {"message": "Text added to vector DB"}

@router.get("/rag/answer")
def get_rag_answer(q: str):
    answer = query_rag(q)
    return {"answer": answer}
