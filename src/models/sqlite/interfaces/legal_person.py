from abc import ABC, abstractmethod
from src.models.sqlite.entities.legal_person import LegalPersonTable

class LegalPersonInterface(ABC):
    @abstractmethod
    def list_pessoa_fisica(self) -> list[LegalPersonTable]:
        pass

    @abstractmethod
    def insert_legal_person(self, faturamento: float, idade: int, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: float) -> None:
        pass