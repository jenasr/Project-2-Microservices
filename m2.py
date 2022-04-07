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
    with contextlib.closing(sqlite3.connect("answers.db", check_same_thread=False)) as db:
        db.row_factory = sqlite3.Row
        yield db

app = FastAPI()
# Statelessness
    # We should be able to change the answer of the day
    # But we never save it, that is clients job
# unifying the microservices: do we put them in the same file?
# how do I pass multiple arguments to the endpoint
# Posting if the word already exists, do just use primary key, since that is unique
@app.get("/games/{answer_id}")
async def check_guess(answer_id: int, guess: str, response: Response, db: sqlite3.Connection = Depends(get_db)):
    cur = db.execute("SELECT game_answers FROM words WHERE answer_id = ?", [answer_id])
    looking_for = cur.fetchall()

    if not looking_for:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id not found"
        )

    wordleOfDay = looking_for[0]
    #for guess in guessesList:
        #Checking all valid guesses against the answer for the current day.
    if guess == wordleOfDay:
        return "Guess is correct!"
        #If the guess is incorrect, the response should identify the letters that are:
    else:
      # single out each v, letter is index
        letter_list;
        for letter, v in enumerate(guess):
            found = 0
                #in the word and in the correct spot,
            if wordleOfDay[letter] == guess[letter]:
                found += 1
                letter_list.append("Letter is Green: " + v)
                #in the word but in the wrong spot, and
            else:
              # single out each v, char is index
                for char in wordleOfDay:
                    #print(char)
                    if char == guess[letter]:
                        found += 1
                        letter_list.append("Letter is Yellow: " + v)
                #not in the word in any spot
                if found < 1:
                    letter_list.append("Letter is Gray: " + v)
        #Changing the answers for future games.
    # fetchall returns a list

        # if not (empty list)  = true
    return {letter: letter_list[index] for index, letter in enumerate(guess)}

@app.put("/games/{answer_id}")
async def change_daily_word(letters: str, response: Response, db: sqlite3.Connection = Depends(get_db)):
    # Make sure word is not in database
    #json object with new words
    # put it to games

    cur = db.execute("SELECT answer_id FROM words WHERE answer_id = ?", [answer_id])
    looking_for = cur.fetchall()

    if not looking_for:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id not found"
        )
    #Check to make sure if its unique
    db.execute("Update words SET answer_id = ? WHERE word = ?", [answer_id, word])
    db.commit()
    return {"Successfully updated": answer_id}
