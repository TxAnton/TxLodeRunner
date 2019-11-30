import Main

import math

from internals.actions import LoderunnerAction
from internals.board import Board
from internals.element import _ELEMENTS


stack=[]

size=58

used = []

def dfs(x,y, dist, brd):
    brd = Board("&")

    found = False

    global size
    global used

    #if (size == []):
    #    size = math.sqrt(len(brd.to_string()))

    if(used == []):
        used = [[0 for i in range(size)] for j in range(size)]


    used[x][y] = 1

    if(brd.has_gold_at(x,y)):
        stack.append([x,y,dist])
        return True

    #go

    # go LEFT
    _x = x - 1
    _y = y
    brd.get_at(_x, _y).get_char() == '#'
    if (not used[_x][_y] and 0 <= _x < size and 0 <= _y < size):  # in bounds and not visited
        if (brd.has_ladder_at(_x, _y) or brd.has_pipe_at(_x, _y) or (
                _y < size - 1 and (brd.get_at(_x, _y+1).get_char() == '#'))):  # Walkable
            found = found or dfs(_x, _y, dist + 1, brd)

    # go RIGHT
    _x = x + 1
    _y = y

    if (not used[_x][_y] and 0 <= _x < size and 0 <= _y < size):  # in bounds and not visited
        if (brd.has_ladder_at(_x, _y) or brd.has_pipe_at(_x,_y) or (
                _y < size - 1 and (brd.get_at(_x, _y+1).get_char() == '#'))):  # Walkable
            found = found or dfs(_x, _y,dist+1,brd)

    # go UP
    _x = x
    _y = y - 1

    if (not used[_x][_y] and 0 <= _x < size and 0 <= _y < size):  # in bounds and not visited
        if (brd.has_ladder_at(_x, _y) or brd.has_pipe_at(_x,_y) or (
                _y < size - 1 and (brd.get_at(_x, _y+1).get_char() == '#'))):  # Walkable
            found = found or dfs(_x, _y,dist+1,brd)

    # go DOWN
    _x = x
    _y = y + 1

    if (not used[_x][_y] and 0 <= _x < size and 0 <= _y < size):  # in bounds and not visited
        if (brd.has_ladder_at(_x, _y) or brd.has_pipe_at(_x,_y) or (
                _y < size - 1 and (brd.get_at(_x, _y+1).get_char() == '#'))):  # Walkable
            found = found or dfs(_x, _y,dist+1,brd)

    if not found:
        return False
    return True
