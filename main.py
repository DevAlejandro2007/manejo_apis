from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles


"""
**PARA INICIAR EL SERVIDOR**
fastapi dev (api.py) --> NOMBRE DE TU ARCHIVO

**PARA VER DOCUMENTACIÓN DE LA API**
/docs para ver la documentación de la API en Swagger    
/redoc para ver la documentación de la API en ReDoc
"""


app = FastAPI()

#routers
app.include_router(products.router)
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="static"), name = "static")

#url local: http://127.0.0.1:8000/

@app.get("/")
async def root():
    return "Hola Fast Api"

@app.get("/url")
async def url():
    return {"URL":"www.google.com"}






