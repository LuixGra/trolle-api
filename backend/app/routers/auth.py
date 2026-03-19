"""
Coracao do sistema de login
Endpoints para register, login e jwt tokens

Senhas hasheadas
oAuth2
"""

from fastapi import APIRouter, Depends, HTTPException #Rotas
from sqlalchemy.orm import Session
from app.session import SessionLocal
from app.session import get_db
from app import models, schemas
from app.security import hash_password, verify_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm #>:)

#ROTAS
router = APIRouter(prefix="/auth", tags=["Auth"])


##POST /auth/register
@router.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    #Verifica se usuario ja existe
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")


    hashed = hash_password(user.password)#HASHED >:)
    new_user = models.User(email=user.email, hashed_password=hashed)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user #retorna sem senha

#POST /auth/login
@router.post("/login")
#recebe dados no formato application/x-www-form-urlencoded
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == form_data.username).first()

    if not db_user or not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": db_user.email}) #TOKEN JWT

    return {"access_token": token, "token_type": "bearer"}