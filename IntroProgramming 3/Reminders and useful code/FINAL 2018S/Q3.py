from typing import Tuple
def pack(x: int, y: int, z: int) -> int:
    #I FINISH
    """Pack x, y, and z into fields of an 8-bit unsigned integer.
    x: bits 5..7  (3 bits)
    y: bits 1..4  (4 bits)
    z: bit 0(1 bit)"""
    return (x << 5 | y << 1 | z)

def unpack(word: int) -> Tuple[int, int, int]:
    """Unpacks unsigned 8-bit int into
    bits 5..7  => x, bits 1..4  => y, bit 0 => z
    Input and all outputs are unsigned."""
    x = (word >> 5) & 7
    y = (word >> 1) & 15
    z = word & 1
    return x, y, z

print("(15, 15, 15) => {} (expect (7, 15, 1))".format(unpack(pack(15, 15, 15))))
print("(3, 3, 3) => {} (expect 3, 3, 1)".format(unpack(pack(3, 3, 3))))
print("(0, 3, 0) => {}  (expect 0, 3, 0)".format(unpack(pack(0, 3, 0))))