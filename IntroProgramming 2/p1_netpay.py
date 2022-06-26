'''                          
Net Pay
CIS 210 W19 Project 2-1

Author: Edison Mielke

Credits: N/A

Write a Project to determine net pay
'''

def netpay(hours):
    '''
    (int, int)

    Takes hours and multiplies it by the hourrate which is 10.75 which
    makes the hourly pay hourlypay is then multiplied by taxrate making the tax
    finally tax is subtracted by hourly pay making totalpay, which is then returned

    >>>netpay(10)
    91.375
    >>>netpay(40)
    365.5
    >>>netpay(100)
    913.75
    >>>netpay(50)
    456.875
    '''
    TAXRATE = 0.15
    HOURRATE = 10.75
    hourlypay = HOURRATE * hours
    tax = TAXRATE * hourlypay
    totalpay = hourlypay - tax
    return totalpay

def main():
    '''shows net pay in a user friendly format '''
    print('for 10 hours work, net pay is: ', netpay(10))
    print('for 25 hours work, net pay is: ', netpay(25))
    print('for 40 hours work, net pay is: ', netpay(40))
    print('for 100 hours work, net pay is: ', netpay(100))
    return None

main()
