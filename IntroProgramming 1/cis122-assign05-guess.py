'''
Assignment: Cis 122 Assignment 5
Author: Edison N. Mielke
Description: Make a game of hangman!
'''
def Hangman(lifes=True):
    gametime = True
    guess_word = input("Enter Guess Word (Blank to quit)")
    guess_count = 0
    while lifes:
        if len(guess_word) == 0:
            break
            while gametime:
                letter = input("Enter a Guess Letter: ")
                if (letter):
                    
                if len(letter) == 0:
                        break
                else:
                    if len(letter) > 1:
                        print("Invalid guess, try again!")


    if len(guess_word) > 0:
        print("")
        print("***RESULTS***")
        print("Word: " + guess_word)
        #print("Matched: " + )
        #print ("Guesses: " + )
    print("Thanks for Playing!")
Hangman()
