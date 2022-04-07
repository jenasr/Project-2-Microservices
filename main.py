#! /usr/bin/env python3
import collections
import contextlib
import logging.config
import sqlite3
import typing
from fastapi import FastAPI, Depends, Response, HTTPException, status
from pydantic import BaseModel, BaseSettings
from enum import Enum

# connection = sqlite3.connect("words.db")
# cursor = connection.cursor()


def get_db():
    with contextlib.closing(sqlite3.connect("words.db", check_same_thread=False)) as db:
        db.row_factory = sqlite3.Row
        yield db


app = FastAPI()
# Statelessness
    # We should be able to change the answer of the day
    # But we never save it, that is clients job
# unifying the microservices: do we put them in the same file?
# how do I pass multiple arguments to the endpoint
# Posting if the word already exists, do just use primary key, since that is unique
@app.get("/words/{letters}")
async def valid_word(letters: str, response: Response, db: sqlite3.Connection = Depends(get_db)):
    cur = db.execute("SELECT word FROM words WHERE word = ?", [letters])
    looking_for = cur.fetchall()
    # fetchall returns a list
    if not looking_for:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Word not found"
        )
        # if not (empty list)  = true
    return {"word": looking_for[0][0]}

@app.post("/words/{letters}")
async def add_guess(letters: str, response: Response, db: sqlite3.Connection = Depends(get_db)):
    # Make sure word is not in database
    cur = db.execute("SELECT word FROM words WHERE word = ?", [letters])
    # its list
    looking_for = cur.fetchall()
    # fetchall returns a list
    if looking_for:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Word already exists"
        )
    #Check to make sure if its unique
    db.execute("INSERT INTO words VALUES(?)", [letters])
    db.commit()
    return {"Successfully added": letters}

@app.delete("/words/{letters}")
async def delete_guess(letters: str, response: Response, db: sqlite3.Connection = Depends(get_db)):
    # Make sure word is not in database
    cur = db.execute("SELECT word FROM words WHERE word = ?", [letters])
    looking_for = cur.fetchall()
    # fetchall returns a list
    if not looking_for:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Word not found"
        )
    # Don't have to check
    # check return value of execute
    db.execute("DELETE FROM words WHERE word = ?", [letters])
    db.commit()
    return {"Successfully removed": letters}
