from abc import ABC, abstractmethod

class LegalPersonCreaterController(ABC):

    @abstractmethod
    def create(self, legal_person_info: dict) -> dict:
        pass