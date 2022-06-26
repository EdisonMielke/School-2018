'''
Assignment: Cis 122 Assignment 06 Random
Author: Edison N. Mielke
Description: Evaluate a random number file
'''
import os
from cis122_assign06_shared import pad_left, pad_right
find_file = True
while find_file:
    find_file = input("Enter filename (blank to exit): ")
    if find_file == "":
        break
    elif os.path.exists(find_file) == False:
        print("invalid File Name")
    else:
        fin = open(find_file)
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
        pad_right("Count:", 8)
        print(count)
        pad_right("Comments: ", 6)
        print(comment_count)
        pad_right("Total: ", 6)
        print(total)
        pad_right("Average: ", 3)
        print(total/count)
        break
 
