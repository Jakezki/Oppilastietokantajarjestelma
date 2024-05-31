import psycopg2

def add_student(conn, name, birthdate, contact_info):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO Oppilaat (nimi, syntyma_aika, yhteystiedot)
            VALUES (%s, %s, %s) RETURNING opiskelija_id;
        """, (name, birthdate, contact_info))
        student_id = cur.fetchone()[0]
        conn.commit()
        return student_id

