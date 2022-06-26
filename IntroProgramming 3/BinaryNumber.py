"""
CIS 211 LAB #6
Author: Edison Mielke

Description: 
"""
class BinaryNumber:
    """ A list of 0's and 1's """

    def __init__(self, binary:list):
        self.binary = binary

    def __or__(self, other) -> 'BinaryNumber':
        """Compares two BinaryNumbers and creates a
        new BinaryNumber where 1 is in any position
        a 1 was in either self or other and a 0 in
        any other position
        """
        assert len(self.binary) == len(other.binary)
        newbinary = []
        for num in range(len(self.binary)):
            if (self.binary[num] != other.binary[num]):
                newbinary.append(1)
            else:
                if self.binary[num] == 1:
                    newbinary.append(1)
                else:
                    newbinary.append(0)
        return BinaryNumber(newbinary)
            
    
    def __and__(self, other) -> 'BinaryNumber':
        """Compares two BinaryNumbers and creates a
        new BinaryNumber where 1 is in any position
        where both self and other had a 1 and a 0
        in any other position
        """
        assert len(self.binary) == len(other.binary)
        newbinary = []
        for num in range(len(self.binary)):
            if self.binary[num] == other.binary[num]:
                if self.binary[num] == 1:
                    newbinary.append(1)
                else:
                    newbinary.append(0)
            else:
                newbinary.append(0)
        return BinaryNumber(newbinary)

    def __add__(self, other) -> 'BinaryNumber':
        """Adds two numbers in binary format together"""
        assert len(self.binary) == len(other.binary)
        newbinary = []
        carryover = 0
        for i in range(len(self.binary)):
            carryover = (self.binary[-(i+1)] + other.binary[-(i+1)] + carryover)
            if carryover < 2:
                newbinary = [carryover] + newbinary
                carryover = 0
            if carryover == 2:
                carryover = 1
                newbinary = [0] + newbinary
            if carryover == 3:
                carryover = 1
                newbinary = [1] + newbinary
        if carryover + (self.binary[0]) + (other.binary[0]) == 3:
            newbinary = [1] + newbinary

        return BinaryNumber(newbinary)
    
    def left_shift(self):
        """Does a binary shift to the left"""
        self.binary.append(0)
        self.binary.remove(self.binary[0])

    def right_shift(self):
        """Does a binary shift to the right"""
        self.binary.pop()
        self.binary = [0] + self.binary

    def arithmetic_right_shift(self):
        """Does an arithmetic binary shift to the right"""
        self.binary.pop()
        self.binary = [self.binary[0]] + self.binary

    def __str__(self):
        stringbinary = ""
        for num in self.binary:
            stringbinary += str(num)
        return stringbinary
    
    def __repr__(self):
        return f"BinaryNumber({self.binary})"

bn = BinaryNumber([1,0,1,0,1])
bn2 = BinaryNumber([1,1,1,0,0])
