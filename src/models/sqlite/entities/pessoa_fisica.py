from sqlalchemy import Column, BIGINT, String, REAL
from src.models.sqlite.settings.base import Base

class PhysicsPersonTable(Base):
    __tablename__ = "pessoa_fisica"

    id = Column(BIGINT, primary_key=True, nullable=False)
    faturamento = Column(REAL, nullable=False)
    idade = Column(BIGINT, nullable=False)
    nome_fantasia = Column(String, nullable=False)
    celular = Column(String, nullable=False)
    email_corporativo = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    saldo = Column(REAL, nullable=False)

    def __repr__(self):
        return (
            f"PessoaFisicaTable [\n"
            f"    id={self.id},\n"
            f"    nome_fantasia={self.nome_fantasia},\n"
            f"    idade={self.idade},\n"
            f"    email_corporativo={self.email_corporativo},\n"
            f"    celular={self.celular},\n"
            f"    faturamento={self.faturamento},\n"
            f"    saldo={self.saldo},\n"
            f"    categoria={self.categoria}\n"
            f"]"
        )