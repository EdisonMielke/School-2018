"""Rodents of Unusual Size: CIS 211 final exam problem, Winter 2020
One of the three dangers of the fire swamps
"""

from typing import List

class Rodent:
    def __init__(self, name: str, weight_gm: int):
        self.name = name
        self._weight = weight_gm  # Weight in grams

    def size(self) -> int:
        """Weight is a good enough approximation of size"""
        return self._weight

def r_o_u_s(rodents: List[Rodent]) -> List[Rodent]:
    """Returns members of rodents who are at least
    twice as heavy as the average weight of rodents
    in the group.
    """
    totalrodentweight = 0
    rodentsofunusualsize = []
    if len(rodents) == 0:
        return []
    for ratking in rodents:
        totalrodentweight += ratking._weight
    averagerodentweight = totalrodentweight/(len(rodents))
    unusualsize = averagerodentweight*2
    for ratking in rodents:
        if ratking._weight > unusualsize:
            rodentsofunusualsize.append(ratking)
    return rodentsofunusualsize


charly = Rodent("Charly", 5)
marley = Rodent("Marley", 8)
corey = Rodent("Corey", 18)
fiona = Rodent("Fiona", 3)
mory = Rodent("Mory", 9)
phillip = Rodent("Phillip", 9)
swarm = [ charly, marley, corey, fiona, mory, phillip ]

assert r_o_u_s(swarm) == [corey]
assert r_o_u_s([]) == []

# The rodents of unusual size?  I don't believe they exist.
typical_swarm = [charly, marley, fiona, mory]
assert r_o_u_s(typical_swarm) == [ ]