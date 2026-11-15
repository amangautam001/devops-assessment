import os
import psycopg

from flask import Flask, jsonify, request

app = Flask(__name__)


def get_db_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST", "db"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "studentdb"),
        user=os.getenv("DB_USER", "studentuser"),
        password=os.getenv("DB_PASSWORD")
    )


def init_db():
    with get_db_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL
            )
        """)


@app.route("/")
def home():
    return jsonify({
        "message": "Student Management API is running"
    })


@app.route("/health")
def health():
    try:
        with get_db_connection() as conn:
            conn.execute("SELECT 1")

        return jsonify({
            "status": "healthy",
            "database": "connected"
        }), 200

    except Exception:
        return jsonify({
            "status": "unhealthy",
            "database": "disconnected"
        }), 503


@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json(silent=True) or {}
    name = data.get("name")

    if not name or not name.strip():
        return jsonify({"error": "Student name is required"}), 400

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO students (name) VALUES (%s) RETURNING id, name",
                (name.strip(),)
            )
            student = cur.fetchone()

    return jsonify({
        "id": student[0],
        "name": student[1]
    }), 201


@app.route("/students", methods=["GET"])
def get_students():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name FROM students ORDER BY id")
            students = cur.fetchall()

    return jsonify([
        {"id": student[0], "name": student[1]}
        for student in students
    ])


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
