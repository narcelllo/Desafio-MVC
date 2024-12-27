import re
from src.models.sqlite.interfaces.physics_person import PhysicsPersonRepositoryInterface
from .interfaces.physics_person_creator_controller import PhysicsPersonCreatorControllerInterface

class PhysicsPersonCreatorController(PhysicsPersonCreatorControllerInterface):
    def __init__(self, physics_person_repository: PhysicsPersonRepositoryInterface) -> None:
        self.__physics_person_repository = physics_person_repository
        
    def create(self, physics_person_info: dict) -> dict:
        renda_mensal = physics_person_info["renda_mensal"]
        idade = physics_person_info["idade"]
        nome_completo = physics_person_info["nome_completo"]
        celular = physics_person_info["celular"]
        email = physics_person_info["email"]
        categoria = physics_person_info["categoria"]
        saldo = physics_person_info["saldo"]

        self.__validate_nome_completo(nome_completo)
        self.__insert_physics_person_in_db(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
        formated_response = self.__format_response(physics_person_info)
        return formated_response

    def __validate_nome_completo(self, nome_completo: str, ) -> None:
        
        non_valid_caracteres = re.compile(r'[^a-zA-Z\' ]')

        if non_valid_caracteres.search(nome_completo):
            raise Exception("Invalid name!")
        
    def __insert_physics_person_in_db(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float) -> None:
        self.__physics_person_repository.insert_physics_person(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
    
    def __format_response(self, physics_person_info: dict) -> dict:
        return{
            "data": {
                "type": "Physics Person",
                "count": 1,
                "atributes": physics_person_info
            }
        }
