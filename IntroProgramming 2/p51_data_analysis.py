'''
CIS 210 W19 Project 5.1

Author: Edison Mielke

Credits: Python Programming in Context, 2nd Edition

Description: understand, impliment and revise data analysis functions.
'''
import doctest
doctest.testmod()
def mean(alist):
    '''
    (list) -> float

    finds the mean from a list of numbers

    >>>mean([0])
    0.0
    >>>mean([0,0,0,0,0,0])
    0.0
    >>>mean([1,2,3,4,5])
    3.0
    '''
    mean = sum(alist) / len(alist)
    return mean
def isEven(n):
    '''
    (int/list) -> bool

    checks to see if a number or if the elements of a list are even.

    >>>isEven(0)
    True
    >>>isEven(100)
    True
    '''
    even =''
    if n % 2 !=0 or n % 2 !=1:
        if (n % 2) == 0:
            even = "Even"
        elif (n % 2) == 1:
            even = "Odd"    
    else:
        even = "Not Even or Odd"
    return even

def median(alist):
    '''
    (int/list) -> int,str

    checks to see the median of a number and calls isEven to check if it is even or odd

    >>>median([0])
    (0, 'Even')
    >>>median([1,2,3])
    (2, 'Even')
    >>>median([1,2,3,4,5])
    (3, 'Odd')
    '''
    even = ''
    copylist = alist[:]#make  a  copy  using  slice  operator
    copylist.sort()
    if len(copylist)%2 == 0:#even  length
        rightmid = len(copylist)//2
        leftmid = rightmid  - 1
        median = (copylist[leftmid] + copylist[rightmid])/2
    else:#odd  length
        mid = len(copylist)//2
        median = copylist[mid]
        even = isEven(median)
    return median,even
def mode(alist):
    '''
    (int/list) -> int

    determines most common number

    >>>mode([0])
    [0]
    >>>mode([0,1,2,3])
    [0, 1, 2, 3]
    >>>mode([0,1,2,2])
    [2]
    >>>mode([0,0,1,1])
    [0, 1]
    '''
    countdict = {}

    for item in alist:
        if item in countdict:
            countdict[item] = countdict[item]+17
        else:
            countdict[item] = 1
    countlist = countdict.values()
    maxcount = max(countlist)

    modelist = [ ]
    for item in countdict:
        if countdict[item] == maxcount:
            modelist.append(item)
    return modelist

def frequencyTable(alist):
    '''
    (int/list) -> int

    counts the frequency of certain numbers by calling
    genFrequencyTable

    >>>frequencyTable([0])
    ITEM FREQUENCY
    0         1
    >>>frequencyTable([0,1,2])
    ITEM FREQUENCY
    0         1
    1         2
    2         3
    >>>frequencyTable([0,0,0])
    ITEM FREQUENCY
    0         3
    '''
    
    countdict = genFrequencyTable(alist)
    itemlist = list(countdict.keys())
    itemlist.sort()

    print("ITEM","FREQUENCY")

    for item in itemlist:
        print(item, "	 ",countdict[item])
    return None
def genFrequencyTable(alist):
    '''
    (List/Int) -> Dict

    Counts the occurance of repeated digits

    >>>genFrequencyTable([0])
    {0: 1}
    >>>genFrequencyTable([1,2,3])
    {1: 1, 2: 1, 3: 1}
    '''
    countdict = {}

    for item in alist:
        if item in countdict:
            countdict[item] = countdict[item]+1
        else:
            countdict[item] = 1
    return(countdict)

def main(equakes):
    mean(equakes)
    print()
    median(equakes)
    print()
    mode(equakes)
    print()
    frequencyTable(equakes)
main([5.3, 3.0, 2.6, 4.4, 2.9, 4.8, 4.3, 2.6, 2.9, 4.9, 2.5, 4.8, 4.2, 2.6, 4.8, 2.7, 5.0, 2.7, 2.8, 4.3, 3.1, 4.1, 2.8, 5.8, 2.5, 3.9, 4.8, 2.9, 2.5, 4.9, 5.0, 2.5, 3.2, 2.6, 2.7, 4.8, 4.1, 5.1, 4.7, 2.6, 2.9, 2.7, 3.3, 3.0, 4.4, 2.7, 5.7, 2.5, 5.1, 2.5, 4.4, 4.6, 5.7, 4.5, 4.7, 5.1, 2.9, 3.3, 2.7, 2.8, 2.9, 2.6, 5.3, 6.0, 3.0, 5.3, 2.7, 4.3, 5.4, 4.4, 2.6, 2.8, 4.4, 4.3, 4.7, 3.3, 4.0, 2.5, 4.9, 4.9, 2.5, 4.8, 3.1, 4.9, 4.4, 6.6, 3.3, 2.5, 5.0, 4.8, 2.5, 4.2, 4.5, 2.6, 4.0, 3.3, 3.1, 2.6, 2.7, 2.9, 2.7, 2.9, 3.3, 2.8, 3.1, 2.5, 4.3, 3.2, 4.6, 2.8, 4.8, 5.1, 2.7, 2.6, 3.1, 2.9, 4.2, 4.8, 2.5, 4.5, 4.5, 2.8, 4.7, 4.6, 4.6, 5.1, 4.2, 2.8, 2.5, 4.5, 4.6, 2.6, 5.0, 2.8, 2.9, 2.7, 3.1, 2.6, 2.5, 3.2, 3.2, 5.2, 2.8, 3.2, 2.6, 5.3, 5.5, 2.7, 5.2, 6.4, 4.2, 3.1, 2.8, 4.5, 2.9, 3.1, 4.3, 4.9, 5.2, 2.6, 6.7, 2.7, 4.9, 3.0, 4.9, 4.7, 2.6, 4.6, 2.5, 3.2, 2.7, 6.2, 4.0, 4.6, 4.9, 2.5, 5.1, 3.3, 2.5, 4.7, 2.5, 4.1, 3.1, 4.6, 2.8, 3.1, 6.3])
