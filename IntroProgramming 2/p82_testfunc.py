''' 
Test Binary Search
CIS 210 W19 Project 8.2

Author: Edison Mielke

Credits:

Test the isMember function
'''
def isMember(aseq,target):
    '''
    (sequence,element) -> boolean

    Searches if an element is in an ordered sequence and splits the sequence and repeats until an element is found or isnt found

    >>> isMember((1, 2, 3, 3, 4), 4)
    True
    >>> isMember((1, 2, 3, 3, 4), 2)
    True
    >>> isMember('aeiou', 'i')
    True
    >>> isMember('aeiou', 'y')
    False
    >>> isMember((1, 3, 5, 7), 4) #even number of items - False
    False
    >>> isMember((23, 24, 25, 26, 27), 5) #odd number of items - False
    False
    >>> isMember ((0, 1, 4, 5, 6, 8), 4) # even number of items - True
    True
    >>> isMember((0, 1, 2, 3, 4, 5, 6), 3) # odd number of items - True
    True
    >>> isMember((1, 3), 1) # target is first (zeroth) item
    True
    >>> isMember((2, 10), 10) # target is last item 
    True
    >>> isMember((99, 100), 101) # short sequence - False
    False
    >>> isMember((42,), 42) # one item sequence - True
    True
    >>> isMember((43,), 44) # one item sequence - False
    False
    >>> isMember((), 99) # empty sequence
    False
    '''
    result = False
    for item in aseq:

        result = False
        aseqlen = ((len(aseq)//2))
        aseqelem = (aseq[aseqlen])

        if aseqelem == target:
            result = True

        elif aseq[0] > target:
            result = False

        else:
            if aseqelem < target:
                aseq = aseq[aseqlen:(len(aseq))]
            else:
                aseq = aseq[0:aseqlen]
        
    print(result)
    return result

def test_isMember():
    '''
    -> None

    Tests a tuple of various different test cases for isMember
    '''
    testfuncs =(((1, 2, 3, 3, 4), 4, True),((1, 2, 3, 3, 4), 2, True),('aeiou', 'i', True),('aeiou', 'y', False),((1, 3, 5, 7), 4, False),((23, 24, 25, 26, 27), 5, False),((0, 1, 4, 5, 6, 8), 4, True),((0, 1, 2, 3, 4, 5, 6), 3, True),((1, 3), 1, True),((2, 10), 10, True),((99, 100), 101, False),((42,), 42, True),((43,), 44, False),((), 99, False))
    for i in range (len(testfuncs)):
        truefalse = isMember((testfuncs[i][0]),(testfuncs[i][1]))
        if truefalse == testfuncs[i][-1]:
            print("Checking", testfuncs[i][0], "for target", testfuncs[i][1], "... It's value", testfuncs[i][-1] ,"is correct")
        else:
            print("Checking", testfuncs[i][0], "for target", testfuncs[i][1], "... It's value", testfuncs[i][-1] ,"is incorrect")
    return None

def main():
    test_isMember()
    return None
main()
