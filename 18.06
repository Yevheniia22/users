from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field, field_validator, ValidationError
from sqlalchemy import create_engine, Boolean, Integer, String, Column, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
import uvicorn


from sqlalchemy.orm import Session

DATABASE_URL = 'sqlite:///to_do.db'
engine = create_engine(DATABASE_URL)
session = sessionmaker(bind=engine, autoflush=False, autocomit=False)
Base = declarative_base()


class ToDoItem(Base):
    __tablename__ = 'to_do'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String(200))
    status = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)
app = FastAPI()

class ToDoBase(BaseModel):
    title: str
    description: str
    status: bool = False

class ToDoCreate(ToDoBase):
    pass

class ToDoUpdate(ToDoBase):
    pass

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get('/to_do/')
def get_all_todos(db: Session = Depends(get_db)):
    to_dos = db.query(ToDoItem).all()
    return to_dos


@app.get('/to_do/{todo_id}')
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    to_do = db.query(ToDoItem).filter(todo_id == ToDoItem.id)
    if not to_do:
        raise HTTPException(status_code=404, detail='There are no todos')
    return  to_do


@app.post('/to_do')
def create_todo(todo: ToDoCreate, db: Session = Depends(get_db)):
    to_do = ToDoItem(**todo.dict())
    db.add(to_do)
    db.commit()
    db.refresh(to_do)
    return to_do


@app.put('/update/{todo_id}')
def db_update(todo: ToDoUpdate, todo_id: int,  db: Session = Depends(get_db)):
    to_do = db.query(ToDoItem).filter(todo_id == ToDoItem.id)
    if not to_do:
        raise HTTPException(status_code=404, detail='There are no todos')
    to_do_upd = ToDoItem(**todo.dict())

    if to_do_upd.title is not None:
        to_do.title = to_do_upd.title
    if to_do_upd.description is not None:
        to_do.description = to_do_upd.description
    if to_do_upd.status is not None:
        to_do.status = to_do_upd.status

    db.commit()
    db.refresh(to_do)
    return to_do


@app.delete('/delete/{todo_id}')
def db_delete(todo_id: int,  db: Session = Depends(get_db)):
    to_do = db.query(ToDoItem).filter(todo_id == ToDoItem.id)
    if not to_do:
        raise HTTPException(status_code=404, detail='There are no todos')
    db.delete(to_do)
    db.commit()


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8001, reload=True)
