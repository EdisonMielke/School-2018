import re

def validate_email(email: str) -> bool:
    '''Validates your Email to see if it does not start with a number, if it ends with .com or .edu and if there is exactly ONE @ symbol'''
    digitcheck = re.findall("^[0-9]", email)
    com_or_edu = re.findall("\.com|\.edu", email)
    atcheck = re.findall("@+", email)
    if len(digitcheck) == 0:
        if len(com_or_edu) == 1:
            if len(atcheck) == 1:
                print("Email Accepted!")
                return True
            else:
                print("You have to have only ONE @ symbol!")
        else:
            print("Your email must end in '.com' or '.edu'!")
    else:
        print("You cannot start with a number!")
    return False

def validate_password(password: str) -> bool:
    '''Validates your password to see if it is 10 charracters long with at least 1 number and special character'''
    passlen = re.findall("^.{10,}", password)
    if len(passlen) > 0:
        passlen = passlen[0]
    else:
        print("Password has to be at least '10' Characters long!")
        return False
    digits = re.findall("[0-9]", passlen)
    specialchars = re.findall("[^\w]", passlen)
    if len(digits) > 0:
        if len(specialchars) > 0:
            print("Password Accepted!")
            return True
        else:
            print("Password must contain at least 1 special character")
    else:
        print("Password must contain at least 1 number!")
    return False

def main():
    '''Loops validate_email and validate_password to check if they are good'''
    emailcheck = False
    passcheck = False
    while emailcheck == False:
        email = input("Please input your Email: ")
        if validate_email(email) == True:
            emailcheck = True
    while passcheck == False:
        password = input("Please input your Password: ")
        if validate_password(password) == True:
            passcheck = True
    print("Sign-Up Successful!")

main()
