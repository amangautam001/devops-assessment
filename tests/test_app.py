from app.app import app


def test_home_endpoint():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

    # Intentional wrong value for CI failure demonstration
    assert response.json["message"] == "Wrong message"


def test_add_student_without_name():
    client = app.test_client()

    response = client.post(
        "/students",
        json={}
    )

    assert response.status_code == 400
    assert response.json["error"] == "Student name is required"


def test_health_endpoint(monkeypatch):
    class MockConnection:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            return False

        def execute(self, query):
            return None

    monkeypatch.setattr(
        "app.app.get_db_connection",
        lambda: MockConnection()
    )

    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"
    assert response.json["database"] == "connected"
