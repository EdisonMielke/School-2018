from typing import List
class Grid(object):
    """Holds a small 3x3 grid of digits "0".."9".Each row of the grid is a string, e.g., "987"."""

    def __init__(self, digits: List[str]):
        self._grid = digits

    def has_duplicates(self) -> bool:
        """Returns True iff the same digit valueappears in any two distinct cells."""
        seen = set()
        for row in self._grid:
            for cell in row:
                if cell in seen:
                    return True
                seen.add(cell)

        return False

with_dups = Grid(["012", "234", "567"])
without_dups = Grid(["012", "345", "678"])
print("With dups, should be true: {}".format(with_dups.has_duplicates()))
print("Without dups, should be false: {}".format(without_dups.has_duplicates()))