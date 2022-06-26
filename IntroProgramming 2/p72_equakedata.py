''' 
Earthquake Watch
CIS 210 W19 Project 7.2

Author: Edison Mielke

Credits: N/A

Practice Data Analysis by organizing the earthquake data
'''
def equake_readf(fname):
    '''
    (txt -> list)

    creates list from a text document
    '''
    dataf=""
    checkf = open(fname,'r')
    dataf = checkf.read()
    checkf.close()
    print(dataf.split('\n'))
    for i in dataf:
        countdict = dataf.split('\n')[i]
    return dataf.split(",")
    
def equake_analysis(magnitudes):
    '''
    (list) -> list, int
    
    finds the mode of a list and also finds the amount of unique elements in the list

    >>> majors_analysis(['CIS', 'CIS', 'EXPL', 'COLT', 'EXPL'])
    (['CIS', 'EXPL'], 3)
    >>> majors_analysis(['CIS', 'CIS', 'CIS', 'CIS', 'CIS'])
    (['CIS'], 1)
    '''
    print(magnitudes)
    countdict = {}

    for item in magnitudes:
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
    print(modelist)
    countdict2 = {}

    for item in magnitudes:
        if item in countdict:
            countdict[item] = countdict[item]+1
        else:
            countdict[item] = 1
    
    return (modelist, len(countdict))
def equake_report_report(mmm,magnitudes):

    pass
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

    print("ITEM","FREQUENCY")
    return(countdict)
fname = 'equakes50f.txt'
equake_analysis(equake_readf(fname))


