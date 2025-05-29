from fastapi import FastAPI
from app.routes import auth
from app.db.database import engine
from app.db.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Learnify++ API")

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])


@app.get("/")
def root():
    return {"message": "Learnify++ API is running 🚀"}
