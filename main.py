from fastapi import FastAPI
from fastapi import Depends
from app.src.service import friend_service
from app.src.connection.db_connection import engine
from app.src.connection.db_connection import SessionLocal
from app.src.service.friend_service import *
from app.src.service.friend_service import Session


# Instancia do FastAPI
app = FastAPI()

# Criando as tabelas do DB quando iniciar ou reiniciar
friend_service.Base.metadata.create_all(bind=engine)

# Dependência do SessionLocal
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        raise e
    finally:
        db.close()
        

# Endpoint inicial
@app.get("/")
def home():
    return {"message": "Hello World"}

# Endpoint de listagem de usuário por Id
@app.get("/get_friend/{id}/")
def get_friend(id:int, db:Session = Depends(get_db)):
    friend = Friend.get_friend(db=db, id=id)
    if friend:
        return friend, 200
    return {"message": "Usuário não encontrado"}, 404


# Endpoint de listagem de todos os usuários
@app.get("/list_friends")
def list_friends(db:Session = Depends(get_db)):
    friends_list = Friend.list_friends(db=db)
    if friends_list:
        return friends_list, 200
    return {"message": "Nenhum usuário encontrado"}, 404


# Endpoint de criação de um novo usuário
@app.post("/create_friend")
def create_friend(first_name:str,last_name:str,age:int,db:Session = Depends(get_db)):
    friend = Friend.create_friend(
        db=db,
        first_name=first_name,
        last_name=last_name,
        age=age
    )
    if friend:
        return friend, 201
    return {"message": "Erro ao criar usuário"}, 500


# Endpoint de atualização de um usuário por Id
@app.put("/update_friend/{id}/") #id is a path parameter
def update_friend(id:int, first_name:str, last_name:str, age:int, db:Session=Depends(get_db)):
    db_friend = Friend.get_friend(db=db, id=id)
    if db_friend:
        updated_friend = Friend.update_friend(
            db=db, 
            id=id, 
            first_name=first_name, 
            last_name=last_name, 
            age=age
        )
        return updated_friend, 200
    return {"message": "Usuário não encontrado"}, 404


# Endpoint de exclusão de um usuário por Id
@app.delete("/delete_friend/{id}/")
def delete_friend(id:int, db:Session=Depends(get_db)):
    db_friend = Friend.get_friend(db=db, id=id)
    if db_friend:
        return {"message": "Usuário excluído com sucesso"}, 200
    return {"message": "Usuário não encontrado"}, 404

