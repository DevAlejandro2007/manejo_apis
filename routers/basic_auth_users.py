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

def search_user_db(usrname: str):
    if usrname in users_db:
        return UserDB(**users_db[usrname])
    
def search_user(usrname: str):
    if usrname in users_db:
        return User(**users_db[usrname])

async def current_user(token: str = Depends(oauth2)):
    user =  search_user(token)      
    if not  user:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, 
                            detail="NO ESTAS AUTORIZADO", headers={"WWW-Authenticate":"Bearer"})  

    if user.disable:  
        return HTTPException(status_code= status.HTTP_400_BAD_REQUEST, 
                            detail="USUARIO INACTIVO", headers={"WWW-Authenticate":"Bearer"})
    return user


@app.post("/login")         
async def login(form :OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code= 400, detail="USAURIO INCORRECTO")
    
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code= 400, detail="CONTRASEÑA INCORRECTOS")

    return {"acces_token": user.usrname,"token_type": "bearer"}

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user 