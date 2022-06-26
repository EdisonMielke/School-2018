def print_column(grid: list):
    #establish height of column
    for row in range (len(grid[0])):
        #do it again for each column
        for height in range (len(grid)):
            #flip the values
            print(grid[height][row])

def print_row(grid: list):
    for row in grid:
        for index in range (len(row)):
            print(row[index])

print()
print_column([[1,2,3,4],
              [1,2,3,4],
              [1,2,3,4],
              [1,2,3,4]])
print()
print_row([[1,2,3,4],
           [1,2,3,4],
           [1,2,3,4]])