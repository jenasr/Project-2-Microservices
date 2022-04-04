#! /usr/bin/env python
import sqlite3
import os.path
from words import *

file_exists = os.path.exists('word.db')
words5 = get_word_list()

if(file_exists):
    print("DB already made")
else:
    new_cursor = make_database(words5)
    for row in new_cursor.execute("SELECT * FROM words"):
        print(str(row).replace('u\'', '\''))
    print("DB made")
    
#connection.close()
