from abc import ABC, abstractmethod

class PhysicsPersonFinderController(ABC):

    @abstractmethod
    def find(self, physics_person_id: int) -> dict:
        pass