from psycopg2.extras import RealDictCursor


class NotesDao:
    def __init__(self, conn):
        if not conn:
            raise ValueError("conn is required")

        self._conn = conn

    def _get_cursor(self):
        return self._conn.cursor(cursor_factory=RealDictCursor)

    def get_notes(self):
        with self._get_cursor() as cur:
            cur.execute(
                """
                select note_id, name, created_dt, modified_dt
                from notes;
                """
            )
            results = cur.fetchall()
        return results

    def get_note_by_id(self, note_id):
        with self._get_cursor() as cur:
            cur.execute("select * from notes where note_id = %s", (note_id,))
            result = cur.fetchone()
        return result

    def create_note(self, name):
        result = None
        with self._get_cursor() as cur:
            cur.execute(
                """
                insert into notes (name)
                values (%s)
                returning notes.note_id;
                """,
                (name,),
            )
            result = cur.fetchone()
        self._conn.commit()
        return result

    def update_note(self, note_id, name, body):
        with self._get_cursor() as cur:
            cur.execute(
                """
                update notes set name = %s, body = %s
                where note_id = %s;
                """,
                (
                    name,
                    body,
                    note_id,
                ),
            )
        self._conn.commit()
