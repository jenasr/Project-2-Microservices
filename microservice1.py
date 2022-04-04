#! /usr/bin/env python
import sqlite3
from words import *

words5 = get_word_list()
db = get_database(words5)

for row in db.execute("SELECT * FROM words"):
   print(str(row).replace('u\'', '\''))
   