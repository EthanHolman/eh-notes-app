from flask import Flask, jsonify, request
from flask_cors import CORS
from init_db import init_db
from db import get_postgres_conn
from notes_dao import NotesDao

app = Flask(__name__)
cors = CORS(app)

# TODO: use flyway for migrations
init_db()

pg_conn = get_postgres_conn()
notes_dao = NotesDao(pg_conn)


@app.route("/notes", methods=["GET"])
def list_all_notes():
    result = notes_dao.get_notes()
    return jsonify(result)


@app.route("/notes", methods=["POST"])
def create_note():
    req = request.json

    name = req.get("name", None)
    if not name:
        return jsonify("missing name in request body"), 400

    body = req.get("body", None)
    if not body:
        return jsonify("missing body in request body"), 400

    notes_dao.create_note(name, body)
    return jsonify(), 204


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
