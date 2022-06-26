'''
Class: Cis122 Lab 05
Author: Edison N. Mielke
Description: create a program that accepts test scores and outputs information about the scores
'''

def start():
    score = True
    count = 0
    max_score = 0
    total_score = 0
    min_score = 100
    while score:
        score = input("Enter Score: ")
        if (score) == (''):
            break
        if not 0 < int(score) < 101:
            score = False
            print("Invalid Entry")
        if (score) == True:
            print(score)
        total_score = int(total_score) + int(score)
        if int(score) > int(max_score):
           max_score = score
        if int(score) < int(min_score):
           min_score = score
        count = count + 1
        print(count)
    if count > 0:
        print()
        print("Total score is equal to: ")
        print(total_score/count)
        print("The High score was: ")
        print(max_score)
        print("The low score was: ")
        print(min_score)
    else:
        return 0
    
start()
