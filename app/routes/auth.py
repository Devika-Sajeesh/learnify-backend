from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.user import UserCreate, UserOut
from app.models.user import User
from app.core.security import hash_password

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
