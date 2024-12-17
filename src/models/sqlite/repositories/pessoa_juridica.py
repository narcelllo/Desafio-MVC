from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_juridica import LegalPersonTable

class PessoaJuridicaRepository():
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_pessoa_fisica(self) -> list[LegalPersonTable]:
        with self.__db_connection as database:
            try:
                pessoa_fisica = database.session.query(LegalPersonTable).all()
                return pessoa_fisica
            except NoResultFound:
                return []