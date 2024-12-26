from abc import ABC, abstractmethod
from src.models.sqlite.entities.physics_person import PhysicsPersonTable

class PhysicsPersonRepositoryInterface(ABC):
    @abstractmethod
    def list_physics_person(self) -> list[PhysicsPersonTable]:
        pass

    @abstractmethod
    def insert_physics_person(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float) -> PhysicsPersonTable:
        pass