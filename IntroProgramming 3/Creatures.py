class Creature(object):

    def __init__(self):
        raise NotImplementedError("Abstract classes should not be instanciated")

    def __str__(self) -> str:
        raise NotImplementedError("Abstract class methods should not be called")

    def search(self, value: str) -> bool:
        raise NotImplementedError("Abstract class methods should not be called")

class Orthrus(Creature):

    def __init__(self, left: 'Creature', right: 'Creature'):
        self.left = left
        self.right = right

    def __str__(self) -> str:
        combined = f"{str(self.left)} {str(self.right)}"
        return combined

    def search(self, value: str) -> bool:
        if self.left.search(value) == True:
            return True
        elif self.right.search(value) == True:
            return True
        else:
            return False

class Cerberus(Creature):
    def __init__(self,left: 'Creature', middle: 'Creature', right: 'Creature'):
        self.left = left
        self.middle = middle
        self.right = right

    def __str__(self) -> str:
        combined = f"{str(self.left)} {str(self.middle)} {str(self.right)}"
        return combined

    def search(self, value: str) -> bool:
        
        if self.left.search(value) == True:
            return True
        elif self.middle.search(value) == True:
            return True
        elif self.right.search(value) == True:
            return True
        else:
            return False

class Head(Creature):

    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return (self.name)

    def search(self, value: str) -> bool:
        if self.name == value:
            return True
        else:
            return False
