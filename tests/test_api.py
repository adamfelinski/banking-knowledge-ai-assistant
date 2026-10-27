
from fastapi.testclient import TestClient
from main import app


# Tworzymy klienta testowego
client = TestClient(app)


# Test 1 - sprawdzenie stanu aplikacji
def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


# Test 2 - poprawne pytanie
def test_ask_valid_question():
    response = client.post(
        "/ask",
        json={"question": "Jak otworzyc konto bankowe?"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["question"] == "Jak otworzyc konto bankowe?"
    assert "answer" in data
    assert data["sources"] == []


# Test 3 - pytanie zbyt krotkie
def test_ask_short_question():
    response = client.post(
        "/ask",
        json={"question": "OK"}
    )

    assert response.status_code == 422

    data = response.json()

    assert data["detail"][0]["type"] == "string_too_short"
