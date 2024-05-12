from databases import Database
from fastapi import FastAPI
from sqlalchemy import MetaData, create_engine, Column, Table, Integer, String

DATABASE_URL = 'sqlite:///test.db'
DATABASE = create_engine(DATABASE_URL)
metadata = MetaData()
database = Database(DATABASE_URL)
app = FastAPI()

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('email', String),
    Column('phone number', String),
    Column('birthday', String)
)


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


@app.get('/users/{user_id}')
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    user = await database.fetch_one(query)
    return {'user': user}