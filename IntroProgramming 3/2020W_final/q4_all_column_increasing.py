"""
All columns strictly increasing
(Final exam problem, Winter 2020, CIS 211 at UO)
"""
from typing import List

def all_col_increasing(grid: List[List[int]]) -> bool:
    """Grid is a rectangular array of integers
    (each row is the same length).
    Returns True iff for each column, the integers in that
    column are strictly increasing.
    """
    if grid == []:
        return True
    if grid == ([[],[]]):
        return True
    if len(grid[0]) == 1:
        return True

    for row in range(len(grid[0])):
        previous = grid[0][row]
        for height in range(len(grid)-1):
            if previous < grid[height+1][row]:
                previous = grid[height+1][row]
            else:
                return False



    return True

# Test cases
# Vacuous cases:
# If there are no columns, then there are no columns out of order
assert all_col_increasing([])        # No rows or columns
assert all_col_increasing([[], []])  # Two rows, no columns

# If there is only one element in a column, then
# it must be in order
assert all_col_increasing([[1],[2]])

# Typical true case:
assert all_col_increasing([[3, 2, 1],
                           [4, 3, 2],
                           [5, 4, 3]])

# Typical false case:
assert not all_col_increasing([[5, 10, 20],
                               [6, 7,  21],
                               [7, 8,  10]])

# Don't assume square grid
assert not all_col_increasing([[5, 6, 7],
                               [6, 7, 8],
                               [7, 8, 9],
                               [8, 9, 8]])

assert not all_col_increasing([[5, 6, 7, 8],
                               [6, 7, 8, 8]])

# Don't assume positive values
assert all_col_increasing([[-20, -30, -10],
                           [-18, -28, -8],
                           [-5, -2,  -5]])

print("Successful")








