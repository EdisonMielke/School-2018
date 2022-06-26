'''
Class: Cis 123 Lab 4
Author: Edison N. Mielke
Description: make a calendar using Idle
'''
def get_full_month(month):
    if month == 1:
        month =("Janurary")
    elif month == 2:
        month =("Feburary")
    elif month == 3:
        month =("March")
    elif month == 4:
        month =("April")
    elif month == 5:
        month =("May")
    elif month == 6:
        month =("June")
    elif month == 7:
        month =("July")
    elif month == 8:
        month =("August")
    elif month == 9:
        month =("September")
    elif month == 10:
        month =("October")
    elif month == 11:
        month =("November")
    elif month == 12:
        month =("December")
    elif 0 <= month <= 13:
        month =("Must be an integer between 1 and 12 ("+str(month) +") is invalid")
    return print(month)
def test_get_full_month():
    for month in range(14):
        if month == 1:
            month =(str(month) + " Janurary")
            print(month)
        elif month == 2:
            month =(str(month) + " Feburary")
            print(month)
        elif month == 3:
            month =(str(month) + " March")
            print(month)
        elif month == 4:
            month =(str(month) + " April")
            print(month)
        elif month == 5:
            month =(str(month) + " May")
            print(month)
        elif month == 6:
            month =(str(month) + " June")
            print(month)
        elif month == 7:
            month =(str(month) + " July")
            print(month)
        elif month == 8:
            month =(str(month) + " August")
            print(month)
        elif month == 9:
            month =(str(month) + " September")
            print(month)
        elif month == 10:
            month =(str(month) + " October")
            print(month)
        elif month == 11:
            month =(str(month) + " November")
            print(month)
        elif month == 12:
            month =(str(month) + " December")
            print(month)
        elif 0 <= month <= 13:
            month =(str(month) + " Must be an integer between 1 and 12 ("+str(month) +") is invalid")
            print(month)
    return

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("This year is a leap year, it has 366 days")
            else:
                print("This year is not a leap year, it has 365 days")
        else:
            print("This year is a leap year, it has 366 days")
    else:
        print("This year is not a leap year, it has 365 days")

def test_is_leap_year(start_year, end_year):
    for year in range(start_year, end_year + 1):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print(year)
                else:
                    pass
            else:
                print(year)
        else:
            pass
