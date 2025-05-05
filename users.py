from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/user",
                   tags= ["user"],
                   responses={404:{"MESSAGE": "NO ENCONTRADO"}})

"""
**PARA INICIAR EL SERVIDOR**
fastapi dev (api.py) --> NOMBRE DE TU ARCHIVO

**PARA VER DOCUMENTACIÓN DE LA API**
/docs para ver la documentación de la API en Swagger    
/redoc para ver la documentación de la API en ReDoc
"""

# Entidad User
class User(BaseModel):
    id : int 
    name: str
    surname: str
    url: str
    age : int



#Lista de Usuarios 
users_list = [User(id = 1 ,name = "Alejo",surname = "Rojas",url = "www.youtube.com",age = 15),
            User(id = 2,name = "Alejandro",surname ="Benitez",url ="www.google.com",age =  15),
            User(id = 3,name ="x",surname = "z", url= "www.instagram.com",age= 15)]

#Direccion de la lista de usuarios
@router.get("/users")
async def users():
    return users_list

# VIA PATH (URL)
@router.get("/{id}")
async def user(id: int):
    return found_usuario(id)

# VIA QUERY (URL CON SIGNO DE INTERROGACION )
@router.get("/query")
async def user(id: int):
     return found_usuario(id)


# CREAR USUARIO 
@router.post("/",response_model=  User, status_code=201)
async def user(user: User):
    if type(found_usuario(user.id)) == User:
        raise HTTPException(status_code= 404, detail="EL USUARIO YA EXISTE")
    users_list.append(user)
    return user

#ACTUALIZAR UN RECURSO
@router.put("/")
async def user(user: User):
    
    found = False

    for index,saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            return user
    if found == False:
        return {"ERROR":" NO SE HA ENCONTRADO EL USUARIO"}

    
#ELIMINAR UN RECURSO 
@router.delete("/{id}")
async def user(id: int):
    found = False
    for index, saved_u in enumerate(users_list):
        if saved_u.id == id:
            del users_list[index]
            found = True
            return {" COMPLETED": " USUARIO ELIMINADO"}
        if not found: 
            return{"ERROR": "USUARIO NO ELIMINADO"  }
            

#FUNDION BUSCAR USUARIO 
def found_usuario(id:int):
    users = filter(lambda user: user.id == id, users_list) 
    try:
        return list(users)[0]
    except:
        return {"ERROR": "NO SE HA ENCONTRADO EL USUARIO"}



