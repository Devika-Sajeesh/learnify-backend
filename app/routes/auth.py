from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.user import UserCreate, UserOut
from app.models.user import User
from app.core.security import hash_password
from fastapi.security import OAuth2PasswordRequestForm
from app.core.jwt import create_access_token
from datetime import timedelta
from app.core.security import pwd_context
from app.core.jwt import get_current_user
from app.core.jwt import get_current_user

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_pw = hash_password(user.password)
    new_user = User(
        username=user.username,
        password_hash=hashed_pw,
        gpa=user.gpa,
        branch=user.branch,
        sem=user.sem
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not pwd_context.verify(form_data.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=60)
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserOut)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

from groq import Groq
import os
from fastapi import HTTPException, Depends
from app.core.jwt import get_current_user
from app.models.user import User
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@router.get("/planner")
def generate_study_plan(current_user: User = Depends(get_current_user)):
    prompt = f"""
    Create a personalized study plan for:
    - GPA: {current_user.gpa}
    - Branch: {current_user.branch}
    - Semester: {current_user.sem}
    - Subjects I'm good at: {current_user.subin}
    - Subjects I struggle with: {current_user.subnin}
    Output in Markdown.
    """
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return {"plan": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))







