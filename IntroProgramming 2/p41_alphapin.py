''' 
Alphapin Encoding/Decoding
CIS 210 W19 Project 4.1

Author: Edison Mielke

Credits: N/A

Description: Encode and Decode pins
'''

import math
def alphabetCon(num):
    '''
    (int) -> str

    changes a number to a cooresponding vowel

    >>> alphabetCon (1)
    c
    '''
    final = -1
    if num == 0:
        final = 'b'
    if num == 1:
        final = 'c'
    elif num == 2:
        final = 'd'
    elif num == 3:
        final = 'f'
    elif num == 4:
        final = 'g'
    elif num == 5:
        final = 'h'
    elif num == 6:
        final = 'j'
    elif num == 7:
        final = 'k'
    elif num == 8:
        final = 'l'
    elif num == 9:
        final = 'm'
    elif num == 10:
        final = 'n'
    elif num == 11:
        final = 'p'
    elif num == 12:
        final = 'q'
    elif num == 13:
        final = 'r'
    elif num == 14:
        final = 's'
    elif num == 15:
        final = 't'
    elif num == 16:
        final = 'v'
    elif num == 17:
        final = 'w'
    elif num == 18:
        final = 'x'
    elif num == 19:
        final = 'y'
    elif num == 20:
        final = 'z'
    return final
def alphabetVowel(num):
    '''
    (int) -> str

    changes a number to a cooresponding vowel

    >>> alphabetVowel (1)
    e
    '''
    final = -1
    if num == 0:
        final = 'a'
    elif num == 1:
        final = 'e'
    elif num == 2:
        final = 'i'
    elif num == 3:
        final = 'o'
    elif num == 4:
        final = 'u'
    return final

def numerVowel(vow):
    '''
    (str) -> int

    changes a vowel to a corresponding number

    >>> numerVowel(a)
    0
    '''
    final = -1
    if vow == 'a':
        final = 0
    elif vow == 'e':
        final = 1
    elif vow == 'i':
        final = 2
    elif vow == 'o':
        final = 3
    elif vow == 'u':
        final = 4
    return final 
def numerCon(con):
    '''
    (str) -> int

    changes a consenant to a corresponding number

    >>> numerCon(b)
    0
    '''
    final = -1
    if con == 'b':
        final = 0
    elif con == 'c':
        final = 1
    elif con == 'd':
        final = 2
    elif con == 'f':
        final = 3
    elif con == 'g':
        final = 4
    elif con == 'h':
        final = 5
    elif con == 'j':
        final = 6
    elif con == 'k':
        final = 7
    elif con == 'l':
        final = 8
    elif con == 'm':
        final = 9
    elif con == 'n':
        final = 10
    elif con == 'p':
        final = 11
    elif con == 'q':
        final = 12
    elif con == 'r':
        final = 13
    elif con == 's':
        final = 14
    elif con == 't':
        final = 15
    elif con == 'v':
        final = 16
    elif con == 'w':
        final = 17
    elif con == 'x':
        final = 18
    elif con == 'y':
        final = 19
    elif con == 'z':
        final = 20     
    return final
def alphapinEncode(pin):
    '''
    (int) -> str

    Takes a integer and checks if it is first even or odd, afterwards breaks it up
    into groups of 2 and then calls functions "alphabetcon" and "alphabetvowel" to
    convert into letters

    >>> alphapinEncode(4327)
    'lohi'
    >>> alphapinEncode(1298)
    'diyo'
    >>> alphapinEncode(3464140)
    'bomelela'
    >>> alphapinEncode(9995455)
    'cuyunupa'
    >>> alphapinEncode(3464408)
    'bomeluco'
    '''

    pinlength = len(str(pin))
    encodednumber = ""
    for i in range(math.ceil(pinlength/2)):

        i=i+1

        if pinlength % 2 == 0:    

            firstdigit = str(pin)[2*i-2] 

            seconddigit = (str(pin)[2*i - 1])

        else:

            firstdigit = str(pin)[2*i-3]

            seconddigit = str(pin) [2*i - 2]

            if i == 1:

                seconddigit = ""
        
        if i == 1:

            firstdigit = str(pin)[0]
            
        alphacode = firstdigit + seconddigit

        alphacode = int(alphacode)
        consenant = alphacode // 5
        vowel = alphacode % 5
        encodednumber = (encodednumber+alphabetCon(consenant)+alphabetVowel(vowel))

    print(encodednumber)
    print(pin)
        
    return

def checkTone(tone):
    '''
    (str) -> bool

    checks if a phrase is an encoded number

    >>>checkTone(dasa)
    True
    >>>checkTone(aaaa)
    False
    '''

    for i in range(math.ceil(len(tone)/2)):

        i=i+1

        if len(tone) % 2 == 0:

            firstdigit = str(tone)[2*i-2]
            seconddigit = (str(tone)[2*i - 1])
            consenant = (numerCon(firstdigit))
            vowel = (numerVowel(seconddigit))

            if 0 <= consenant <=20:

                if 0 <= vowel <= 4:

                    result = True
                else:
                    result = False
            else:       
                result = False
        else:
            result = False       
    return result

def alphapinDecode(tone):
    '''
    (str) -> int

    takes a series of letters and calls checkTone to make sure it is compatible
    and then takes the letters, converts them through numerCon and Vowel functions
    and then converts them to the original integers

    >>>alphapinDecode('popo')
    5858
    >>>alphapinDecode('make')
    4536
    >>>alphapinDecode('makefa')
    453615
    '''
    merge = ''
    if checkTone(tone) == False:
        print("Tone is in invalid format.")
        pass
    for i in range (math.ceil(len(tone)/2)):
        i=i+1
        
        if len(tone) % 2 == 0:    

            firstdigit = str(tone)[2*i-2] 

            seconddigit = (str(tone)[2*i - 1])
            
        if i == 1:

            firstdigit = str(tone)[0]

        consenant = numerCon(firstdigit)
        vowel = numerVowel(seconddigit)
        merge = merge + str((consenant*5) + vowel)
    merge = int(merge)
    return merge

def main():
    encoding = input("What number would you like to encode?")
    alphapinEncode(encoding)
main()
        


        

        
