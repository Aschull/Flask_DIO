from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Configuração para criação da base de dados - SQLite
engine = create_engine('sqlite:///storage.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

# Tabelas
class Pessoas(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    def __repr__(self):
        return '<Pessoas {}>'.format(self.nome)

class Atividades(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship('Pessoas')
    
    

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()