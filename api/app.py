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
    return jsonify(result), 200


@app.route("/notes", methods=["POST"])
def create_note():
    req = request.json

    name = req.get("name", None)
    if not name:
        return jsonify("missing name in request body"), 400

    result = notes_dao.create_note(name)
    return jsonify(result), 200


@app.route("/notes/<int:note_id>", methods=["PATCH"])
def update_note(note_id):
    req = request.json

    body = req.get("body", None)
    if not body:
        return jsonify("missing body in request body"), 400

    notes_dao.update_note(note_id, body)
    return jsonify(), 204


@app.route("/notes/<int:note_id>", methods=["GET"])
def get_note_by_id(note_id):
    result = notes_dao.get_note_by_id(note_id)
    return jsonify(result), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
