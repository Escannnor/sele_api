from sqlmodel import Field, SQLModel
from db import create_db_and_tables

class Movie(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    name : str | None = Field(default='No title', max_length=100, unique=True)
    image : str
    year : int | None = Field(default=None)
    url : str
    
class MovieDescription(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    movie_id : int | None = Field(default=None, foreign_key='movie.id')
    description : str
    
create_db_and_tables()