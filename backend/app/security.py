"""
Seguranca do nosso sistema
Esse modulo toma contade:
    Hashear senhas e verificar senhas hasheadas
    Criacao de tokens JWT
    Retorno de usuario autenticado da sessao atual
oAuth2 babyy
"""

from passlib.context import CryptContext #Criptografia para senha
from jose import JWTError, jwt #JWT, cria e le tokens temporarios
from datetime import datetime, timedelta #Usado pra definir expiracao do token
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer #Sistema de autenticacao
from sqlalchemy.orm import Session #Sessao do banco de dados
from app.session import SessionLocal
from app import models #Modelos ja criados

import os

##ENV
SECRET_KEY = os.getenv("SECRET_KEY") 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 #Token expira em 60 minutos

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login") #rota onde o login acontece

#PEGA SESSAO DO BANCO DE DADOS
def get_db():
    #conexao
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() #fechar importante

#CRIA HASH DA SENHA
def hash_password(password: str):
    return pwd_context.hash(password)

#VERIFICA PASSWORD
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

#FINALMENTE JWT
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) #expiracao
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) #TOKEN

#CRITICO
#FUNCAO QUE PROTEGE AS ROTAS PEGANDO USUARIO ATUAL
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub") #Email do token
        if email is None:
            #Email inexistente/token invalido
            raise HTTPException(status_code=401, detail="Invalid token")
    #Token invalido
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(models.User).filter(models.User.email == email).first()
    if user is None:
        #Usuario inexistente/credenciais invalidas
        raise HTTPException(status_code=401, detail="Invalid credencials")

    return user