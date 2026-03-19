"""
Modelos usados pra aplicaçao. 

SQLAlchemy ORM models:
- User
- Tasks

Utilizado conceito de relacao entre tabelas. Bem gostosin no azeite.
"""

#importa os tipos usados no banco atraves de SQLAlchemy
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.session import Base

#USUARIO
class User(Base):
    """
    Um usuario possui id(int), email(str) e hashed_password(str).
    """

    __tablename__ = "users"#nome

    id = Column(Integer, primary_key=True, index=True)#index melhora perfomance de busca
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    #RELACAO USUARIO TASK
    tasks = relationship("Task", back_populates="owner")

    #user.tasks



#TASKS
class Task(Base):
    """
    Uma task possui id, title(str), description(str) e completed(boolean).
    """
    __tablename__ = "tasks"#nome

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    #RELACAO TASK USUARIO
    owner = relationship("User")

    #User(1) --> N Tasks
    #tasks.owner.email 