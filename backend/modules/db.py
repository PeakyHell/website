import os, psycopg


def connect_db():

    with open(os.getenv("POSTGRES_PASSWORD")) as f: POSTGRES_PASSWORD = f.read().strip()

    return psycopg.connect(
        host="database",
        port="5432",
        dbname="postgres",
        user="postgres",
        password=POSTGRES_PASSWORD
    )


def db_query(query):

    conn = connect_db()

    cur = conn.cursor()
    cur.execute(query)

    if "SELECT" in query:
        return cur.fetchall()

    conn.commit()

    return
