from abc import ABC, abstractmethod

class LegalPersonCreatorControllerInterface(ABC):

    @abstractmethod
    def create(self, legal_person_info: dict) -> dict:
        pass