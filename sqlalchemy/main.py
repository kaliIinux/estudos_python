import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

engine = sqlalchemy.create_engine('sqlite:///enterpise.db', echo=True) # echo = ver os códigos sql

# Declarando o mapeamento
base = declarative_base()

class User(base):
    
    __tablename__ = 'users' # obrigatório
    id = Column(Integer, primary_key=True) # obrigatório
    name = Column(String(50))
    fullname = Column(String(50))
    age = Column(Integer)
    
    def __repr__(self):
        return f"<User(name={self.name}, fullname={self.fullname}, age={self.age}), id={self.id}>"
    
# Criar tabela no banco de dados
base.metadata.create_all(engine)

# Criar instâncias da classe
user1 = User(name='Ângelo', fullname='Ângelo do Prado Carnevale', age=17)
user2 = User(name='Diego', fullname='Diego Alencar Jacober', age=18)
user3 = User(name='Nicole', fullname='Nicole Siqueira', age=18)

# Criar uma sessão
Session = sessionmaker(bind=engine)
session = Session()

# Adicionar objetos (INSERT)
#session.add(user1)
#session.commit()

#session.add_all([user2, user3])
#session.commit()

# Consultar objetos (SELECT)

query_user = session.query(User).filter_by(name='Diego').first()

# Iterar pelos usuários da tabela
for instance in session.query(User).order_by(User.id):
    print(instance)