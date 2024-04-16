from fastapi import FastAPI

from config.database import  engine, Base
from middewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router





app = FastAPI()
app.title = "Mi aplicacion con Fast Api"
app.version ="0.0.1"

app.add_middleware(ErrorHandler) 
app.include_router(movie_router)
app.include_router(user_router)


Base.metadata.create_all(bind=engine)

def a():
    pass

        
movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "en un exhuverante planeta llamado pandora viven los Na'vi",
        "years":"2009",
        "rating": 7.8,
        "category": "Accion"
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "en un exhuverante planeta llamado pandora viven los Na'vi",
        "years":"2009",
        "rating": 7.8,
        "category": "Accion"
    }
]

@app.get('/',tags=['home'])
def message():
    return HTTPResponse('<h1>hello world</h1>')











