#! /usr/bin/env python3
import sqlite3
import json
import os.path

"""Loads database of wordle_script answers"""

def get_answers():
    """Loads all answers from wordle_script into list1"""
    # Open the wordle answer JSON file
    file = open('answers.json')

    # Load all answers into a list1
    data = json.load(file)

    # Create list1 of answers with following pair (answer, answer_id)
    all_answers = []
    answer_id = 1
    for i, answer in enumerate(data):
        all_answers.append((answer,))
    return all_answers

def get_database(list1):
    """Creates database of wordle answers"""
    file_exists = os.path.exists('answers.db')
    connection = sqlite3.connect("answers.db")
    cursor = connection.cursor()
    if not file_exists:
        cursor.execute("CREATE TABLE words (game_answers CHAR(5), answer_id INTEGER PRIMARY KEY)")
        cursor.executemany("INSERT INTO words VALUES(?, NULL)", list1)
        connection.commit()
    else:
        print("DB already made")
    connection.close()

if __name__ == '__main__':
    wordle_answers = get_answers()
    get_database(wordle_answers)
