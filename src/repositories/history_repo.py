from pathlib import Path
from database_connection import get_database_connection
from note import Note

class HistoryRepository:
    """Class that deals with the database connections."""
    def __init__(self, connection):
        """Constructor.
        
            Args: 
                connection: the database connection
        """
        self._connection = connection

    def find_all(self):
        """Gets all entries from database"""
        cursor = self._connection.cursor()

        cursor.execute("select * from notes")

        rows = cursor.fetchall()

        return [Note(row["expression"], row["time"]) for row in rows]

    def insert(self, note):
        """"Inserts entry into database
            Args:
                note: a Note object
        """
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO notes (expression, time) VALUES (?, ?)",
        [note.expression, note.time])
        self._connection.commit()

    def delete_all(self):
        "Deletes all entries from database"
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM notes")
        self._connection.commit()

history_repository = HistoryRepository(get_database_connection())
notes = history_repository.find_all()