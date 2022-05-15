from repositories.history_repo import history_repository as DefaultRepo

class HistoryService:
    """A class that acts as connector between repository and UI"""
    def __init__(self, history_repo =DefaultRepo):
        """Constructor for the class."""
        self.note = None
        self._history_repo = history_repo

    def save_note(self, note):
        """"Saves entry into history database"""
        self._history_repo.insert(note)

    def get_notes(self):
        """Gets all entries from history database"""
        return self._history_repo.find_all()

    def delete_all(self):
        "Deletes all entries from history database"
        self._history_repo.delete_all()

history_service=HistoryService()
