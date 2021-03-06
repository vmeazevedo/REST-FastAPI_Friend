from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from ..connection.db_connection import Base


class Friend(Base):
    __tablename__ = "friend"

    # Criando colunas da tabela
    id = Column(Integer,primary_key=True, index=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    age = Column(Integer)

    # Criando o construtor
    def __init__(self,first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # Método para criar um novo usuário
    def create_friend(db:Session, first_name, last_name, age):
        new_friend = Friend(
        first_name=first_name, 
        last_name=last_name, 
        age=age
        )
        db.add(new_friend)
        db.commit()
        db.refresh(new_friend)
        return new_friend

    # Método para buscar um usuário por Id
    def get_friend(db:Session, id:int):
        db_friend = db.query(Friend).filter(Friend.id==id).first()
        return db_friend

    # Método para listar todos os usuários
    def list_friends(db:Session):
        all_friends = db.query(Friend).all()
        return all_friends

    # Método para atualizar um usuário
    def update_friend(db:Session, id:int, first_name: str, last_name: str, age:int):
        db_friend = Friend.get_friend(db=db, id=id)
        db_friend.first_name = first_name
        db_friend.last_name = last_name
        db_friend.age = age

        db.commit()
        db.refresh(db_friend)
        return db_friend

    # Método para excluir um usuário
    def delete_friend(db:Session, id:int):
        db_friend = Friend.get_friend(db=db, id=id)
        db.delete(db_friend)
        db.commit()