from abc import ABC, abstractmethod

class LegalPersonFinderController(ABC):

    @abstractmethod
    def find(self, legal_person_id: int) -> dict:
        pass