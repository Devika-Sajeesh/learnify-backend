# Learnify Backend

Learnify Backend is a **FastAPI-based REST API** that powers the Learnify educational platform.  
It provides secure authentication, user data handling, AI-powered features, and database management.

---

## 🚀 Features
- **User Authentication** (Register, Login, JWT-based sessions)
- **AI Chatbot API** integration (LLaMA3 / Groq API)
- **GPA-based study plan generation**
- **Community Q&A management**
- **Resource & Content APIs**
- **Wellness tools** (mood tracking, meditation, etc.)
- **Database migrations** with Alembic

---

## 📂 Project Structure
learnify-backend/
│-- app/ # Core FastAPI application code
│-- alembic/ # Database migration scripts
│-- .env # Environment variables
│-- requirements.txt # Python dependencies
│-- alembic.ini # Alembic configuration
│-- README.md # Project documentation


---

## 🛠️ Tech Stack
- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database ORM**: SQLAlchemy
- **Migrations**: Alembic
- **Authentication**: JWT
- **AI API**: Groq API (LLaMA3-70B)
- **Server**: Uvicorn

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/learnify-backend.git
cd learnify-backend

python -m venv venv
# Activate on Windows
venv\Scripts\activate
# Activate on macOS/Linux
source venv/bin/activate

pip install -r requirements.txt

DATABASE_URL=postgresql+psycopg2://user:password@localhost/learnify
SECRET_KEY=your_jwt_secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
GROQ_API_KEY=your_groq_api_key

alembic upgrade head

uvicorn app.main:app --reload
```
## Deployment
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

🛡️ Security Notes
Never commit .env to version control.

Use strong SECRET_KEY for JWT authentication.

Rotate API keys regularly.

👩‍💻 Author
Devika Sajeesh
