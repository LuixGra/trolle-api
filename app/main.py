from fastapi import FastAPI
from app.session import engine, Base
from app import models  # importante importar
from app.routers import tasks
from app.routers import auth


app = FastAPI()
app.include_router(tasks.router)
app.include_router(auth.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "TaskFlow API running"}