from typing import List
class Cheese(object):
    def __init__(self, name: str, smelliness: int):
        self.name = name
        self.smelliness = smelliness

    def __repr__(self):
        return '{} ({})'.format(self.name, self.smelliness)

def select_cheeses(cheeses: List["Cheese"]) -> List["Cheese"]:
    """Returns a list of selected cheeses, which are those with
    smelliness strictly greater than the average smelliness
    of all the cheeses in the list.  Cheeses in the returned list
    are in the same order as they appear in the input list."""
    total_smelliness = 0
    selected_cheeses = []
    for cheese in cheeses:
        total_smelliness += cheese.smelliness
    average_smelliness = (total_smelliness/len(cheeses))
    for cheese in cheeses:
        if cheese.smelliness > average_smelliness:
            selected_cheeses.append(cheese)
    return selected_cheeses


cheeses = [ Cheese("brie", 5), Cheese("stilton", 2), Cheese("camembert", 6),
            Cheese("provolone", 1), Cheese("parmigiano", 2) ]

print("Selected {}".format(select_cheeses(cheeses)))
# Expected output:
# Selected [brie (5), camembert (6)]