from fastapi import FastAPI
from fastapi import Depends
from app.src.service import models
from app.src.connection.db import engine
from app.src.connection.db import SessionLocal
from app.src.service.models import *
from app.src.service.models import Session


#initailize FastApi instance
app = FastAPI()

#create the database tables on app startup or reload
models.Base.metadata.create_all(bind=engine)

# getting the db
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        raise e
    finally:
        db.close()
        

# HOME
@app.get("/")
def home():
    return {"message": "Hello World"}

#get a Friend object
@app.get("/get_friend/{id}/")
def get_friend(id:int, db:Session = Depends(get_db)):
    friend = Friend.get_friend(db=db, id=id)
    return friend

#list Friend objects
@app.get("/list_friends")
def list_friends(db:Session = Depends(get_db)):
    friends_list = Friend.list_friends(db=db)
    return friends_list

#create a friend
@app.post("/create_friend")
def create_friend(first_name:str,last_name:str,age:int,db:Session = Depends(get_db)):
    friend = Friend.create_friend(
        db=db,
        first_name=first_name,
        last_name=last_name,
        age=age
    )
    return {"friend": friend}

# update a Friend object
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
        return updated_friend
    else:
        return {"error": f"Friend with id {id} does not exist"}

#delete friend object
@app.delete("/delete_friend/{id}/")
def delete_friend(id:int, db:Session=Depends(get_db)):
    db_friend = Friend.get_friend(db=db, id=id)
    if db_friend:
        return Friend.delete_friend(db=db, id=id)
    else:
        return {"error": f"Friend with id {id} does not exist"}


