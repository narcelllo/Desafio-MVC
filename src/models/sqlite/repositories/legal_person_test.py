from src.models.sqlite.settings.connection import db_connection_handler
from .legal_person import LegalPersonRepository

db_connection_handler.connect_to_db()

def test_list_legal_person():
    repo = LegalPersonRepository(db_connection_handler)
    response = repo.list_legal_person()
    print()
    print(response)