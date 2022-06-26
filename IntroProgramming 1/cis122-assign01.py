'''
CIS 122 Fall 2018 Assignment 1 
Author: Edison N. Mielke
Description: Introduction to programming problem set uses Python numeric data types and 
operations to solve a variety of small problems.
'''
#Okay, lets do this!

# Question 1
total_hats = 64
cost_red = 10
cost_blue = 5
total_red = total_hats // 2
total_blue = total_hats - total_red
total_blue_cost = total_blue * cost_blue
total_red_cost = total_red * cost_red
total_cost = total_red_cost + total_blue_cost
# Question 1 Part 1: trying to find the total cost for all the hats using python
cost_message = "Total Hat Cost: "
print ("Question 1 Part A")
print(cost_message + str(total_cost))
print()
print()

# 99 bugs in the code, 99 bugs in the code, take one down, patch it around, 112 bugs in the code

# Part B bug fix: Changed total_red = total_hats / 2 to // 2 since we can't do half hats
# Part C To make things more neat I made "Total Hat Cost: " into cost_message
# Afterwards I used the str() command to change total_cost into a string so I can use concatenation
print("_________________________________________")
# Question 2
# My friend believes he takes 100,000 steps per day, I'm going to break down how thats impossible, 1 step at a time
print("Question 2")
target_steps1k = 1000
target_steps10k = 10000
target_steps20k = 20000
target_steps100k = 100000
calling_friend_out = " You need to take"

steps_hour = target_steps1k // 24
steps_min = steps_hour // 60 
steps_sec = steps_min // 60
print("To take" ,target_steps1k,"steps in a day...") 
print(calling_friend_out, steps_hour, "steps per hour.")
print(calling_friend_out, steps_min, "steps per minute.")
print(calling_friend_out, steps_sec, "steps per second.")

print()
steps_hour = target_steps10k // 24
steps_min = steps_hour // 60 
steps_sec = steps_min // 60
print("To take" ,target_steps10k,"steps in a day...") 
print(calling_friend_out, steps_hour, "steps per hour.")
print(calling_friend_out, steps_min, "steps per minute.")
print(calling_friend_out, steps_sec, "steps per second.")

print()
steps_hour = target_steps20k // 24
steps_min = steps_hour // 60 
steps_sec = steps_min // 60
print("To take" ,target_steps20k,"steps in a day...") 
print(calling_friend_out, steps_hour, "steps per hour.")
print(calling_friend_out, steps_min, "steps per minute.")
print(calling_friend_out, steps_sec, "steps per second.")

print()
steps_hour = target_steps100k // 24
steps_min = steps_hour // 60 
steps_sec = steps_min // 60
print("To take" ,target_steps100k,"steps in a day...") 
print(calling_friend_out, steps_hour, "steps per hour.")
print(calling_friend_out, steps_min, "steps per minute.")
print(calling_friend_out, steps_sec, "steps per second.")
print("Dude, you take",steps_sec, "step per second all day? Do you sleep?")
print()
print("_________________________________________")
#Question 3
print("Question 3")
# my friend has to walk around 5 pivots, twice per day, 5 days per week and they each had a radius of 200ft
# ((( 2pi * 200feet radius x 5 pivots) * 2times) * 5days) / 5280feet
pivot_radi = 200
number_of_pivots = 5
inspections = 2
days = 5
mile = 5280
pi = 3.1415926535897932384626
diam = pivot_radi * 2
circum = diam * pi
print("There is " + str(circum) + " feet per pivot.")
farm = circum * number_of_pivots
print()
print("So the farm's pivot systems are " + str(farm) + " feet long.")
print()
feet_day = inspections * farm
weekly_distance_ft = feet_day * days
print("my friend walked " + str(weekly_distance_ft)+" feet.")
print()
weekly_distance = weekly_distance_ft / mile
print("which translates to " + str(weekly_distance)+ " miles")
print()
print("My friend is a liar, first the steps thing and now he walks not even a fifth of what he says he does")
print("geez")
