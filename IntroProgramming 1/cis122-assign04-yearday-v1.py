'''
Class: Cis 123 Assignment 4
Author: Edison N. Mielke
Description: calculate year and day
'''
#check if leap year
def is_leap_year(year):
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
This function checks if your year is a leap year
'''
#Prompt user for year
year_input = int(input("Enter Year: "))
#record year time
if(is_leap_year(year_input)) == 366:
    #prompt user for day
    day = int(input("Enter a number between 1 and 366: "))
    #record day
    #assign number range for each month
    if day == 0:
          print("Day not Supported")
    elif day <= 31:
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
    elif day > 366:
        print("Unsupported date, please enter a number between 1 and 366.")
    
else:
    #assign alternate number range for each month for non leap years
    #prompt user for day
    print(is_leap_year(year_input))
    #record day
    day = int(input("Enter a number between 1 and 365: "))
    if day == 0:
          print("Day not Supported")
    elif day <= 31:
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
    elif day > 365:
        print("Unsupported date, please enter a number between 1 and 365.")
#get everything together
#print all to user
print(month +str(day)+", "+ str(year_input))
