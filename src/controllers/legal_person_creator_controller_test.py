import pytest
from .legal_person_creator_controller import LegalPersonCreaterController

class MockLegalPersonRepository:
    def insert_legal_person(self, faturamento: float, idade: int, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: float):
        pass

def test_create():
    legal_person_info = {
        "faturamento": 15000.50,
        "idade": 3,
        "nome_fantasia": "MarcelloLTDA",
        "celular": "(15) 99999-9999",
        "email_corporativo": "email@corpmail.com",
        "categoria": "credito",
        "saldo": 700.000
    }
    controller = LegalPersonCreaterController(MockLegalPersonRepository())
    response = controller.create(legal_person_info)

    assert response ["data"]["type"] == "Legal Person"
    assert response ["data"]["count"] == 1
    assert response ["data"]["atributes"] == legal_person_info

def test_create_error():
    legal_person_info = {
        "faturamento": 15000.50,
        "idade": 3,
        "nome_fantasia": "MarcelloLTDA 123",
        "celular": "(15) 99999-9999",
        "email_corporativo": "email@corpmail.com",
        "categoria": "ME",
        "saldo": 700.000
    }
    controller = LegalPersonCreaterController(MockLegalPersonRepository())
    with pytest.raises(Exception):
        controller.create(legal_person_info)