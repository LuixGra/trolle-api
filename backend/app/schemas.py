"""
Esquemas do pydantic para validacao de requests e repostas.
Esses esquemas garatem a validacao dos dados e controla o que eh exposto pela API
"""

#base pra criar os esquemas, pydantic valida automaticamente os dados
from pydantic import BaseModel
from pydantic import EmailStr

##TASK
#CRIACAO DA TASK
class TaskCreate(BaseModel):
    title: str #obrigatorio
    description: str | None = None #opcional

#RESPOSTA DA API
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool = False

    #muito importante, permite converter direto  do SQLAlchemy
    class Config:
        from_attributes = True

#UPDATE (/PUT)
class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None


##USUARIO
#CRIACAO DO USUARIO
class UserCreate(BaseModel):
    email: EmailStr
    password: str #senha nao criptografada

#LOGIN
class UserLogin(BaseModel):
    email: str
    password: str

#RESPOSTA DA API
class UserResponse(BaseModel):
    id: int
    email: str
    #sem senha rsrs

    class Config:
        from_attributes = True