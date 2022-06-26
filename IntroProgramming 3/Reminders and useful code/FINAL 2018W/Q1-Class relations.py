class Interval(object):
    """An interval has a starting point and an ending point"""

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self):
        return "Interval({},{})".format(self.start, self.end)

    def __str__(self):
        return self.__repr__()

    def slide(self, delta: int):
        print(f"Start: {self.start}, Delta: {delta}")
        self.start += delta
        print(f"End: {self.end}, Delta: {delta}")
        self.end += delta
        print(self.start,self.end)

    def scale(self, factor: int):
        print(f"Factor: {factor}")
        print(f"END{self.end} = START{self.start} + FACTOR{factor} * (END{self.end} - START{self.start})")
        self.end = self.start + factor * (self.end - self.start)

from_zero = Interval(0,1)
from_one = Interval(1,2)
from_zero.slide(10)
from_zero.scale(10)
from_one.slide(8)
print(from_zero)
print(from_one)

#To explain Interval from_zero starts at 0,1 and slides over 10 to the right (10,11)
#*End(11) - start(10) = 1) * factor(10) + start(10) = 20 = end
#10,20
