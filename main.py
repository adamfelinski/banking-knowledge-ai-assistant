
from fastapi import FastAPI
from pydantic import BaseModel, Field


# Konfiguracja aplikacji
app = FastAPI(
    title="Banking Knowledge AI Assistant",
    description="AI assistant for banking documents using RAG",
    version="0.1.0"
)


# Model pytania użytkownika
class AskRequest(BaseModel):
    question: str = Field(
        min_length=3,
        max_length=500,
        description="Pytanie dotyczące dokumentacji bankowej"
    )


# Model odpowiedzi aplikacji
class AskResponse(BaseModel):
    question: str
    answer: str
    sources: list[str]


# Sprawdzanie stanu aplikacji
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Banking Knowledge AI Assistant is running"
    }


# Endpoint chatbota
@app.post("/ask", response_model=AskResponse)
def ask_question(request: AskRequest):
    return AskResponse(
        question=request.question,
        answer=(
            "Modul RAG nie jest jeszcze podlaczony. "
            "Nie moge udzielic odpowiedzi na podstawie dokumentow."
        ),
        sources=[]
    )
