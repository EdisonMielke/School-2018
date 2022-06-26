
def all_same(l: list) -> bool:
    '''
    Determines whether or not each element of a list is the same integer and
    returns a boolean expression
    Ex:
    all_same([]) returns True
    all_same([1]) returns True
    all_same([1,1,1,1]) returns True
    all_same([1,2]) returns False
    all_same([1,2,1]) returns False
    '''
    if len(l) <= 1:
        return True
    #Accounting for edge cases
    
    for i in range (len(l)-1):
        if l[i] != l[i-1]:
            return False
        else:        
            if l[-1] == l[-2]:
                return True
        
def dedup(l: list) -> list:
    '''
    Creates a new list in which each element is not duplicated
    Ex:
    dedup([]) returns []
    dedup([1]) returns [1]
    dedup([1,1,1,1]) returns [1]
    dedup([1,2,3,4]) returns [1,2,3,4]
    dedup([1,1,3,3,3,5]) returns [1,3,5]
    '''
    if len(l) == 0:
        return []
    if all_same(l) == True:
        return [l[0]]
    #Accounting for edge cases

    new_list = []
    for i in range(len(l)-1):
        if l[i] != l[i+1]:
            new_list.append(l[i])          
    new_list.append(l[-1])
    return new_list
        
def max_run(l: list) -> int:
    '''
    Determines the maximum 'run' of a list, which is the repeat of the same
    integer in a row
    Ex:
    max_run([]) returns 0
    max_run([42]) returns 1
    max_run([5,5,5,5,5]) returns 5
    max_run([1,2,3,4]) returns 1
    max_run([1,2,2,2]) returns 3
    '''
    if len(l) == 0:
        return 0
    if len(l) == 1:
        return 1
    if all_same(l) == True:
        return len(l)
    #Accounting for edge cases

    count = 1
    max_count = 0

    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            count += 1   
            if max_count < count:
                max_count = count
        else:
            count = 1

    if count == 1 and max_count == 0:
        max_count = 1

    return(max_count)
