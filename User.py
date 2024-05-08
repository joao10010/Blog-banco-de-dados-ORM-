from conexao_orm import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(Base): # criando uma classe users
    __tablename__ = 'users' # tablename, serve para criaçao de uma tabela

    id = Column(Integer,primary_key=True) # criando primeira coluna chamda ID , e a funcaop primery_key significa que a chave primeira 
    name = Column(String) # colunas do tipo stringfs
    email = Column(String)
    posts = relationship('Post', back_populates='author')
# A função 'relationship()' é usada para criar uma relação entre as classes 'Author' e 'Post'.
# O argumento 'back_populates' é usado para estabelecer uma relação bidirecional.
# Isso significa que se um lado da relação é alterado (por exemplo, um post é adicionado a um autor),
# o outro lado também é atualizado (o post sabe quem é o seu autor).

    def __init__(self, name,email): #criando o construtor
        self.name = name
        self.email = email
    
