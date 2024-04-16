from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middewares.jwt_bearer import JWTBearer
from services import movie
from services.movie import MovieService
from schemas.movie import Movie




movie_router = APIRouter()

@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code = 200, dependencies=[Depends(JWTBearer())])
def get_movie()-> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(content=jsonable_encoder(result))

@movie_router.get('/movies/{id}',tags=['movies'], response_model=Movie)
def get_movie(id: int=Path(ge=1, le=2000))->Movie:
    db = Session()
    result = MovieService(db).get_movies(id)
    if not result:
        return JSONResponse(status_code=404,content={'message':"No encontrado"})
   
    return JSONResponse(status_code = 200,content=jsonable_encoder(result))


@movie_router.get('/movies/', tags=['movies'],response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_lenght=5, max_lenght=15))->List[Movie]:
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
    
@movie_router.post('/movies', tags=['movies'])
def create_movie(movie: Movie)-> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(content={"message":"Se ha registrado la pelicula"})

@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict)
def updade_movie(id:int, movie: Movie)-> dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404,content={'message':"No encontrado"})
    MovieService(db).update_movie(id, movie)
    return JSONResponse(content={"message":"Se ha actualizado la pelicula"})

        

@movie_router.delete('/movies/{id}', tags=['movies'],response_model=dict)
def delete_movie(id: int)->dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404,content={'message':"No encontrado"})
    MovieService(db).delete_movie(id)
    return JSONResponse(content={"message":"Se ha eliminado la pelicula"})

