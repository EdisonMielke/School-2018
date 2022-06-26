'''
Assignment: Cis 122 Lab 07
Author: Edison Mielke
Description: Create a word checking program
'''

def start(word = True):
    while word == True:
        #Prompt for input
        word = input("Enter a search word (blank to exit): ")
        word = word.strip()
        if len(word) == 0:

            break

        else:

            #Perform search
            #print(word)
            #Open file

            fin = open("words_alpha.txt")

            # Search word by looping file

            #count = 0
            #for line in fin:
            #    count = count +1

            #initialize defalt search result to false

            word_found = False

            for line in fin:

                line = line.strip()

                if word.upper() == line.upper():

                    word_found = True

                    break
            # Close file
            fin.close()
            # Print results
            if word_found:
                print("Word, " + word + ", found")
            else:
                print("Word " + word + " not found")
            word = True
start()
