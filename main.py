from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def f_index():
    return {"FIO": "Куракин Лев Александрович"}

@app.get('/tools')
async def f_index():
    return {"About me": "Я обладаю навыками в области разработки сайтов, изучаю несколько языков программирования, учусь работать с базами данных"}

@app.get('/users')
async def f_index():
    return {"Contacts": "+79619860866"}
