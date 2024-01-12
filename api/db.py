import psycopg2


def get_postgres_conn():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="supersecure",
        host="postgres",
        port=5432,
    )
