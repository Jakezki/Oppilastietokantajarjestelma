import psycopg2

# Yhdisty tietokantaan
conn = psycopg2.connect(
    dbname="student_db",
    user="student_user",
    password="password",
    host="localhost"
)

def lisaa_opiskelija(conn, nimi, syntyma_aika, yhteystiedot):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO Oppilaat (nimi, syntyma_aika, yhteystiedot)
            VALUES (%s, %s, %s)
            RETURNING opiskelija_id;
        """, (nimi, syntyma_aika, yhteystiedot))
        opiskelija_id = cur.fetchone()[0]
        conn.commit()
        return opiskelija_id

def lisaa_kurssi(conn, kurssi_nimi, opettaja):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO Kurssit (kurssi_nimi, opettaja)
            VALUES (%s, %s)
            RETURNING kurssi_id;
        """, (kurssi_nimi, opettaja))
        kurssi_id = cur.fetchone()[0]
        conn.commit()
        return kurssi_id

def ilmoittaudu_kurssille(conn, opiskelija_id, kurssi_id, ilmoittautumispaiva):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO Ilmoittautumiset (opiskelija_id, kurssi_id, ilmoittautumispaiva)
            VALUES (%s, %s, %s);
        """, (opiskelija_id, kurssi_id, ilmoittautumispaiva))
        conn.commit()

# Käyttäjän syötteiden kysyminen
nimi = input("Syötä opiskelijan nimi: ")
syntyma_aika = input("Syötä opiskelijan syntymäaika (muodossa VVVV-KK-PP): ")
yhteystiedot = input("Syötä opiskelijan yhteystiedot: ")
kurssi_nimi = input("Syötä kurssin nimi: ")
opettaja = input("Syötä kurssin opettajan nimi: ")
ilmoittautumispaiva = input("Syötä ilmoittautumispäivä (muodossa VVVV-KK-PP): ")

# Lisää opiskelija ja kurssi tietokantaan
uusi_opiskelija_id = lisaa_opiskelija(conn, nimi, syntyma_aika, yhteystiedot)
print("Uusi opiskelija lisätty, opiskelija_id:", uusi_opiskelija_id)

uusi_kurssi_id = lisaa_kurssi(conn, kurssi_nimi, opettaja)
print("Uusi kurssi lisätty, kurssi_id:", uusi_kurssi_id)

# Ilmoittaudu kurssille
ilmoittaudu_kurssille(conn, uusi_opiskelija_id, uusi_kurssi_id, ilmoittautumispaiva)
print("Opiskelija ilmoittautunut kurssille")

# Sulje yhteys
conn.close()
