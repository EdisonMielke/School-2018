"""
Author: Edison Mielke
Project: Sudoku

A Sudoku board holds a matrix of tiles.
Each row and column and also sub-blocks
are treated as a group (sometimes called
a 'nonet'); when solved, each group must contain
exactly one occurrence of each of the
symbol choices.

Note: I had a test case that would seemingly randomly fail "test_groups_are_distinct"
and after adding the __hash__ method professor Young posted Here "https://piazza.com/class/k4gg6ijvm5crw?cid=134"
it seemed to fix it.

Credit: I got huge help after looking at my peer review and saw the hidden single and naked single solutions that
William King and Yushu Chen used for my peer reviews for them and figured out how to do that thanks to them. 
"""
from sdk_config import CHOICES, UNKNOWN, ROOT, NROWS, NCOLS
from typing import Sequence, List, Set
import enum
import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class Event(object):
    """Abstract base class of all events, both for MVC
    and for other purposes.
    """
    pass

class Listener(object):
    """Abstract base class for listeners.
    Subclass this to make the notification do
    something useful.
    """

    def __init__(self):
        """Default constructor for simple listeners without state"""
        pass

    def notify(self, event: Event):
        """The 'notify' method of the base class must be
        overridden in concrete classes.
        """
        raise NotImplementedError("You must override Listener.notify")

class EventKind(enum.Enum):
    TileChanged = 1
    TileGuessed = 2

class TileEvent(Event):
    """Abstract base class for things that happen
    to tiles. We always indicate the tile.  Concrete
    subclasses indicate the nature of the event.
    """

    def __init__(self, tile: 'Tile', kind: EventKind):
        self.tile = tile
        self.kind = kind
        # Note 'Tile' type is a forward reference;
        # Tile class is defined below

    def __str__(self):
        """Printed representation includes name of concrete subclass"""
        return f"{repr(self.tile)}"

class TileListener(Listener):
    def notify(self, event: TileEvent):
        raise NotImplementedError(
            "TileListener subclass needs to override notify(TileEvent)")

class Listenable:
    """Objects to which listeners (like a view component) can be attached"""

    def __init__(self):
        self.listeners = [ ]

    def add_listener(self, listener: Listener):
        self.listeners.append(listener)

    def notify_all(self, event: Event):
        for listener in self.listeners:
            listener.notify(event)

class Tile(Listenable):
    """Builds a tile that will be built into the Board class"""
    def __init__(self, row: int, col: int, value=UNKNOWN):
        super().__init__()
        assert value == UNKNOWN or value in CHOICES
        self.row = row
        self.col = col
        self.set_value(value)

    def set_value(self, value: str):
        """Sets a value in a particular tile"""
        if value in CHOICES:
            self.value = value
            self.candidates = {value}
        else:
            self.value = UNKNOWN
            self.candidates = set(CHOICES)
        self.notify_all(TileEvent(self, EventKind.TileChanged))

    def __str__(self) -> str:
        """Returns the value of a tile when printed as a string"""
        return str(self.value)

    def __repr__(self) -> str:
        """Returns the representation of what the tile actually contains"""
        return f"Tile({self.row}, {self.col}, '{self.value}')"
    
    def could_be(self, value: str) -> bool:
        """True iff value is a candidate value for this tile"""
        return value in self.candidates
    
    def __hash__(self) -> int:
        """Hash on position only (not value)"""
        return hash((self.row, self.col))

    def remove_candidates(self, used_values: Set[str]):
        """The used values cannot be a value of this unknown tile.
        We remove those possibilities from the list of candidates.
        If there is exactly one candidate left, we set the
        value of the tile.
        Returns:  True means we eliminated at least one candidate,
        False means nothing changed (none of the 'used_values' was
        in our candidates set).
        """
        new_candidates = self.candidates.difference(used_values)
        if new_candidates == self.candidates:
            # Didn't remove any candidates
            return False
        self.candidates = new_candidates
        if len(self.candidates) == 1:
            self.set_value(new_candidates.pop())
        self.notify_all(TileEvent(self, EventKind.TileChanged))
        return True
    
class Board(object):
    """A board is a matrix of tiles"""
    def __init__(self):
        """The empty board"""
        # Row/Column structure: Each row contains columns
        self.tiles: List[List[Tile]] = [ ]
        for row in range(NROWS):
            cols = [ ]
            for col in range(NCOLS):
                cols.append(Tile(row, col))
            self.tiles.append(cols)
        self.groups = []
        #Clear comment hashes between here and Print('END') to check if rows,
        #cols and groups are working properly    
        #print('START')
        for row in self.tiles:    
            #print(f"Row:{row}")
            self.groups.append(row)
        for i in range(NCOLS):
            col = []
            for row in self.tiles: 
                col.append(row[i])
            #print(f"Column:{col}")
            self.groups.append(col)
        for block_row in range(ROOT):
            for block_col in range(ROOT):
                group = [ ] 
                for row in range(ROOT):
                    for col in range(ROOT):
                        row_addr = (ROOT * block_row) + row
                        col_addr = (ROOT * block_col) + col
                        group.append(self.tiles[row_addr][col_addr])
                #print(f"Group:{group}")
                self.groups.append(group)
        #print(self.groups)
        #print('END')
        #Clear comment hashes between here and print('START') to check if rows,
        #cols and groups are working properly

    def is_consistent(self) -> bool:
        """Checks the consistancy of the board to see if it is possible"""
        for group in self.groups:
            symbols = []
            for i in range(NCOLS):
                symbols.append(group[i].__str__())
            for i in range(NCOLS):
                for j in range(NCOLS):
                    #print(f"Symbol List:{symbols} Symbol 1:{symbols[i]} Symbol 1 Pos:{i} Symbol 2:{symbols[j]} Symbol 2 Pos:{j}")
                    if symbols[i] == '.':
                        break
                    if i == j:
                        #print("Same Position, Skipping")
                        break
                    else:
                        if symbols[i] == symbols[j]:
                            #print("Same Value, Not Consistant")
                            return False
        #print("This is Consistant")
        return True

    def set_tiles(self, tile_values: Sequence[Sequence[str]] ):
        """Set the tile values a list of lists or a list of strings"""
        for row_num in range(NROWS):
            for col_num in range(NCOLS):
                tile = self.tiles[row_num][col_num]
                tile.set_value(tile_values[row_num][col_num])

    def naked_single(self) -> bool:
        """Eliminate candidates and check for sole remaining possibilities.
        Return value True means we crossed off at least one candidate.
        Return value False means we made no progress.
        """
        '''

        ###My original solution that didn't work, it didn't feel
        ###right to outright delete it

        candidates = []
        symbols = []
        possiblesymbols = ['1','2','3','4','5','6','7','8','9']
        for row in self.tiles:
            for tile in row:
                if tile.__str__() == '.':
                    candidates.append(tile)
                    #Creates Candidates for the search
        for candidate in candidates:
            symbols = []
            knownsymbols = []
            for group in self.groups:
                for i in range(NCOLS):  
                    if candidate.__repr__() == group[i].__repr__():
                        for tile in group:
                            symbols.append(tile.__str__())
                            #Searches for relevant self.group groups
            for symbol in symbols:
                if symbol != '.':
                    knownsymbols.append(symbol)
            #print(knownsymbols)
            if len(knownsymbols) == 9:
                 naked_single = set(possiblesymbols) ^ set(knownsymbols)
                 naked_single = (list(naked_single))
                 naked_single = naked_single[0]
                 #Finds the symbol

                 for row in self.tiles:
                    for tile in row:
                        if tile.row == candidate.row and tile.col == candidate.col:
                            tile.value = naked_single
                 return True 
        return False
    '''
        nakedsingle = False
        for row in self.groups:
            used = set()
            for tile in row:
                if tile.value in CHOICES:
                    if tile.value in used:
                        break
                    else:
                        used.add(tile.value)
            for tile in row:
                 if tile.value == UNKNOWN:
                    nakedsingle = tile.remove_candidates(used) or nakedsingle
        return nakedsingle

    def hidden_single(self):
        """Eliminate candidates and check for sole remaining possibilities.
        Return value True means we crossed off at least one candidate.
        Return value False means we made no progress"""
        hiddensingle = False
        for row in self.groups:
            values = set(CHOICES)
            for tile in row:
                if tile != UNKNOWN:
                    values.discard(tile.value)
            for value in values:
                counter = 0
                for tile in row:
                    if value in tile.candidates:
                        counter += 1
                if counter == 1:
                    for tile in row:
                        if tile.value == UNKNOWN:
                            if value in tile.candidates:
                                tile.set_value(value)
                                hiddensingle = True
        return hiddensingle
    
    def propagate(self):
        """Repeat solution tactics until we 
        don't make any progress, whether or not
        the board is solved. 
        """
        progress = True
        while progress:
            progress = self.naked_single()
            self.hidden_single()
        return

    def solve(self):
        """General solver; guess-and-check 
        combined with constraint propagation.
        """
        self.propagate()
        if self.is_complete() == True:
            return True
        if self.is_consistent() == False:
            return False
        else:
            saved = self.as_list()
            boardsaved = Board() 
            mintile = self.min_choice_tile()
            for value in mintile.candidates:
                mintile.value = value
                if self.solve():
                    return True
                else: 
                    self.set_tiles(saved)
            return False

    def __str__(self) -> str:
        """In Sadman Sudoku format"""
        return "\n".join(self.as_list())

    def as_list(self) -> List[str]:
        """Tile values in a format compatible with 
        set_tiles.
        """
        row_syms = [ ]
        for row in self.tiles:
            values = [tile.value for tile in row]
            row_syms.append("".join(values))
        return row_syms

    def min_choice_tile(self) -> Tile: 
        """Returns a tile with value UNKNOWN and 
        minimum number of candidates. 
        Precondition: There is at least one tile 
        with value UNKNOWN. 
        """
        #finds first possible tile with an UNKNOWN value
        for row in self.groups:
            for tile in row:
                if len(tile.candidates) != 1:
                    mintile = tile
                    break
            break
        #Using the first possible value, compares each next tile to find the smallest candidate count
        for row in self.groups:
            values = set(CHOICES)
            for tile in row:
                if len(tile.candidates) != 1:
                        if len(tile.candidates) < len(mintile.candidates):
                            mintile = tile
        return(mintile)

    def is_complete(self) -> bool:
        """None of the tiles are UNKNOWN.  
        Note: Does not check consistency; do that 
        separately with is_consistent.
        """
        if self.is_consistent() is True:
            for row in self.tiles:
                for tile in row:
                    if tile.value == UNKNOWN:
                        return False
        else:
            return False
        return True

