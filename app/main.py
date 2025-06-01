from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import auth, qa
from app.db.database import engine
from app.db.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://192.168.0.103:3000",  # ✅ this is your actual frontend IP
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(qa.router, prefix="/qa", tags=["Q&A"])

@app.get("/")
def root():
    return {"message": "Learnify++ API is running 🚀"}
