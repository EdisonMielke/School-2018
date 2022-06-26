'''
Class: Cis 123 Assignment 4
Author: Edison N. Mielke
Description: calculate year and day
'''

def valid_year(year):
    
    if year >= 1:
        return year
    else: 
        return print("Please input valid year")
'''
This checks if the year is greater than 1 so it could be valid
'''
def valid_day_of_year(days,day_check):
    
    if (0 <= days <= day_check):
        return True
    else:
        return print("Please input valid day") and False

'''
This checks the day to make sure its between 0 and 365 (366 if its a leap year)
'''
def input_year():
    year_input = int(input("Enter year: "))
    return year_input
'''
This records the year input from the end user
'''
def input_day_of_year(total):
    if total == 366:
        days = int(input("Enter a day between 1 and 366: "))
    else:
        days = int(input("Enter a day between 1 and 365: "))
    return days
'''
this records the input of the day the end user puts in
'''
def get_days_in_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                total_year = 366
            else:
                total_year = 365
        else:
            total_year = 366
    else:
        total_year = 365
    return total_year
'''
this checks and sees if the year is a leap year and acts accordingly
'''
def valid_month(month):
    0<month<=12
'''
this checks whether or not the months are valid
'''
def translate_month():
    if month < 1:
        print("Invalid month")
    elif month > 12:
        print("Invalid month")
'''
This translates the month error
'''
def get_days_in_month(year,month):
    pass
'''
I could not impliment this into my coding structure
'''
def valid_day():
    pass
'''
This was already built into another function
'''
def get_month_leap_year(day):
    if day <= 31:
          month = "Janurary "
    elif day <= 50:
          month = "February "
          day = day - 31
    elif day <= 81:
          month = "March "
          day = day - 50
    elif day <= 121:
          month = "April "
          day = day - 81
    elif day <= 152:
          month = "May "
          day = day - 121
    elif day <= 182:
          month = "June "
          day = day - 151
    elif day <= 213:
          month = "July "
          day = day - 182
    elif day <= 244:
          month = "August "
          day = day - 213
    elif day <= 274:
          month = "September "
          day = day - 244
    elif day <= 305:
          month = "October "
          day = day - 274
    elif day <= 335:
          month = "November "
          day = day - 305
    elif day <= 366:
          month = "December "
          day = day - 335
    return (str(month)',' + str(day))
'''
this records the values for each month for a leap year
'''
def get_month(day):
    if day <= 31:
          month = "Janurary "
    elif day <= 49:
          month = "February "
          day = day - 31
    elif day <= 80:
          month = "March "
          day = day - 49
    elif day <= 120:
          month = "April "
          day = day - 80
    elif day <= 151:
          month = "May "
          day = day - 120
    elif day <= 181:
          month = "June "
          day = day - 150
    elif day <= 212:
          month = "July "
          day = day - 181
    elif day <= 243:
          month = "August "
          day = day - 212
    elif day <= 273:
          month = "September "
          day = day - 243
    elif day <= 304:
          month = "October "
          day = day - 273
    elif day <= 334:
          month = "November "
          day = day - 304
    elif day <= 365:
          month = "December "
          day = day - 334
    return (str(month)',' + str(day))
'''
this records values for each month on a normal year
'''
def start():
    year=input_year()
    x=(get_days_in_year(valid_year(int(year))))
    y = input_day_of_year(x)
    valid_day_of_year(y,x)
    if x == 366:
        print(get_month_leap_year(y), year)
    else:
        print(get_month(y), year)
'''
this finally runs the whole thing
'''
start()
