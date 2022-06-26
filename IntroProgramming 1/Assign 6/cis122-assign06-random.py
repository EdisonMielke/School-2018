'''
Assignment: Cis 122 Assignment 06 Random
Author: Edison N. Mielke
Description: Evaluate a random number file
'''
fin = open("random_numbers.txt")
count = 0
list_of_numbers = fin.readlines()
total = 0
comment_count = 0
for num in list_of_numbers:
    if num[0] != "#":
        count = count + 1
        num = int(num)
        total += num
    else:
        comment_count = comment_count + 1
print ("Count: ",count)
print ("Comments: ",comment_count)
print ("Total: ",total)
print ("Average: ",total/count)
