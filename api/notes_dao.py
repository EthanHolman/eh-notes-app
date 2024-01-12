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

    def create_note(self, name, body):
        with self._get_cursor() as cur:
            cur.execute(
                """
                insert into notes (name, body)
                values (%s, %s);
                """,
                (
                    name,
                    body,
                ),
            )
        self._conn.commit()
