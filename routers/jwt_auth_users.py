from fastapi import FastAPI,HTTPException, Depends, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    usrname: str
    fullname: str
    email: str
    disable: bool

class UserDB(User):
    password: str

users_db = {
    "mouredev":{
    "usrname": "mouredev",
    "fullname": "Brais Moure",  
    "email": "mouredev@gmail.com",
    "disable": False,   
    "password": "123456"
    },
    "mouredev2":{
    "usrname": "mouredev2", 
    "fullname": "Brais Moure 2",
    "email": "mouredev2@gmail.com",
    "disable": True,   
    "password": "654321"
    },
}