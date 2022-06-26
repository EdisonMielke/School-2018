"""
The game state and logic (model component) of 512, 
a game based on 2048 with a few changes. 
This is the 'model' part of the model-view-controller
construction plan.  It must NOT depend on any
particular view component, but it produces event 
notifications to trigger view updates. 
"""

from game_element import GameElement, GameEvent, EventKind
from typing import List, Tuple, Optional
import random

# Configuration constants
GRID_SIZE = 4

class Vec():
    """A Vec is an (x,y) or (row, column) pair that
    represents distance along two orthogonal axes.
    Interpreted as a position, a Vec represents
    distance from (0,0).  Interpreted as movement,
    it represents distance from another position.
    Thus we can add two Vecs to get a Vec.
    """
    #Added Constructor, __add__ and __eq__
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: "Vec") -> "Vec":
        newrow = self.x + other.x
        newcol = self.y + other.y
        
        return Vec(newrow, newcol)

    def __eq__(self, other: "Vec") -> "Vec":
        if self.x == other.x and self.y == other.y:
            return True

    def rettup(self) -> tuple:
        """Returns the individual elements of Vec for easier access"""
        return(self.x,self.y)

    def __str__(self) -> str:
        return str(self.x, self.y)

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

class Tile(GameElement):
    """A slidy numbered thing."""

    def __init__(self, pos: Vec, value: int):
        super().__init__()
        self.row = pos.x
        self.col = pos.y
        self.value = value
        
    def __repr__(self):
        """Not like constructor --- more useful for debugging"""
        return f"Tile[{self.row},{self.col}]:{self.value}"

    def __str__(self):
        return str(self.value)

    def move_to(self, new_pos: Vec):
        self.row = new_pos.x
        self.col = new_pos.y
        self.notify_all(GameEvent(EventKind.tile_updated, self))

    def __eq__(self, other: "Tile") -> bool:
        return self.value == other.value

    def merge(self, other: "Tile"):
        # This tile incorporates the value of the other tile
        self.value = self.value + other.value
        self.notify_all(GameEvent(EventKind.tile_updated, self))
        # The other tile has been absorbed.  Resistance was futile. 
        other.notify_all(GameEvent(EventKind.tile_removed, other))
  
class Board(GameElement):
    """The game grid.  Inherits 'add_listener' and 'notify_all'
    methods from game_element.GameElement so that the game
    can be displayed graphically.
    """

    def __init__(self, rows=4, cols=4):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.tiles = [ ]
        for row in range(rows):
            row_tiles = [ ]
            for col in range(cols):
                row_tiles.append(None)
            self.tiles.append(row_tiles)

    def __getitem__(self, pos: Vec) -> Tile:
        return self.tiles[pos.x][pos.y]
    
    def __setitem__(self, pos: Vec, tile: Tile):
        self.tiles[pos.x][pos.y] = tile

    def _empty_positions(self) -> List[Vec]:
        """Return a list of positions of None values, 
        i.e., unoccupied spaces. 
        """
        empties = [ ]
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[row])):
                empty = (self.tiles[row][col])
                if empty is None:
                    empties.append(Vec(row, col))
        return empties

    def to_list(self) -> List[List[int]]:
        """Test scaffolding: represent each Tile by its
        integer value and empty positions as 0
        """
        result = [ ]
        for row in self.tiles:
            row_values = []     
            for col in row:
                if col is None:  
                    row_values.append(0)
                else:
                    row_values.append(col.value)
            result.append(row_values)
        return result
    
    def from_list(self, values: List[List[int]]):
        """Test scaffolding: set board tiles to the
        given values, where 0 represents an empty space.
        """
        
        self.tiles = []
        colnew = []
        for row in range (len(values)):
            rownew = []
            for col in range (len(values[row])):
                pos = Vec(row, col)
                value = values[row][col]
                if value == 0:
                    value = None
                else:
                    value = Tile(pos,value)
                rownew.append(value)
            self.tiles.append(rownew)

    def has_empty(self) -> bool:
        """Is there at least one grid element without a tile?"""
        if self._empty_positions() != []:
            return True
        
    def place_tile(self, value=None):
        """Place a tile on a randomly chosen empty square."""
        empties = self._empty_positions()
        assert len(empties) > 0
        choice = random.choice(empties)
        row, col = choice.x, choice.y
        if value is None:
            # 0.1 probability of 4
            if random.random() <= 0.1:
                value = 4
            else:
                value = 2
        new_tile = Tile(Vec(row, col), value)
        self.tiles[row][col] = new_tile
        self.notify_all(GameEvent(EventKind.tile_created, new_tile))

    def in_bounds(self, pos: Vec) -> bool:
        """Is position (pos.x, pos.y) a legal position on the board?"""
        if -1 < (pos.rettup()[0]) < self.rows and -1 < pos.rettup()[1] < self.cols:
            return True
        else:
            return False

    def slide(self, pos: Vec,  dir: Vec):
        """Slide tile at pos.x, pos.y (if any)
        in direction (dir.x, dir.y) until it bumps into
        another tile or the edge of the board.
        """

        if self[pos] is None:
            return
        while True:
            new_pos = pos + dir
            if not self.in_bounds(new_pos):
                break
            if self[new_pos] is None:
                self._move_tile(pos, new_pos)
            elif self[pos] == self[new_pos]:
                self[pos].merge(self[new_pos])
                self._move_tile(pos, new_pos)
                break  # Stop moving when we merge with another tile
            else:
                # Stuck against another tile
                break
            pos = new_pos
 
    def _move_tile(self, old_pos: Vec, new_pos: Vec):
        '''I write this'''
        self.tiles[old_pos.x][old_pos.y].move_to(new_pos)
        self.tiles[new_pos.x][new_pos.y] = self.tiles[old_pos.x][old_pos.y]
        Vec(self.tiles[old_pos.x],[old_pos.y])
        self.tiles[old_pos.x][old_pos.y] = None

    def right(self):
        for i in reversed(range(self.rows)):
            for j in range(self.cols):
                self.slide(Vec(i,j), Vec(0, 1))

    def left(self):
        for i in range(self.rows):
            for j in range(self.cols):             
                self.slide(Vec(i,j), Vec(0, -1))

    def up(self):
        for i in reversed(range(self.rows)):
            for j in range(self.cols):
                self.slide(Vec(j,i), Vec(-1, 0))
    
    def down(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.slide(Vec(j,i), Vec(1, 0))

        
    def score(self) -> int:
        """Calculate a score from the board.
        (Differs from classic 1024, which calculates score
        based on sequence of moves rather than state of
        board.
        """

        total_score = []
        new_score = 0
        for row in range (len(self.tiles)):
            for col in range (len(self.tiles[row])):
                if self.tiles[row][col] is None:
                    pass
                else:
                    total_score.append(self.tiles[row][col])
        for i in total_score:
            new_score += i.value
        return new_score
