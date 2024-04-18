from typing import List, Optional
from fastapi import FastAPI, Query
from recommander import item_based_recommandation
from resolver import random_items, random_genres_items

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/all/")
async def all_movies():
    result = random_items()
    return {"result": result}

@app.get("/genres/{genre}")
async def genre_movies(genre: str):
    result = random_genres_items(genre)
    return {"result": result}

@app.get("/user-based/")
async def user_based(params: Optional[List[str]] = Query(None)):
    return {"message": "user based"}

@app.get("/item-based/{item_id}")
async def item_based(item_id: str):
    result = item_based_recommandation(item_id)
    return {"result": result}