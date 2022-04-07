#! /usr/bin/env python3
import sqlite3


if __name__ == '__main__':
    print("Checking")
    connection = sqlite3.connect("answers.db")
    cursor = connection.cursor()
    cur = cursor.execute("SELECT game_answers FROM words")
    output = cur.fetchall()

    for row in output:
        print(str(output).replace('u\'', '\''))

    connection.close()
