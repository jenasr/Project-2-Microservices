#! /usr/bin/env python
import sqlite3
import re

def get_word_list():
    all_words = []
    with open("/usr/share/dict/words", "r") as word_file:
        for line in word_file:
            if len(line) == 6:
                word = line.replace("\n","")
                if re.search('[a-z]{5}', word):
                    all_words.append(word)

    offensive_words = []
    with open("offensive.txt", "r") as word_file:
        for line in word_file:
            if len(line) == 6:
                word = line.replace("\n","")
                if re.search('[a-z]{5}', word):
                    offensive_words.append(word)

    five_letter_words = []
    word_ID = 1
    for i, words in enumerate(all_words):
        if words not in offensive_words:
            a_word = (words, word_ID)
            five_letter_words.append(a_word)
            word_ID += 1
    return five_letter_words

def make_database(words5):
    connection = sqlite3.connect("word.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE words (word, number PRIMARY KEY)")
    cursor.executemany("INSERT INTO words VALUES(?, ?)", words5)
    return cursor



