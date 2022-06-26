"""Chooser: CIS 211 Winter 2020 exam problem.
Factoring methods with inheritance.
"""

from typing import List

class Chooser:
    """Abstract base class. Write concrete subclasses
    that make particular choices.
    """

    def _choose(self, prior: int, item: int) -> int:
        raise NotImplementedError("You must override _choose")

    def choose(self, items: List[int]) -> int:
        if len(items) == 0:
            raise ValueError("Cannot choose from empty list")
        choice = items[0]
        for item in items:
            choice = self._choose(choice, item)
        return choice

class Minimizer(Chooser):
    """Choose the smallest element"""
    def _choose(self, prior: int, item: int) -> int:
        if item <= prior:
            return item
        else:
            return prior

class Maximizer(Chooser):
    """Choose the largest element"""
    def _choose(self, prior: int, item: int) -> int:
        if item >= prior:
            return item
        else:
            return prior

# Examples that work
class First(Chooser):
    """Choose the first element"""
    def _choose(self, prior: int, current: int) -> int:
        return prior

class Last(Chooser):
    """Choose the last element"""
    def _choose(self, prior: int, current: int) -> int:
        return current

a_list = [1, 3, 7, 2, 7, 18, -12, 4]
assert Last().choose(a_list) == 4
assert First().choose(a_list) == 1
assert Minimizer().choose(a_list) == -12
assert Maximizer().choose(a_list) == 18
print("Finished")



