"""This is just a series of functions to show
 exactly how each regex command works"""

import re
print()
print("RE CRASH COURSE")
print()
print('-----------------------------------------------------------------')
print()

def short_regex_methods():


    print("re.findall:")
    print("re.findall Finds all of the matches and returns a list of the matches")
    print("Input: 're.findall('a','The quick brown fox jumped over the lazy dog')")
    output = re.findall("a", "The quick brown fox jumped over the lazy dog")
    print("Output:",output)
    print()
    print()
    print("re.search:")
    print("re.search Finds the first match and then returns a match, useful to find if something exists in a string")
    print("Input: 're.search('a','The quick brown fox jumped over the lazy dog')")
    output = re.search("a", "The quick brown fox jumped over the lazy dog")
    print("Output:",output)
    print()
    print()
    print("re.split:")
    print("re.split splits the string into different strings in a list at the point where a match happens")
    print("Input: 're.split('a','The quick brown fox jumped over the lazy dog')")
    output = re.split("a", "The quick brown fox jumped over the lazy dog")
    print("Output:",output)
    print()
    print()
    print("re.sub Finds all the matches and replaces them with a selected string")
    print("Input: 're.sub('a','The quick brown fox jumped over the lazy dog')")
    output = re.sub("a","aaaaaaaaaa", "The quick brown fox jumped over the lazy dog")
    print("Output:",output)
    print()
    print()
    print('-----------------------------------------------------------------')
    print()
def single_character():
    output = re.findall("a","The quick brown fox jumped over the lazy dog")
    print('Single Character: a')
    print()
    print("Returns a match where the character is present")
    print("Input: 're.findall('a','The quick brown fox jumped over the lazy dog')")
    print("Output:",output)
    print()

def set_of_characters():
    output = re.findall("[lazy]","The quick brown fox jumped over the lazy dog")
    print('[Sets]:')
    print()
    print("Returns a match where one of the specified characters are present")
    print("Input: 're.findall('[lazy]','The quick brown fox jumped over the lazy dog')")
    print("Output:",output)
    print()
    print("It can also be used to find a span of characters")
    output = re.findall("[w-z]", "The quick brown fox jumped over the lazy dog")
    print("Input: 're.findall('[w-z]','The quick brown fox jumped over the lazy dog')")
    print("Output:",output)
    print()

def anycharacter():
    output = re.findall(".","The quick brown fox jumped over the lazy dog")
    print('Any Character: . ')
    print()
    print("Returns a match where any characters are present")
    print("Input: 're.findall('.','The quick brown fox jumped over the lazy dog')")
    print("Output:",output)
    print()
    print()



def metacharacters():
    print("METACHARACTERS & BASICS")
    print()
    print('-----------------------------------------------------------------')
    print()
    single_character()
    set_of_characters()
    anycharacter()

def main():
    short_regex_methods()
    metacharacters()


main()