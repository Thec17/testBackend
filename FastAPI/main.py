from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI() # URL: http://127.0.0.1:8000
# Para montar el servidor local hay que ir a la ruta del main (o el archivo a montar) -> cd .\curso_backend_mouredev\FastAPI
# Después se ejecuta en la terminal: fastapi dev main.py (o el archivo a montar)

app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)
app.mount("/static", StaticFiles(directory="static"), name="static") # URL: http://127.0.0.1:8000/static/images/pfp.jpg

@app.get("/")
async def root():
    return "Hola FastAPI!"

@app.get("/url")
async def url():
    return {"url": "https://mouredev.com/python"}