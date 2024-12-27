from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.physics_person import PhysicsPersonTable
from src.models.sqlite.interfaces.physics_person import PhysicsPersonRepositoryInterface

class PhysicsPersonRepository(PhysicsPersonRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_physics_person(self) -> list[PhysicsPersonTable]:
        with self.__db_connection as database:
            try:
                physics_person = database.session.query(PhysicsPersonTable).all()
                return physics_person
            except NoResultFound:
                return []

    def insert_physics_person(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float) -> None:
        with self.__db_connection as database:
            try:
                physics_person_data = PhysicsPersonTable(
                    renda_mensal = renda_mensal,
                    idade = idade,
                    nome_completo = nome_completo,
                    celular = celular,
                    email = email,
                    categoria = categoria,
                    saldo = saldo
                )

                database.session.add(physics_person_data)
                database.session.commit()
            except Exception:
                database.session.rollback()
                raise Exception("db rollback")
            
    def get_physics_person(self, physics_person_id: int) -> PhysicsPersonTable:
        with self.__db_connection as database:
            try:
                physics_person_data = (
                    database.session
                        .query(PhysicsPersonTable)
                        .filter(PhysicsPersonTable.id == physics_person_id )
                        .with_entities(
                            PhysicsPersonTable.renda_mensal,
                            PhysicsPersonTable.idade,
                            PhysicsPersonTable.nome_completo,
                            PhysicsPersonTable.celular,
                            PhysicsPersonTable.email,
                            PhysicsPersonTable.categoria,
                            PhysicsPersonTable.saldo,
                        )
                        .one()
                )
                return physics_person_data

            except NoResultFound:
                return None