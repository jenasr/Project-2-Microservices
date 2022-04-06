# importing the module
#import sqlite3
  
# connect withe the myTable database
#connection = sqlite3.connect("gfg.db")
  
# cursor object
#guessesDB = connection.cursor()
  
# execute the command to fetch all the data from the table emp
#guessesDB.execute("SELECT * FROM emp")
  
# store all the fetched data in the ans variable
#guessesList = guessesDB.fetchall()
  
# Since we have already selected all the data entries
# using the "SELECT *" SQL command and stored them in
# the ans variable, all we need to do now is to print
# out the ans variable
#for i in guessesList:
#    print(i)

#Wordle of the day
wordleOfDay = "great"
guess = "grape"
#for guess in guessesList:
    #Checking all valid guesses against the answer for the current day.
if guess == wordleOfDay:
    print("Guess is correct!")
    #If the guess is incorrect, the response should identify the letters that are:
else:
  # single out each v, letter is index
    for letter, v in enumerate(guess):
        found = 0
            #in the word and in the correct spot,
        if wordleOfDay[letter] == guess[letter]:
            found += 1
            print("Letter is Green: " + v)
            #in the word but in the wrong spot, and
        else:
          # single out each v, char is index
            for char in wordleOfDay:
                #print(char)
                if char == guess[letter]:
                    found += 1
                    print("Letter is Yellow: " + v)
            #not in the word in any spot
            if found < 1:
                print("Letter is Gray: " + v)
    #Changing the answers for future games.
