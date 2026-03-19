"""
Main aplication entry point

Inicializa FastAPI, configura o middleware(CORS) e registra todas as rotas da API.

Rotas:
-Users
-Auth
-Tasks
"""

from fastapi import FastAPI#Main app
from app.session import engine, Base
from app import models
#endpoints
from app.routers import tasks
from app.routers import auth


app = FastAPI()#inicializaçao
app.include_router(tasks.router)
app.include_router(auth.router)

Base.metadata.create_all(bind=engine)

#RAIZ
@app.get("/")
def root():
    return {"message": "TaskFlow API running"}#teste

#Ligacao entre Frontend Backend
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],#importante limitar o acesso em producao
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
