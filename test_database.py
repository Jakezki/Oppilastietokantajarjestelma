import unittest
import psycopg2

class TestStudentDatabase(unittest.TestCase):

    def setUp(self):
        # Yhdisty tietokantaan
        self.conn = psycopg2.connect(
            dbname="student_db",
            user="student_user",
            password="password",
            host="localhost"
        )
        self.cur = self.conn.cursor()

        # Lisää testidataa tietokantaan
        self.lisaa_testidata()

    def lisaa_testidata(self):
        # Lisää testidataa tietokantaan
        self.cur.execute("""
            INSERT INTO Oppilaat (nimi, syntyma_aika, yhteystiedot)
            VALUES ('Testi Opiskelija', '2000-01-01', 'testi@example.com');
        """)
        self.cur.execute("""
            INSERT INTO Kurssit (kurssi_nimi, opettaja)
            VALUES ('Testi Kurssi', 'Testi Opettaja');
        """)
        self.cur.execute("""
            INSERT INTO Ilmoittautumiset (opiskelija_id, kurssi_id, ilmoittautumispaiva)
            VALUES (1, 1, '2024-01-01');
        """)
        self.conn.commit()

    def tearDown(self):
        # Sulje tietokantayhteys
        self.conn.close()

    def test_opiskelijan_lisays(self):
        # Testaa opiskelijan lisäämistä
        # TODO: Lisää testitapahtumia
        pass

    def test_kurssin_lisays(self):
        # Testaa kurssin lisäämistä
        # TODO: Lisää testitapahtumia
        pass

    def test_ilmoittautumisen_lisays(self):
        # Testaa ilmoittautumisen lisäämistä
        # TODO: Lisää testitapahtumia
        pass

if __name__ == '__main__':
    unittest.main()
