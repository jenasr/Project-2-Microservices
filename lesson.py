#! /usr/bin/env python3
import sqlite3


if __name__ == '__main__':
    print("Checking")
    connection = sqlite3.connect("answers.db")
    cursor = connection.cursor()
    for row in cursor.execute("SELECT game_answers FROM words"):
        print(str(row).replace('u\'', '\''))
    connection.commit()
    connection.close()
