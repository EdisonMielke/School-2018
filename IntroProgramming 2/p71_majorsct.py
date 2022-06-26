''' 
Earthquake Watch
CIS 210 W19 Project 7.1

Author: Edison Mielke

Credits: Imported several functions from p51_data_analysis.py

Organize major to practice data analysis
'''

def majors_readf(fname):
    '''
    (txt -> list)

    creates list from a text document
    '''
    dataf=""
    checkf = open(fname,'r')
    dataf = checkf.read()
    checkf.close()
    return dataf.split("\n")

def majors_analysis(majorsli):
    '''
    (list) -> list, int
    
    finds the mode of a list and also finds the amount of unique elements in the list

    >>> majors_analysis(['CIS', 'CIS', 'EXPL', 'COLT', 'EXPL'])
    (['CIS', 'EXPL'], 3)
    >>> majors_analysis(['CIS', 'CIS', 'CIS', 'CIS', 'CIS'])
    (['CIS'], 1)
    '''
    del majorsli[0]
    del majorsli[0]
    countdict = {}

    for item in majorsli:
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

    countdict2 = {}

    for item in majorsli:
        if item in countdict:
            countdict[item] = countdict[item]+1
        else:
            countdict[item] = 1
    
    return (modelist, len(countdict))
def majors_report(majors_mode,majors_ct,majorsli):
    '''
    (list),(int),(list) -> None
    '''
    print(majors_ct, "Majors are represented in CIS 210 this term.")
    print("The most represented major(s):", majors_mode)
    frequencyTable(majorsli)
    return None
def frequencyTable(majorsli):
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
    countdict = genFrequencyTable(majorsli)
    itemlist = list(countdict.keys())
    itemlist.sort()

    print("ITEM","FREQUENCY")

    for item in itemlist:
        print(item, "	 ",countdict[item])
    return None
def genFrequencyTable(majorsli):
    
    '''
    (List/Int) -> Dict

    Counts the occurance of repeated digits

    >>>genFrequencyTable([0])
    {0: 1}
    >>>genFrequencyTable([1,2,3])
    {1: 1, 2: 1, 3: 1}
    '''
    del majorsli[0]
    del majorsli[0]
    countdict = {}
    
    for item in majorsli:
        if item in countdict:
            countdict[item] = countdict[item]+1
        else:
            countdict[item] = 1
    

    print("ITEM","FREQUENCY")
    return(countdict)

def main():
    '''()-> None

    Calls:  majors_readf, majors_analysis, majors_report

    Top level function for analysis of CIS 210 majors data.

    '''
    #fname = 'majors_short.txt'
    fname = 'majors_cis210w19.txt'

    majors_report(majors_analysis(majors_readf(fname))[0],
                  majors_analysis(majors_readf(fname))[1],
                  majors_readf(fname))
    return None
main()
