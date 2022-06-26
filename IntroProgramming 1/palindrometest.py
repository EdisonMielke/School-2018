#Define Function

def palindrome():

    word = True
    while word:
        word = input("Please input a palindrome, don't be a bitch: ")
        if len(word) == 0:
            break

        #Define punctuation symbols  

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        #unnessecary but useful for checking

        print(word)
        print()

        #check and removes spaces from palindrome

        word = word.replace(" ", "")

        #unnessecary but useful for checking

        print(word)
        print()

        #Check the string for punctuation and remove it

        for i in punctuations:
            word = word.replace(i,"")

        #unnessecary but useful for checking

        print(word)
        print()

        #makes all the letters in the same case

        word = word.lower()

        #unnessecary but useful for checking

        print(word)
        print()

        #check if the end product is the same forwards and backward

        if(word == word[::-1]):

            #If true print "This string is a palindrome

          print("This string is a palindrome")
          print()
        else:

            #If false, insult user

           print("YOU FUCK")
           print()
palindrome()
