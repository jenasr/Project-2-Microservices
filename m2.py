#! /usr/bin/env python3
import collections
import contextlib
import logging.config
import sqlite3
import typing
from fastapi import FastAPI, Depends, Response, HTTPException, status
from pydantic import BaseModel, BaseSettings
from enum import Enum

# connection = sqlite3.connect("games.db")
# cursor = connection.cursor()

class Game(BaseModel):
    word: str
    game_id: int


def get_db():
    with contextlib.closing(sqlite3.connect("answers.db", check_same_thread=False)) as db:
        db.row_factory = sqlite3.Row
        yield db


app = FastAPI()


@app.get("/games/{answer_id}")
async def check_guess(answer_id: int, guess: str, response: Response, db: sqlite3.Connection = Depends(get_db)):
    cur = db.execute("SELECT game_answers FROM games WHERE answer_id = ?", [answer_id])
    looking_for = cur.fetchall()

    if not looking_for:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id not found"
        )
    wordleOfDay = looking_for[0][0]
    if guess == wordleOfDay:
        return {"detail": "Guess is correct!"}
    else:
        color_list = []
        for index, letter in enumerate(guess):
            color = "Gray"
            if wordleOfDay[index] == guess[index]:
                color = "Green"
            else:
                if letter in wordleOfDay:
                    color = "Yellow"
            color_list.append(color)
    return {f"{letter}": f"{color_list[index]}" for index, letter in enumerate(guess)}



@app.put("/games/")
async def change_daily_word(game: Game, response: Response, db: sqlite3.Connection = Depends(get_db)):
    # Make sure word is not in database
    #json object with new games
    # put it to games
    cur = db.execute("SELECT answer_id FROM games WHERE answer_id = ?", [game.game_id])
    looking_for = cur.fetchall()
    if not looking_for:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id not found"
        )
    db.execute("Update games SET game_answers = ? WHERE answer_id = ?", [game.word, game.game_id])
    db.commit()
    return game
