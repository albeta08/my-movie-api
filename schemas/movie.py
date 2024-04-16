from pydantic import BaseModel, Field
from typing import Optional, List




class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_lenght=5 ,max_length=50)
    overview: str = Field(min_lenght=15 ,max_length=50)
    year: int = Field(le=2022)
    rating: float = Field(ge=1, le=10)
    category: str

    class Config():
        json_schema_extra = {
        "example":{
            "id": 1,
            "title": "Registra el nombre de tu pelicula",
            "overview": "Descripcion de la pelicula",
            "year": 2022,
            "rating": 9.8,
            "category": "Accion"

            }
    }
