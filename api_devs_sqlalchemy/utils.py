from models import Pessoas, db_session


def insere_pessoas():
    pessoa = Pessoas(nome='Andrews', idade='29')
    print(pessoa)
    db_session.add(pessoa)
    db_session.commit()
    

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)

if __name__ == '__main__':
    insere_pessoas()
    consulta_pessoas()