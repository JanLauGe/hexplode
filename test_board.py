#Code from hexplode/simulation.py to create board shape
def _make_id(i, j):
    return "tile_{}_{}".format(i, j)

def _make_neighbours(i, j, boardsize):
    maxi = 2 * boardsize - 1
    maxj = min(boardsize + i, 3 * boardsize - 2 - i)
    neighbours = []
    if j - 1 >= 0:
        neighbours.append(_make_id(i, j - 1))  # North neighbour
    if j + 1 < maxj:
        neighbours.append(_make_id(i, j + 1))  # South neighbour
    if i < (maxi - 1) / 2:
        # West of the central column
        neighbours.append(_make_id(i + 1, j))  # Northeast neighbour
        neighbours.append(_make_id(i + 1, j + 1))  # Southeast neighbour
        if i - 1 >= 0:
            # East of the first column
            if j - 1 >= 0:
                neighbours.append(_make_id(i - 1, j - 1))  # Northwest neighbour
            if j < maxj - 1:
                neighbours.append(_make_id(i - 1, j))  # Southwest neighbour
    elif i > ((maxi - 1) / 2):
        # East of the central column
        neighbours.append(_make_id(i - 1, j))  # Northwest neighbour
        neighbours.append(_make_id(i - 1, j + 1))  # Soutwest neighbour
        if i + 1 < maxi:
            # West of the last column
            if j - 1 >= 0:
                neighbours.append(_make_id(i + 1, j - 1))  # Northeast neighbour
            if j < maxj - 1:
                neighbours.append(_make_id(i + 1, j))  # Southeast neighbour
    else:
        # On the central column
        if j - 1 >= 0:
            neighbours.append(_make_id(i - 1, j - 1))  # Northwest neighbour
            neighbours.append(_make_id(i + 1, j - 1))  # Northeast neighbour
        if j < maxj - 1:
            neighbours.append(_make_id(i - 1, j))  # Southwest neighbour
            neighbours.append(_make_id(i + 1, j))  # Southeast neighbour
    return neighbours

def _make_board(boardsize):
    return {_make_id(i, j): dict(counters=None,
                                 player=None,
                                 neighbours=_make_neighbours(i, j, boardsize))
            for i in range(2 * boardsize - 1)
            for j in range(min(boardsize + i, 3 * boardsize - 2 - i))}

global BoardShape
BoardShape = _make_board(4)

# Add one counter to avoid game-over at start
board['tile_6_3']['player'] = 1
board['tile_6_3']['counters'] = 1
board['tile_4_1']['player'] = 0
board['tile_4_1']['counters'] = 1    
    