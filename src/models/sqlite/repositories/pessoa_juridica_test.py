from src.models.sqlite.settings.connection import db_connection_handler
from .pessoa_juridica import PessoaJuridicaRepository

db_connection_handler.connect_to_db()

def test_list_pessoa_fisica():
    repo = PessoaJuridicaRepository(db_connection_handler)
    response = repo.list_pessoa_fisica()
    print()
    print(response)