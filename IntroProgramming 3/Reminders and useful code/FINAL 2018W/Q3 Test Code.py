from typing import Tuple
def pack(a: int, b: int, c: int) -> int:
    word = (a & 3) << 6 | (b & 7) << 3 | (c & 7)\
    #print(bin(word))
    return word

def unpack(word: int) -> Tuple[int, int, int]:
    #THIS IS THE CODE I FINISHED
    amask = 3
    bcmask = 7
    a = ((word >> 6) & amask)
    b = ((word >> 3) & bcmask)
    c = ((word & bcmask ))
    return (a,b,c)


w1 = pack(3, 7, 7)
assert unpack(w1) == (3, 7, 7)
w2 = pack(1, 1, 1)
assert unpack(w2) == (1, 1, 1)