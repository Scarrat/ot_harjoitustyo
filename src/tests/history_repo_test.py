from datetime import datetime
import unittest
from repositories.history_repo import history_repository
from initialize_database import initialize_database
from entities.note import Note

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.note_ten = Note("5+5=10",datetime.now().strftime("%d/%m %H:%M"))
        self.note_twenty = Note("10+10=10",datetime.now().strftime("%d/%m %H:%M"))
        self.note_hundred = Note("10*10=100",datetime.now().strftime("%d/%m %H:%M"))

    def tearDown(self):
        initialize_database()


    def test_find_all(self):
        history_repository.insert(self.note_ten)
        history_repository.insert(self.note_twenty)
        history_repository.insert(self.note_hundred)
        notes = history_repository.find_all()
        self.assertEqual(len(notes), 3)

    