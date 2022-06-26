Waldo = 'W'
Other = '.'

def convert_row_to_col(grid: list) -> list:
    '''Converts the grid's rows into columns'''
    icount = -1
    newgrid = []
    applier = []
    for j in range(len(grid[0])):
        for i in grid:
            applier.append(i[j])
            if len(applier) == len(grid[0]):
                newgrid.append(applier)
                applier = []
    return(newgrid)

def all_row_exists_waldo(wally: list) -> bool:
    ''' For all rows in the matrix, Waldo is in some column '''
    wcount = 0
    if wally == []:
        return True
    if wally == [[],[]]:
        return False
    for i in wally:
        for j in i:
            if j == 'W':
                wcount += 1
                break
    if wcount == len(wally):
        return True
    else:
        return False
    
def all_col_exists_waldo(wally: list) -> bool:
    ''' For all columns in the matrix, Waldo is in some row'''
    wcount = 0
    if wally == []:
        return True
    if wally == [[],[]]:
        return True
    wally = convert_row_to_col(wally)
    for i in wally:  
        for j in i:
            if j == 'W':
                wcount += 1
                break
    if wcount == len(wally):
        return True
    else:
        return False
    
def all_row_all_waldo(wally: list) -> bool:
    ''' For all rows in the matrix, Waldo is in every column '''
    if wally == []:
        return True
    if wally == [[],[],[]]:
        return True
    
    for i in wally:
        for j in i:
            if j != 'W':
                return False
    return True

def all_col_all_waldo(wally: list) -> bool:
    #redundant
    ''' For all the columns in the matrix, Waldo is in every row '''
    if wally == []:
        return True
    if wally == [[],[],[]]:
        return True
    wally = convert_row_to_col(wally)
    for i in wally:
        for j in i:
            if j != 'W':
                return False
    return True

def exists_row_all_waldo(wally: list) -> bool:
    ''' There is some row in the matrix in which Waldo is in every column '''
    if wally == []:
        return False
    if wally == [[],[]]:
        return True
    for i in wally:
        wcount = 0
        for j in range (len(i)):
            if i[j] == 'W':
                wcount +=1
            if wcount == len(i):
                return True
    return False
def exists_col_all_waldo(wally: list) -> bool:
    ''' There is some column in the matrix in which Waldo is in every row '''
    if wally == []:
        return False
    if wally == [[],[]]:
        return False
    wally = convert_row_to_col(wally)
    for i in wally:
        wcount = 0
        for j in range (len(i)):
            if i[j] == 'W':
                wcount +=1
            if wcount == len(i):
                return True
    return False
                
def exists_row_exists_waldo(wally: list) -> bool:
    ''' There is some row in the matrix in which Waldo is in some column '''
    if wally == []:
        return False
    if wally == [[],[]]:
        return False
    for i in wally:
        for j in i:
            if j == 'W':
                return True
    return False
def exists_col_exists_waldo(wally: list) -> bool:
    #redundant
    ''' There is some column in the matrix in which Waldo is in some row '''
    if wally == []:
        return False
    if wally == [[],[]]:
        return False
    wally = convert_row_to_col(wally)
    for i in wally:
        for j in i:
            if j == 'W':
                return True
    return False
