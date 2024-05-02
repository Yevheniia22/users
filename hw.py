#напишіть мені роут, який повертає усіх студентів нашої групи і ще 2 окремі роути ,
#кожен який повинен повертати ім'я ваших викладачів із софт та теч скілів

from fastapi import FastAPI

app = FastAPI()

list_students = ["студент1", "студент2", "студент3", "студент4", "студент5",]


@app.get('/students/')
def students():
    return {'message': list_students}


@app.get('/tech/')
async def tech():
    return {'message': 'Maksym'}


@app.get('/soft/')
async def soft():
    return {'message': 'Anastasiia'}