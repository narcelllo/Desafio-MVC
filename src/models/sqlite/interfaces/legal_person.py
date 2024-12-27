from abc import ABC, abstractmethod
from src.models.sqlite.entities.legal_person import LegalPersonTable

class LegalPersonRepositoryInterface(ABC):
    @abstractmethod
    def list_legal_person(self) -> list[LegalPersonTable]:
        pass

    @abstractmethod
    def insert_legal_person(self, faturamento: float, idade: int, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: float) -> None:
        pass

    @abstractmethod
    def get_legal_person(self, legal_person_id: int) -> LegalPersonTable:
        pass