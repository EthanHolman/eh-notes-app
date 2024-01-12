from db import get_postgres_conn


# TODO: replace this with flyway
def init_db():
    conn = get_postgres_conn()

    cur = conn.cursor()

    cur.execute(
        """
        create table if not exists notes (
            note_id serial primary key,
            name text,
            body text,
            created_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            modified_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """
    )

    conn.commit()

    cur.close()
    conn.close()


if __name__ == "__main__":
    init_db()
