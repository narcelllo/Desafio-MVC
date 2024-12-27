import pytest
from .physics_person_creator_controller import PhysicsPersonCreatorController

class MockLegalPersonRepository:
    def insert_physics_person(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float):
        pass

def test_create():
    physics_person_info = {
        "renda_mensal": 15000.50,
        "idade": 3,
        "nome_completo": "MarcelloLTDA",
        "celular": "(15) 99999-9999",
        "email": "email@mail.com",
        "categoria": "debito",
        "saldo": 700.000
    }
    controller = PhysicsPersonCreatorController(MockLegalPersonRepository())
    response = controller.create(physics_person_info)

    assert response ["data"]["type"] == "Physics Person"
    assert response ["data"]["count"] == 1
    assert response ["data"]["atributes"] == physics_person_info

def test_create_error():
    physics_person_info = {
        "faturamento": 15000.50,
        "idade": 3,
        "nome_fantasia": "MarcelloLTDA 123",
        "celular": "(15) 99999-9999",
        "email_corporativo": "email@corpmail.com",
        "categoria": "ME",
        "saldo": 700.000
    }
    controller = PhysicsPersonCreatorController(MockLegalPersonRepository())
    with pytest.raises(Exception):
        controller.create(physics_person_info)