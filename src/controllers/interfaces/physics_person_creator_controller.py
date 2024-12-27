from abc import ABC, abstractmethod

class PhysicsPersonCreatorControllerInterface(ABC):
    
    @abstractmethod
    def create(self, physics_person_info: dict) -> dict:
        pass