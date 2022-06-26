from typing import List
class Seg(object):

    def __init__(self, low: int, high: int):
        self.low = low # low attribute is public, read-only
        self.high = high # high attribute is public, read-only

    def length(self):
        return self.high - self.low

    def __str__(self):
        return "Seg({},{})".format(self.low, self.high)

class Comparison(object):

    def compare(self, s1: Seg, s2: Seg) -> bool:
        raise NotImplementedError("compare method must be overridden")

class Longer(Comparison):

    def compare(self, s1: Seg, s2: Seg) -> bool:
        return s1.length() > s2.length()

class SegList(object):
    def __init__(self, segs: List[Seg]):
        assert len(segs) > 0, "segs must not be empty"
        self._contents = segs

    def maximal(self, comparison: Comparison) -> Seg:
    #I FINISHED
        """Return seg that is maximal according to comparison"""
        maximum = (self._contents[0].high) - (self._contents[0].low)
        maxlow = (self._contents[0].low)
        maxhigh = (self._contents[0].high)

        for i in range(len(self._contents)-1):
            if ((self._contents[i+1].high) - (self._contents[i+1].low)) > maximum:
                maximum = ((self._contents[i+1].high) - (self._contents[i+1].low))
                maxlow = (self._contents[i + 1].low)
                maxhigh = (self._contents[i + 1].high)


        return(Seg(maxlow,maxhigh))
segs = SegList([Seg(0,3), Seg(1,2), Seg(1,10), Seg(5,6)])
print(segs.maximal(Longer())) # Expected output: Seg(1,10)