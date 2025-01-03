from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.legal_person import LegalPersonTable
from src.models.sqlite.interfaces.legal_person import LegalPersonRepositoryInterface

class LegalPersonRepository(LegalPersonRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_legal_person(self) -> list[LegalPersonTable]:
        with self.__db_connection as database:
            try:
                pessoa_fisica = database.session.query(LegalPersonTable).all()
                return pessoa_fisica
            except NoResultFound:
                return []
    
    def insert_legal_person(self, faturamento: float, idade: int, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: float) -> None:
        with self.__db_connection as database:
            try:
                legal_person_data = LegalPersonTable(
                    faturamento = faturamento,
                    idade = idade,
                    nome_fantasia = nome_fantasia,
                    celular = celular,
                    email_corporativo = email_corporativo,
                    categoria = categoria,
                    saldo = saldo
                )

                database.session.add(legal_person_data)
                database.session.commit()
            except Exception:
                database.session.rollback()
                raise Exception("db rollback")

    def get_legal_person(self, legal_person_id: int) -> LegalPersonTable:
        with self.__db_connection as database:
            try:
                legal_person_data = (
                    database.session
                        .query(LegalPersonTable)
                        .filter(LegalPersonTable.id == legal_person_id )
                        .with_entities(
                            LegalPersonTable.faturamento,
                            LegalPersonTable.idade,
                            LegalPersonTable.nome_fantasia,
                            LegalPersonTable.celular,
                            LegalPersonTable.email_corporativo,
                            LegalPersonTable.categoria,
                            LegalPersonTable.saldo,
                        )
                        .one()
                )
                return legal_person_data

            except NoResultFound:
                return None
