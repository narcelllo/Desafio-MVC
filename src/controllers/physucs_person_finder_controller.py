from src.models.sqlite.interfaces.physics_person import PhysicsPersonRepositoryInterface
from src.models.sqlite.entities.physics_person import PhysicsPersonTable
from .interfaces.physucs_person_finder_controller import PhysicsPersonFinderControllerInterface

class PhysicsPersonFinderController(PhysicsPersonFinderControllerInterface):
    def __init__(self, physics_person_repository: PhysicsPersonRepositoryInterface ) -> None:
        self.__physics_person_repository = physics_person_repository

    def find(self, physics_person_id: int) -> dict:
        physics_person = self.__find_physics_person_in_db(physics_person_id)
        response = self.__format_response(physics_person)
        return response

    def __find_physics_person_in_db(self, physics_person_id: int) -> PhysicsPersonTable:
        physics_person = self.__physics_person_repository.physics_person(physics_person_id)
        if not physics_person:
            raise Exception("Conta não encontrada!")
        
        return physics_person

    def __format_response(self, physics_person: PhysicsPersonTable) -> dict:
        return{
            "data": {
                "type": "Physics Person",
                "count": 1,
                "atributes": {
                    "faturamento": physics_person.faturamento,
                    "idade": physics_person.idade,
                    "nome_fantasia": physics_person.nome_fantasia,
                    "celular": physics_person.celular,
                    "email_corporativo": physics_person.email_corporativo,
                    "categoria": physics_person.categoria,
                    "saldo": physics_person.saldo
                }
            }
        }
