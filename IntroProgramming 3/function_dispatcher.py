def total_sum(summable_list: list) -> int:
    ''' Takes a list of integers and returns the sum of each '''
    sum = 0
    for integers in summable_list:
        sum += integers
    return sum

def apply(funct, apply_list: list) -> list:
    ''' Takes a function and a list together and applies
    the function to each element in the list and returns
    a new list '''
    newlist = []
    for integers in apply_list:
        newlist.append(funct(integers))
    return newlist

def square(square_list):
    squared = lambda x: x ** 2
    newlist = []
    for i in (square_list):
        newlist.append(squared(i))
    return(newlist)


def magnitude(mag_list: list) -> int:
    ''' Takes a list of integers and returns the magnitude,
    the square root of all squares in the list'''
    sum = total_sum(square(mag_list))
    return sum ** (1/2)

dispatch_table = {
    "sum": total_sum,
    "square": square,
    "mag": magnitude,
}
class FunctionDispatcher:
    """ A class that takes a dictionary of functions and then applies
    them to a table of integers"""

    def __init__(self, function_table: dict):
        self.function_table = function_table

    def process_command(self,command: int, integer_list: list):
        return self.function_table[command](integer_list)

#Basic Test Cases
fd = FunctionDispatcher(dispatch_table)
print(fd.process_command("sum", [3,4]))
print(fd.process_command("square", [3,4]))
print(fd.process_command("mag", [3,4]))