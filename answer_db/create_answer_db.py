#! /usr/bin/env python
import sqlite3
import json
import os.path

"""Loads database of wordle_script answers"""

def get_answers():
    """Loads all answers from wordle_script into list"""
    # Open the wordle answer JSON file
    file = open('answers.json')

    # Load all answers into a list
    data = json.load(file)

    # Create list of answers with following pair (answer, answer_id)
    all_answers = []
    answer_id = 1
    for i, answer in enumerate(data):
        an_answer = (answer, answer_id)
        all_answers.append(an_answer)
        answer_id += 1
    return all_answers

def get_database(list):
    """Creates database of wordle answers"""
    file_exists = os.path.exists('answers.db')
    connection = sqlite3.connect("answers.db")
    cursor = connection.cursor()
    if not file_exists:
        cursor.execute("CREATE TABLE words (game_answers, answer_id PRIMARY KEY)")
        cursor.executemany("INSERT INTO words VALUES(?, ?)", list)
    else:
        print("DB already made")
    return cursor

if __name__ == '__main__':
    wordle_answers = get_answers()
    print(wordle_answers)
    get_database(wordle_answers)
