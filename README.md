# Banking Knowledge AI Assistant

**AI Engineer Portfolio Project | Projekt portfolio AI Engineer**

Banking knowledge assistant based on Python, FastAPI and Retrieval-Augmented Generation (RAG).

Asystent wiedzy bankowej oparty na Pythonie, FastAPI oraz architekturze Retrieval-Augmented Generation (RAG).

**Documentation / Dokumentacja:** [Polski](#polski) | [English](#english)

---

## Polski

### 1. Opis projektu

Banking Knowledge AI Assistant to projekt asystenta AI przeznaczonego do odpowiadania na pytania dotyczące produktów, usług i procedur bankowych na podstawie dokumentów.

Docelowo aplikacja będzie wykorzystywała architekturę RAG (Retrieval-Augmented Generation), łącząc wyszukiwanie odpowiednich fragmentów dokumentów z generowaniem odpowiedzi przez model językowy (LLM).

Projekt powstaje jako demonstracja umiejętności z zakresu AI Engineering i nie jest oficjalnym systemem żadnego banku.

### 2. Status projektu

**W trakcie realizacji — etap 1: Backend API**

Aktualnie zaimplementowano:

- Aplikację backendową FastAPI.
- Endpoint `GET /health`.
- Endpoint `POST /ask`.
- Walidację pytań z wykorzystaniem Pydantic.
- Automatyczną dokumentację OpenAPI / Swagger UI.
- Trzy testy automatyczne Pytest.
- Środowisko Python 3.12 oraz zarządzanie zależnościami.

Endpoint `/ask` zwraca obecnie odpowiedź demonstracyjną. Integracja z LLM i bazą wiedzy nie została jeszcze zaimplementowana.

### 3. Wykorzystane technologie

**Zaimplementowane:**

- Python 3.12
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- Git

**Planowane:**

- LangChain — orkiestracja mechanizmu RAG.
- LlamaIndex — przetwarzanie i indeksowanie dokumentów.
- ChromaDB — wektorowa baza danych.
- Embeddings — reprezentacja semantyczna dokumentów.
- LLM — generowanie odpowiedzi.
- RAG — generowanie odpowiedzi z wykorzystaniem wyszukanych źródeł.

### 4. Architektura docelowa

Przepływ obsługi pytania:

1. Użytkownik przesyła pytanie do FastAPI.
2. LangChain uruchamia mechanizm wyszukiwania kontekstu.
3. Baza ChromaDB zwraca odpowiednie fragmenty dokumentów.
4. Model LLM otrzymuje pytanie i wyszukany kontekst.
5. API zwraca odpowiedź oraz odniesienia do dokumentów.

Oddzielny proces indeksowania wykorzysta LlamaIndex do wczytywania dokumentów, podziału tekstu i zapisywania embeddings w bazie wektorowej.

### 5. Struktura projektu

```text
banking-knowledge-ai-assistant/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── tests/
    └── test_api.py
```

### 6. Instalacja i uruchomienie

**Wymagania:** Python 3.12, Git.

Sklonuj repozytorium po jego opublikowaniu na GitHubie:

```bash
git clone URL_REPOZYTORIUM
cd banking-knowledge-ai-assistant
```

Utwórz środowisko wirtualne w Windows:

```powershell
py -3.12 -m venv .venv
```

Zainstaluj zależności:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Uruchom serwer:

```powershell
.\.venv\Scripts\python.exe -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Dokumentacja Swagger UI:

`http://127.0.0.1:8000/docs`

### 7. Endpointy API

**GET /health**

Sprawdza stan aplikacji.

Przykładowa odpowiedź:

```json
{
  "status": "ok",
  "message": "Banking Knowledge AI Assistant is running"
}
```

**POST /ask**

Przyjmuje pytanie użytkownika.

Przykładowe żądanie:

```json
{
  "question": "Jak otworzyc konto bankowe?"
}
```

Aktualnie endpoint zwraca odpowiedź informującą o braku integracji z RAG oraz pustą listę źródeł.

Wymagana długość pytania: od 3 do 500 znaków. Nieprawidłowe dane powodują odpowiedź HTTP 422.

### 8. Testowanie

Uruchom testy automatyczne:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/ -v
```

Aktualnie dostępne testy:

- Poprawność endpointu `/health`.
- Obsługa prawidłowego pytania.
- Odrzucanie zbyt krótkiego pytania.

**Ostatni zweryfikowany wynik: 3/3 testy zaliczone.**

### 9. Bezpieczeństwo

- Środowisko `.venv` i pliki `.env` są wykluczone z Git przez `.gitignore`.
- Serwer deweloperski uruchamiany jest lokalnie.
- Projekt nie wymaga rzeczywistych danych klientów.
- Docelowo przewidziano przechowywanie sekretów w zmiennych środowiskowych.
- Aplikacja ma charakter demonstracyjny i nie jest przeznaczona do zastosowań produkcyjnych.

### 10. Plan rozwoju

- [x] Konfiguracja środowiska Python.
- [x] Utworzenie aplikacji FastAPI.
- [x] Implementacja endpointów `/health` i `/ask`.
- [x] Walidacja danych Pydantic.
- [x] Pierwsze testy automatyczne.
- [x] Konfiguracja zależności.
- [ ] Wczytywanie dokumentów bankowych.
- [ ] Podział dokumentów na fragmenty.
- [ ] Generowanie embeddings.
- [ ] Integracja ChromaDB.
- [ ] Implementacja pipeline RAG.
- [ ] Integracja modelu LLM.
- [ ] Cytowanie źródeł.
- [ ] Testy mechanizmu RAG.
- [ ] Końcowa dokumentacja i demonstracja.

---

## English

### 1. Project Overview

Banking Knowledge AI Assistant is a document-based AI assistant designed to answer questions about banking products, services and procedures.

The target application will use Retrieval-Augmented Generation (RAG), combining document retrieval with answer generation using a Large Language Model (LLM).

This is an independent AI Engineering portfolio project and is not affiliated with or endorsed by any bank.

### 2. Project Status

**In development — Phase 1: Backend API**

Currently implemented:

- FastAPI backend application.
- `GET /health` endpoint.
- `POST /ask` endpoint.
- Request validation with Pydantic.
- Automatic OpenAPI / Swagger UI documentation.
- Three automated Pytest tests.
- Python 3.12 environment and dependency management.

The `/ask` endpoint currently returns a placeholder response. LLM integration and knowledge retrieval have not yet been implemented.

### 3. Technology Stack

**Implemented:**

- Python 3.12
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- Git

**Planned:**

- LangChain — RAG workflow orchestration.
- LlamaIndex — document processing and indexing.
- ChromaDB — vector database.
- Embeddings — semantic text representations.
- LLM — answer generation.
- RAG — retrieval-grounded answer generation.

### 4. Target Architecture

Question-processing workflow:

1. A user submits a question through FastAPI.
2. LangChain orchestrates context retrieval.
3. ChromaDB retrieves relevant document chunks.
4. The LLM receives the question and retrieved context.
5. The API returns an answer with source references.

A separate indexing process will use LlamaIndex to load documents, split their content into chunks and store embeddings in the vector database.

### 5. Project Structure

```text
banking-knowledge-ai-assistant/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── tests/
    └── test_api.py
```

### 6. Installation and Setup

**Requirements:** Python 3.12, Git.

Clone the repository once published on GitHub:

```bash
git clone REPOSITORY_URL
cd banking-knowledge-ai-assistant
```

Create a Python virtual environment on Windows:

```powershell
py -3.12 -m venv .venv
```

Install dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Start the development server:

```powershell
.\.venv\Scripts\python.exe -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Swagger UI documentation:

`http://127.0.0.1:8000/docs`

### 7. API Endpoints

**GET /health**

Checks application health.

Example response:

```json
{
  "status": "ok",
  "message": "Banking Knowledge AI Assistant is running"
}
```

**POST /ask**

Accepts a user question.

Example request:

```json
{
  "question": "How can I open a bank account?"
}
```

Currently, this endpoint returns a placeholder message indicating that RAG is not yet connected, along with an empty list of sources.

Questions must be between 3 and 500 characters long. Invalid input returns HTTP 422.

### 8. Automated Tests

Run the test suite:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/ -v
```

Current tests cover:

- Health endpoint functionality.
- Valid question handling.
- Short-question validation.

**Last verified result: 3/3 tests passed.**

### 9. Security Considerations

- Virtual environments and `.env` files are excluded from Git through `.gitignore`.
- The development server runs locally.
- No real customer data is required.
- Environment variables are planned for secret management.
- The application is a demonstration project and is not production-ready.

### 10. Development Roadmap

- [x] Configure Python environment.
- [x] Create FastAPI application.
- [x] Implement `/health` and `/ask` endpoints.
- [x] Add Pydantic validation.
- [x] Implement initial automated tests.
- [x] Configure dependencies.
- [ ] Implement banking document loading.
- [ ] Add document chunking.
- [ ] Generate embeddings.
- [ ] Integrate ChromaDB.
- [ ] Implement RAG pipeline.
- [ ] Connect LLM.
- [ ] Add source citations.
- [ ] Test RAG functionality.
- [ ] Finalize documentation and demo.

---

## Author / Autor

Adam Feliński

AI Engineer Portfolio Project

October 2026 / Październik 2026
