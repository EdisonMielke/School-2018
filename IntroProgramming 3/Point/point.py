'''
Name: Edison Mielke
Assignment: Point Class 
'''
class Point:
    """ This class is a group of 2 integers being x and y,
    usually used to depict a point on a graph, this is mutable but commented out
    is an immutable variant"""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self,dx: int, dy: int):
        ''' this will move the point, adjusting the x coordinate by dx
        and the y coordinate by dy'''
        #return Point(self.x + dx, self.y + dy)# immutable Variant            

        self.x = self.x + dx #Mutable Variant
        self.y = self.y + dy

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

