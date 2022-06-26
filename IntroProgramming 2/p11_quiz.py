''' 
CIS 210 STYLE
CIS 210 W19 Project 1-1

Author: Edison Mielke

Credits: N/A

'''

def q1(onTime, absent):
    '''
    Type:
        Boolean

    Description:
        Function that checks if a variable "onTime" is true
        if "onTime" Is true it returns "Hello!",
        however if it is false it checks "absent"
        If Absent is true returns "Is anyone there?"
        But if absent is false it returns "Better late than never."

    Use:
        >>> q1(1, 0)
        'Hello!'
        >>> q1(0, 0)
        'Better late than never.'
    '''
    if onTime:
        return('Hello!')
    elif absent:
        return('Is anyone there?')
    else:
        return('Better late than never.')

def q2(age, salary):
    '''
    Type:
        Boolean

    Description:
    
        Checks if "age" is below 18, and checks if "salary" is below 10000
        if both are true, it returns true
        if either are false, it returns false

    Use:
        >>> q2(20, 53000)
        False
        >>> q2(10, 100)
        True
        >>> q2(15, 20000)
        False
    '''
    return (age < 18) and (salary < 10000)

def q3():
    '''
    Types:
        Integer
        Boolean
        
    Description:
        Sets p to 1, q to 2 and sets result to 4
        if p < q then the second boolean activates
        if q > 4 then result = 5 else result will = 6

    Use:
        >>> q3()
        result = 6
    '''
    p = 1
    q = 2
    result = 4
    if p < q:
        if q > 4:
            result = 5
        else:
            result = 6

    return result

def q4(balance, deposit):
    '''
    Types:
        Loop
        Integer

    Description:
        Inputs balance and deposits
        Sets count equal to 0 and preforms a while loop for while count is
        less than 0
        while the while loop is going on balance is being added to deposit
        count adds 1 each time until 10 and then the while loop ends

    Use:
        >>> q4 (10, 10)
        110
    '''
    count = 0
    while count < 10:
        balance = balance + deposit
        count += 1

    return balance

def q5(nums):
    '''
    Types:
        Loops
        Boolean
        Integers

    Description:
        Takes input "nums"
        sets result and i to 0 and loops i = 0 while i is less than length of nums
        while the while loop exists i is equal to i + 1
        if nums[i] is greater than or equal to 0 the result is going to add 1 each time it loops
        returns result

    Use:
        Program is nonfunctional
    
    '''
    result = 0
    i = 0
    while i < len(nums):
        if nums[i] >= 0:
            result += 1

        i += 1

    return result

def q6():
    '''
    Types:
        Loops
        Integers

    Description:
        Sets i equal to 0 and p equal to 1
        while loops while i is less than 4
        i is set equal to 1 while it loops (REMOVED)
        p doubles each loop
        i adds 1 every loop
        prints p

    Use:
        >>>q6)
        16
    
    Original:
    i = 0
    p = 1
    while i < 4:
        i = 1
        p = p * 2
        i += 1

    return p

    '''
    i = 0
    p = 1
    while i < 4:
        p = p * 2
        i += 1

    return p
