from src.models.sqlite.settings.connection import db_connection_handler
from .physics_person import PhysicsPersonRepository

db_connection_handler.connect_to_db()

def test_list_physics_person():
    repo = PhysicsPersonRepository(db_connection_handler)
    response = repo.list_physics_person()
    print()
    print(response)