'''
CIS 122 Fall 2018 Assignment 2 Travel
Author: Edison N. Mielke
Description: create functions to calculate travel time in minutes
https://www.calculatorsoup.com/calculators/math/speed-distance-time-calculator.php
'''
#110 miles distance
#test using 60mph and 70mph
#test travel 5 miles at 25mph and 45mph

#I screwed this up hard, I brute forced through this and found out I was supposed
#to use 2 functions afterwards, I thought I had to use 1
def calc_travel_time(miles,speed):
    minu = miles/speed
    minu = minu * 60

    #checks to see if we go above 60 minutes
    if minu < 60:
        
        if (minu % 1) == 0:
            minu = (int(minu))
            minu_sec2 = "0"
        if (minu % 1) > 0:
            
            minu_sec2 = str(int((minu % 1)/10 * 6 * 100))
            minu = (int(minu))
            
    #Creating hour and second command
            
    if minu > 60:

        minu_sec = (minu - 60)
        
        #I hate this so much, I am so sorry
        #mostly it checks if there exists any floats and converts it to seconds
        
        if (minu_sec % 1) == 0:
                minu_sec2 = (int(minu_sec))
        minu = "1 hour " + (str(int(minu_sec)))
        minu_sec2 = minu_sec % 1
        minu_sec2 = (minu_sec2) /10 * 6 * 100
        minu_sec2 =str(int(minu_sec2))
        
#prints the surpisingly working time of arrival
        
    print("To travel " + (str(miles)) + " miles at " + (str(speed)) + "MPH will take" ,minu, "minutes and " + minu_sec2 + " seconds.")
#Space
    print()
    
    return

calc_travel_time(110,60)
calc_travel_time(110,70)
calc_travel_time(5,25)
calc_travel_time(5,45)



    
