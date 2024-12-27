from src.models.sqlite.interfaces.legal_person import LegalPersonRepositoryInterface
from src.models.sqlite.entities.legal_person import LegalPersonTable

class LegalPersonFinderController:
    def __init__(self, legal_person_repository: LegalPersonRepositoryInterface ) -> None:
        self.__legal_person_repository = legal_person_repository

    def find(self, legal_person_id: int) -> dict:
        legal_person = self.__find_legal_person_in_db(legal_person_id)
        response = self.__format_response(legal_person)
        return response

    def __find_legal_person_in_db(self, legal_person_id: int) -> LegalPersonTable:
        legal_person = self.__legal_person_repository.get_legal_person(legal_person_id)
        if not legal_person:
            raise Exception("Conta não encontrada!")
        
        return legal_person

    def __format_response(self, legal_person: LegalPersonTable) -> dict:
        return{
            "data": {
                "type": "Legal Person",
                "count": 1,
                "atributes": {
                    "faturamento": legal_person.faturamento,
                    "idade": legal_person.idade,
                    "nome_fantasia": legal_person.nome_fantasia,
                    "celular": legal_person.celular,
                    "email_corporativo": legal_person.email_corporativo,
                    "categoria": legal_person.categoria,
                    "saldo": legal_person.saldo
                }
            }
        }
