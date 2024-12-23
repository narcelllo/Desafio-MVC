from sqlalchemy import Column, BIGINT, String, REAL
from src.models.sqlite.settings.base import Base

class PhysicsPersonTable(Base):
    __tablename__ = "pessoa_fisica"

    id = Column(BIGINT, primary_key=True, nullable=False)
    renda_mensal = Column(REAL, nullable=False)
    idade = Column(BIGINT, nullable=False)
    nome_completo = Column(String, nullable=False)
    celular = Column(String, nullable=False)
    email = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    saldo = Column(REAL, nullable=False)

    def __repr__(self):
        return (
            f"PhysicsPersonTable [\n"
            f"    id={self.id},\n"
            f"    nome_completo={self.nome_completo},\n"
            f"    idade={self.idade},\n"
            f"    email={self.email},\n"
            f"    celular={self.celular},\n"
            f"    renda_mensal={self.renda_mensal},\n"
            f"    saldo={self.saldo},\n"
            f"    categoria={self.categoria}\n"
            f"]"
        )