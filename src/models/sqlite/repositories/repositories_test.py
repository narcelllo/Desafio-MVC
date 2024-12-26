import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .legal_person import LegalPersonRepository
from .physics_person import PhysicsPersonRepository

#db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Interação com o banco de dados insert_physics_person")
def test_insert_physics_person():
    renda_mensal = 1500.50
    idade = 30
    nome_completo = "Marcello Magno"
    celular = "(15) 99999-9999"
    email = "email@mail.com"
    categoria = "CLT"
    saldo = -3000.30

    repo = PhysicsPersonRepository(db_connection_handler)
    repo.insert_physics_person(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)

@pytest.mark.skip(reason="Interação com o banco de dados insert_legal_person")
def test_insert_legal_person():
    faturamento = 15000.50
    idade = 3
    nome_fantasia = "MarcelloLTDA"
    celular = "(15) 99999-9999"
    email_corporativo = "email@corpmail.com"
    categoria = "ME"
    saldo = 700.000

    repo = LegalPersonRepository(db_connection_handler)
    repo.insert_legal_person(faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)