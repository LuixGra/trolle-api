"""
Rotas de task para operacoes CRUD(Create, Read, Uptade, Delete)
Rotas protegidas e autenticadas.
"""

from fastapi import APIRouter, Depends #Cria rotas
from sqlalchemy.orm import Session
from app import models, schemas
from app.session import SessionLocal
from app.security import get_current_user
from app.session import get_db
from fastapi import HTTPException


router = APIRouter(prefix="/tasks", tags=["Tasks"])

##POST /tasks
@router.post("/", response_model=schemas.TaskResponse)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user) #usuario autenticado
):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        user_id=current_user.id #ligacao ao usuario
    )

    db.add(db_task) #add
    db.commit() #comit
    db.refresh(db_task) #put
    return db_task

##GET /tasks
@router.get("/", response_model=list[schemas.TaskResponse])
def list_tasks(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    tasks = db.query(models.Task).filter(models.Task.user_id == current_user.id).all()
    #Cada usuario ve apenas as suas tasks (filter)
    return tasks

##PUT(UPDATE) /tasks{id}
@router.put("/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    #pega a task pelo ID
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()

    #testa se a taks nao é nula
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    #VERIFICA DONO
    if db_task.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    #testa se o titulo da task n é nulo
    if task.title is not None:
        db_task.title = task.title
    #testa se a descricao n é nula
    if task.description is not None:
        db_task.description = task.description
    #testa se o valor boolean n é nulo
    if task.completed is not None:
        db_task.completed = task.completed
    
    db.commit()
    db.refresh(db_task)

    return db_task


##DELETE /tasks{id}
@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    if db_task.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    db.delete(db_task) #remove do banco
    db.commit()

    return {"message": "Task deleted successfully"}

