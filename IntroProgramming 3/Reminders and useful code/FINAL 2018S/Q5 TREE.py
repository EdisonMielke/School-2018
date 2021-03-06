class Tree(object):
    def depth(self) -> int:
        raise NotImplementedError("depth method must be implemented")

class Inner(Tree):

    def __init__(self, left: Tree, right: Tree):
        self.left = left
        self.right = right

    def __repr__(self):
        return "Inner({}, {})".format(self.left, self.right)

    def depth(self) -> int:
        
        return 1 + max(self.left.depth(), self.right.depth())

class Leaf(Tree):

    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return "Leaf({})".format(self.value)

    def depth(self) -> int:
        return 1


skewed = Inner(Leaf(1), Inner(Leaf(2), Leaf(3)))
print("{} has depth {}".format(skewed, skewed.depth()))
# Expected output:  Inner(Leaf(1), Inner(Leaf(2), Leaf(3))) has depth 3
balanced =   Inner(Inner(Leaf(1), Leaf(2)), Inner(Leaf(3), Leaf(4)))
print("{} has depth {}".format(balanced, balanced.depth()))
# Expected output:  Inner(Inner(Leaf(1), Leaf(2)), Inner(Leaf(3), Leaf(4))) has depth 3
way_skewed = Inner(Leaf(1), Inner(Leaf(2), Inner(Leaf(3), Leaf(4))))
print("{} has depth {}".format(way_skewed, way_skewed.depth()))
# Expected output:   Inner(Leaf(1), Inner(Leaf(2), Inner(Leaf(3), Leaf(4)))) has depth 4