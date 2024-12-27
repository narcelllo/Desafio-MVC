import re
from src.models.sqlite.interfaces.legal_person import LegalPersonRepositoryInterface

class LegalPersonCreaterController:
    def __init__(self, legal_person_repository: LegalPersonRepositoryInterface ) -> None:
        self.__legal_person_repository = legal_person_repository

    def create(self, legal_person_info: dict) -> dict:
        faturamento = legal_person_info["faturamento"]
        idade = legal_person_info["idade"]
        nome_fantasia = legal_person_info["nome_fantasia"]
        celular = legal_person_info["celular"]
        email_corporativo = legal_person_info["email_corporativo"]
        categoria = legal_person_info["categoria"]
        saldo = legal_person_info["saldo"]

        self.__validate_nome_fantasia(nome_fantasia)
        self.__insert_legal_person_in_db(faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)
        formated_response = self.__format_response(legal_person_info)
        return formated_response

    def __validate_nome_fantasia(self, nome_fantasia: str, ) -> None:
        
        non_valid_caracteres = re.compile(r'[^a-zA-Z\' ]')

        if non_valid_caracteres.search(nome_fantasia):
            raise Exception("Invalid name!")
        
    def __insert_legal_person_in_db(self, faturamento: float, idade: int, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: float) -> None:
        self.__legal_person_repository.insert_legal_person(faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)
    
    def __format_response(self, legal_person_info: dict) -> dict:
        return{
            "data": {
                "type": "Legal Person",
                "count": 1,
                "atributes": legal_person_info
            }
        }
