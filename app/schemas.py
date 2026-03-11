from pydantic import BaseModel

#classe schema de criação de task
#titulo e descrição
class TaskCreate(BaseModel):
    title: str
    description: str | None = None

#classe schema resposta, indexando id e completed boolean
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool

    class Config:
        from_attributes = True

#task update
class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None


##ESQUEMAS DE USUARIO
class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True