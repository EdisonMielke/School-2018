'''
Assignment: Cis 122 Assignment 06 Shared Code
Author: Edison N. Mielke
Description: Make the random assignment look nice
'''
def pad_string(phrase,padding_left,padding_right):
    pad_right = padding_right * " "
    pad_left = padding_left * " "
    print(pad_left,phrase,pad_right,end="")
def pad_left(phrase,pad):
    padding = pad * " "
    print(padding + phrase, end="")
def pad_right(phrase,pad):
    padding = pad * " "
    print(phrase+padding, end="")
