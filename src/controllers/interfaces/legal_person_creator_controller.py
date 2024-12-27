from abc import ABC, abstractmethod

class LegalPersonCreaterControllerInterface(ABC):

    @abstractmethod
    def create(self, legal_person_info: dict) -> dict:
        pass