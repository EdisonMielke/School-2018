'''
Class: Cis 122 Assignment 3 Question 1
Author: Edison N. Mielke
Description: Reverse a string

Extended Summary

Args:
    String "Original: When in the Course of human events" Meant to be reversed

Returns:
    String "Reversed: stneve namuh fo esruoC eht ni nehW" which is the reverse of the original 
'''

def reverse(phrase):
    #initalize variable
    a = ""
    #create a loop to measure the length of the phrase
    for i in range(1, len(phrase) + 1):
        #turns a into the opposite of the phrase
        a = a + phrase[len(phrase) -i]
    return a
print("Original: When in the Course of human events")
print("Reversed: " + (reverse("When in the Course of human events")))

