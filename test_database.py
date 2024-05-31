# test_database.py

import unittest
from database import add_student
from datetime import date
import psycopg2

class TestStudentDatabase(unittest.TestCase):
    def setUp(self):
        self.conn = psycopg2.connect(database="student_db", user="student_user", password="password", host="localhost")
        self.cur = self.conn.cursor()
        self.cur.execute("DELETE FROM Oppilaat")
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_add_student(self):
        student_id = add_student(self.conn, "Testi Oppilas", date(2000, 1, 1), "testi@example.com")
        self.cur.execute("SELECT * FROM Oppilaat WHERE opiskelija_id = %s", (student_id,))
        student = self.cur.fetchone()
        self.assertIsNotNone(student)
        self.assertEqual(student[1], "Testi Oppilas")
        self.assertEqual(student[2], date(2000, 1, 1))
        self.assertEqual(student[3], "testi@example.com")

if __name__ == "__main__":
    unittest.main()
