'''
Assignment: Cis 122 Lab 07 Part II
Author: Edison N. Mielke
Description: Get the statistics of a file
'''
#Initializing several variables
fin = open("words_alpha.txt")
longer_word = ""
shorter_word = "qwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewq"
palindrome_count = 0
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
count = 0

#Scans list to find the longest word, shortest word and count
list_of_lines = fin.readlines()
for line in list_of_lines:
        #counts lines
    count = count + 1
    #finds longest word
    if int(len(line)) > int(len(longer_word)):
        longer_word = line
    #finds shortest word
    if int(len(line)) < int(len(shorter_word)):
        shorter_word = line
#finds palindromes
for palindrome in list_of_lines:
    #strips lines
    palindrome = palindrome.strip()
    #checks to see if the first and last letter are the same
    if palindrome[0] == palindrome[-1]:
        #if first and last letter are the same convert to string (I don't know why, it just required it)
        palindrome = str(palindrome)
        #make all letters the same case
        palindrome = palindrome.lower()
        #replace any spaces with blank space
        palindrome = palindrome.replace(" ", "")
        #replaces punctuation with blank space
        for i in punctuations:
            palindrome = palindrome.replace(i,"")
        #if after all that the letters are the same forwards and back the counter counts up
        if palindrome == palindrome[::-1]:
            palindrome_count = palindrome_count +1

def letters(input_letter):
    letter_count = 0
    for letter in list_of_lines:
        if letter[0] == str(input_letter):
            letter_count += 1
    print(input_letter.upper()+": " + str(letter_count), "(",round(((letter_count/count)*100), 2),"%)")
    
print("Word Count:",count)
print()
print("The longest word is"+longer_word+"("+str(len(longer_word))+")")
print()
print("The shortest word is",shorter_word+"("+str(len(shorter_word))+")")
print()
print("There are",palindrome_count,"Palindromes", "(",round(((palindrome_count/count)*100), 2),"%)")
print()
letters("a")
letters("b")
letters("c")
letters("d")
letters("e")
letters("f")
letters("g")
letters("h")
letters("i")
letters("j")
letters("k")
letters("l")
letters("m")
letters("n")
letters("o")
letters("p")
letters("q")
letters("r")
letters("s")
letters("t")
letters("u")
letters("v")
letters("q")
letters("r")
letters("s")
letters("t")
letters("u")
letters("v")
letters("w")
letters("x")
letters("y")
letters("z")
