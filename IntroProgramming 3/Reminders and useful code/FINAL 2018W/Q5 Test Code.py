from typing import List

class Area(object):
    """Abstract class."""

    def __init__(self, name: str):
        self.name = name

    def population(self) -> int:
      raise NotImplementedError("population method nust be overridden")

class Place(Area):
    def __init__(self, name: str, pop: int):
        self.pop = pop
        super().__init__(name)

    def population(self) -> int:
        #I FINISH
        return self.pop


class Region(Area):
    def __init__(self, name, subregions: List[Area]):
        super().__init__(name)
        self.subregions = subregions

    def population(self) -> int:
        #I FINISH
        totalpop = 0
        for i in self.subregions:
            if i.population() != None:
                totalpop += i.population()
        return totalpop



lane = Region("Lane County", [Place("Eugene", 166575), Place("Springfield", 60177)])
benton = Region("Benton County", [Place("Corvallis", 55298), Place("Philomath", 4594)])
s_willamette = Region("South Willamette Valley", [lane, benton])

print(s_willamette.population())
#Expected output: 286644