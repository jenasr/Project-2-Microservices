#! /usr/bin/env python
import sqlite3
from typing import List
from microservice1 import Guess
from words import *
from fastapi import FastAPI
from pydantic import BaseModel, BaseSettings

words5 = get_word_list()
words_db = get_database(words5)
#for row in db.execute("SELECT * FROM words"):
#   print(str(row).replace('u\'', '\''))
#class Settings(BaseSettings):
#    database: str
#    
#class Book(BaseModel):
#    id: int
#    word: str
#
#settings = Settings()

app = FastAPI()

db: List[Guess] = [
    Guess(
        id=1, 
        guess="hello"
    ),
    Guess(
        id=2, 
        guess="break"
    ),
    Guess(
        id=3, 
        guess="heart"
    )
]

@app.get("/")
async def fetch_users():
    return db

@app.post("/")
async def register_guess(guess: Guess):
    db.append(guess)