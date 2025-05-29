from fastapi import FastAPI
from app.routes import auth

app = FastAPI(title="Learnify++ API")

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

@app.get("/")
def root():
    return {"message": "Learnify++ API is running 🚀"}
