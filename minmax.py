from hexplode import algo_player
from sys import maxsize
import random

# SOME CODE HERE TO TEST THE ALGO IS WORKING:
# Simulate a board with tokens to test on

@algo_player(name="weighting function one",
             description="assigning values to positions")

def weighting_function_one_algo(board, game_id, player_id):
    '''
    First custom-made algorithm

    board structure:
    :param board:
        The current state of the board. This is a dict of the form::
            {
                <tile id>: {
                    'counters': <number of counters on tile or None>,
                    'player': <player id of the player who holds the tile or None>,
                    'neighbours': <list of ids of neighbouring tile>
                },
                ...
            }
    :param game_id:
        The id of the game that the algo is playing in.
    :param player_id:
        The id of the player that the algo is playing on behalf of.
    :returns:
        The id of a tile the algo wishes to place a counter in.
    '''

#### PSEUDOCODE
#    def minimax(node, depth, maximizingPlayer):
#        if depth = 0 or node is a terminal node
#            return the heuristic value of node
#        if maximizingPlayer
#            bestValue := -inf
#            for each child of node
#                val := minimax(child, depth - 1, FALSE)
#                bestValue := max(bestValue, val)
#            return bestValue
#        else
#            bestValue := +inf
#            for each child of node
#                val := minimax(child, depth - 1, TRUE)
#                bestValue := min(bestValue, val)
#            return bestValue
#
### https://www.youtube.com/watch?v=fInYh90YMJU
#    #MinMax function:
#    from sys import maxsize
#
#    class Node(object):
#        def __init__(self, i_depth, i_playerNum, i_sticksRemaining, i_value = 0):
#            self.i_depth = i_depth
#            self.i_playerNum = self.i_playerNum
#            i_sticksRemaining = i_sticksRemaining
#            i_value = i_value
#            self.children = []
#            self.CfreateChildren()
#
#        def CreateChildren(self):
#            if self.i_depth >= 0:
#                for i in range(1,3):
#                    v = self.i_sticksRemaining -i
#                    self.children.append( Node( self.i_depth -1,
#                                                -self.i_playerNum,
#                                                v,
#                                                self.ReakVal(v)))
#
#        def RealVal(self, value):
#            if (value == 0):
#                return maxsize * self.i_playerNum
#            elif (value < 0):
#                return maxsize * -self.i_playerNum
#            return 0
#
#    #ALGORITHM
#    def MinMax(node, i_depth, i_playerNum):
#        if (i_depth == 0) or (abs(node.i_value) == maxsize):
#            return node.i_value
#
#        i_bestValue = maxsize * -i_playerNum
#
#        for i in range(len(node.children)):
#            child = node.children[i]
#            i_val = MinMax(child, i_depth - 1, -i_playerNum)
#            if (abs(maxsize * i_playerNum - i_val) < abs(maxsize * i_playerNum - i_bestValue)):
#                i_bestValue = i_val
#
#        return i_bestValue

### EXAMPLE BOARD
# board_state_current = {'tile_1_3': {'player': 0, 'neighbours': ['tile_1_2', 'tile_1_4', 'tile_2_3', 'tile_2_4', 'tile_0_2', 'tile_0_3'], 'counters': 2}, 'tile_6_1': {'player': 1, 'neighbours': ['tile_6_0', 'tile_6_2', 'tile_5_1', 'tile_5_2'], 'counters': 2}, 'tile_1_4': {'player': None, 'neighbours': ['tile_1_3', 'tile_2_4', 'tile_2_5', 'tile_0_3'], 'counters': None}, 'tile_1_1': {'player': None, 'neighbours': ['tile_1_0', 'tile_1_2', 'tile_2_1', 'tile_2_2', 'tile_0_0', 'tile_0_1'], 'counters': None}, 'tile_1_0': {'player': None, 'neighbours': ['tile_1_1', 'tile_2_0', 'tile_2_1', 'tile_0_0'], 'counters': None}, 'tile_6_0': {'player': None, 'neighbours': ['tile_6_1', 'tile_5_0', 'tile_5_1'], 'counters': None}, 'tile_1_2': {'player': None, 'neighbours': ['tile_1_1', 'tile_1_3', 'tile_2_2', 'tile_2_3', 'tile_0_1', 'tile_0_2'], 'counters': None}, 'tile_0_0': {'player': None, 'neighbours': ['tile_0_1', 'tile_1_0', 'tile_1_1'], 'counters': None}, 'tile_0_1': {'player': None, 'neighbours': ['tile_0_0', 'tile_0_2', 'tile_1_1', 'tile_1_2'], 'counters': None}, 'tile_0_2': {'player': None, 'neighbours': ['tile_0_1', 'tile_0_3', 'tile_1_2', 'tile_1_3'], 'counters': None}, 'tile_0_3': {'player': None, 'neighbours': ['tile_0_2', 'tile_1_3', 'tile_1_4'], 'counters': None}, 'tile_3_3': {'player': None, 'neighbours': ['tile_3_2', 'tile_3_4', 'tile_2_2', 'tile_4_2', 'tile_2_3', 'tile_4_3'], 'counters': None}, 'tile_3_2': {'player': None, 'neighbours': ['tile_3_1', 'tile_3_3', 'tile_2_1', 'tile_4_1', 'tile_2_2', 'tile_4_2'], 'counters': None}, 'tile_3_1': {'player': None, 'neighbours': ['tile_3_0', 'tile_3_2', 'tile_2_0', 'tile_4_0', 'tile_2_1', 'tile_4_1'], 'counters': None}, 'tile_3_0': {'player': None, 'neighbours': ['tile_3_1', 'tile_2_0', 'tile_4_0'], 'counters': None}, 'tile_3_6': {'player': None, 'neighbours': ['tile_3_5', 'tile_2_5', 'tile_4_5'], 'counters': None}, 'tile_3_5': {'player': None, 'neighbours': ['tile_3_4', 'tile_3_6', 'tile_2_4', 'tile_4_4', 'tile_2_5', 'tile_4_5'], 'counters': None}, 'tile_3_4': {'player': None, 'neighbours': ['tile_3_3', 'tile_3_5', 'tile_2_3', 'tile_4_3', 'tile_2_4', 'tile_4_4'], 'counters': None}, 'tile_2_2': {'player': None, 'neighbours': ['tile_2_1', 'tile_2_3', 'tile_3_2', 'tile_3_3', 'tile_1_1', 'tile_1_2'], 'counters': None}, 'tile_2_3': {'player': None, 'neighbours': ['tile_2_2', 'tile_2_4', 'tile_3_3', 'tile_3_4', 'tile_1_2', 'tile_1_3'], 'counters': None}, 'tile_2_0': {'player': None, 'neighbours': ['tile_2_1', 'tile_3_0', 'tile_3_1', 'tile_1_0'], 'counters': None}, 'tile_2_1': {'player': None, 'neighbours': ['tile_2_0', 'tile_2_2', 'tile_3_1', 'tile_3_2', 'tile_1_0', 'tile_1_1'], 'counters': None}, 'tile_2_4': {'player': None, 'neighbours': ['tile_2_3', 'tile_2_5', 'tile_3_4', 'tile_3_5', 'tile_1_3', 'tile_1_4'], 'counters': None}, 'tile_2_5': {'player': None, 'neighbours': ['tile_2_4', 'tile_3_5', 'tile_3_6', 'tile_1_4'], 'counters': None}, 'tile_5_1': {'player': None, 'neighbours': ['tile_5_0', 'tile_5_2', 'tile_4_1', 'tile_4_2', 'tile_6_0', 'tile_6_1'], 'counters': None}, 'tile_5_0': {'player': None, 'neighbours': ['tile_5_1', 'tile_4_0', 'tile_4_1', 'tile_6_0'], 'counters': None}, 'tile_5_3': {'player': None, 'neighbours': ['tile_5_2', 'tile_5_4', 'tile_4_3', 'tile_4_4', 'tile_6_2', 'tile_6_3'], 'counters': None}, 'tile_5_2': {'player': None, 'neighbours': ['tile_5_1', 'tile_5_3', 'tile_4_2', 'tile_4_3', 'tile_6_1', 'tile_6_2'], 'counters': None}, 'tile_5_4': {'player': None, 'neighbours': ['tile_5_3', 'tile_4_4', 'tile_4_5', 'tile_6_3'], 'counters': None}, 'tile_4_0': {'player': None, 'neighbours': ['tile_4_1', 'tile_3_0', 'tile_3_1', 'tile_5_0'], 'counters': None}, 'tile_4_1': {'player': None, 'neighbours': ['tile_4_0', 'tile_4_2', 'tile_3_1', 'tile_3_2', 'tile_5_0', 'tile_5_1'], 'counters': None}, 'tile_4_2': {'player': None, 'neighbours': ['tile_4_1', 'tile_4_3', 'tile_3_2', 'tile_3_3', 'tile_5_1', 'tile_5_2'], 'counters': None}, 'tile_4_3': {'player': None, 'neighbours': ['tile_4_2', 'tile_4_4', 'tile_3_3', 'tile_3_4', 'tile_5_2', 'tile_5_3'], 'counters': None}, 'tile_4_4': {'player': None, 'neighbours': ['tile_4_3', 'tile_4_5', 'tile_3_4', 'tile_3_5', 'tile_5_3', 'tile_5_4'], 'counters': None}, 'tile_4_5': {'player': None, 'neighbours': ['tile_4_4', 'tile_3_5', 'tile_3_6', 'tile_5_4'], 'counters': None}, 'tile_6_2': {'player': None, 'neighbours': ['tile_6_1', 'tile_6_3', 'tile_5_2', 'tile_5_3'], 'counters': None}, 'tile_6_3': {'player': None, 'neighbours': ['tile_6_2', 'tile_5_3', 'tile_5_4'], 'counters': None}}

    '''
    board structure:
    :param board:
        The current state of the board. This is a dict of the form::
            {
                <tile id>: {
                    'counters': <number of counters on tile or None>,
                    'player': <player id of the player who holds the tile or None>,
                    'neighbours': <list of ids of neighbouring tile>
                },
                ...
            }
    :param game_id:
        The id of the game that the algo is playing in.
        This is a UUID object
    :param player_id:
        The id of the player that the algo is playing on behalf of.
        This is an integer [0,1]
    :returns:
        The id of a tile the algo wishes to place a counter in.
        This is a string of the format "tile_4_2"
    '''
    # Make player_id into player 1 (algo) and player -1 (enemy)
    #(player_id * 2 -1) * -1

    ### LIBRARIES:
    from sys import maxsize

    ### ISSUES:
    # Currently will stop at move 1 because game over condition is met

    ### PARAMETERS:
    depth = 3

    if (player_id == 0):
        me = 0
        enemy = 1
    elif (player_id == 1):
        me = 1
        enemy = 0


    # Get board state as simple score list
    def GetScores(board, me, enemy):
        n = -1
        scores = [0] * len(board)
        for tile_id, tile in board.items():
            n += 1
            if (tile["player"] == None):
                scores[n] = 0
                continue
            elif (tile["player"] == me):
                scores[n] = tile["counters"]
            elif (tile["player"] == enemy):
                scores[n] = tile["counters"] * -1
        return(scores)


    # Value function
    def ValueFunction(scores):
        n_tiles = sum(x > 0 for x in scores)
        n_counters = sum([x for x in scores if x > 0])
        n_enemy_tiles = sum(x < 0 for x in scores)
        n_enemy_counters = abs(sum([x for x in scores if x < 0]))
        if (n_counters == 0):
            return maxsize * -1
        elif (n_enemy_counters == 0):
            return maxsize
        elif ((n_counters > 0) and (n_enemy_counters > 0)):
            return n_tiles + n_counters - n_enemy_tiles - n_enemy_counters
        else:
            print("Error")


    # If one player has won, stop simulating
    def GameOver(scores):
        if (sum([x for x in scores if x > 0]) == 0):
            return True
        elif (sum([x for x in scores if x < 0]) == 0):
            return True
        elif ((sum([x for x in scores if x > 0]) > 0) and (sum([x for x in scores if x < 0]) >0)):
            return False


    # Simulate a move and evaluate resulting board state.
    # board is the board state,
    # move is a valid tile_id to place the counter on,
    # player is 0 or 1 depending whose turn it is.
    def AddCounter(board_simulate, player_id, move):
        tile = board_simulate[move]
        counters = (tile["counters"] if tile["counters"] else 0) + 1
        # If the field is full, HEXPLODE!
        if counters == len(tile["neighbours"]):
            tile["player"] = None
            tile["counters"] = None
            for neighbour in tile["neighbours"]:
                AddCounter(board_simulate, player_id, neighbour)
        # Else: just change player and counters
        else:
            tile["player"] = player_id
            tile["counters"] = counters
        return board_simulate


### MINMAX APPROACH
# Make node for one possible move.
# player_id is the player making the move.
# depth is the depth of the current node
class Node(object):
    def __init__(self, player_id, board_current, depth):
        self.player_id = player_id
        if (player_id == 0):
            self.me = 0
            self.enemy = 1
        else:
            self.me = 1
            self.enemy = 0
        self.board_current = board_current
        self.depth = depth
        self.scores = GetScores(self.board_current, self.me, self.enemy)
        self.value = ValueFunction(self.scores)
        self.children = []
        self.CreateChildren()
    def CreateChildren(self):
        if self.depth > 0:
            for tile_id, tile in self.board_current.items():
                if tile["player"] is None or tile["player"] == self.player_id:
                    board_future = self.board_current
                    print("passing to board: Player " + str(self.me) + " Tile " + str(tile_id) + " Depth " + str(self.depth - 1) + ", Score: " + str(self.scores))
                    board_future = AddCounter(board_future, self.me, tile_id)
                    self.children.append(Node(enemy, board_future, self.depth -1))
                    del board_future


node = Node(me, board, depth)
### TEST:
board = {'tile_1_3': {'player': 0, 'neighbours': ['tile_1_2', 'tile_1_4', 'tile_2_3', 'tile_2_4', 'tile_0_2', 'tile_0_3'], 'counters': 2}, 'tile_6_1': {'player': 1, 'neighbours': ['tile_6_0', 'tile_6_2', 'tile_5_1', 'tile_5_2'], 'counters': 2}, 'tile_1_4': {'player': None, 'neighbours': ['tile_1_3', 'tile_2_4', 'tile_2_5', 'tile_0_3'], 'counters': None}, 'tile_1_1': {'player': None, 'neighbours': ['tile_1_0', 'tile_1_2', 'tile_2_1', 'tile_2_2', 'tile_0_0', 'tile_0_1'], 'counters': None}, 'tile_1_0': {'player': None, 'neighbours': ['tile_1_1', 'tile_2_0', 'tile_2_1', 'tile_0_0'], 'counters': None}, 'tile_6_0': {'player': None, 'neighbours': ['tile_6_1', 'tile_5_0', 'tile_5_1'], 'counters': None}, 'tile_1_2': {'player': None, 'neighbours': ['tile_1_1', 'tile_1_3', 'tile_2_2', 'tile_2_3', 'tile_0_1', 'tile_0_2'], 'counters': None}, 'tile_0_0': {'player': None, 'neighbours': ['tile_0_1', 'tile_1_0', 'tile_1_1'], 'counters': None}, 'tile_0_1': {'player': None, 'neighbours': ['tile_0_0', 'tile_0_2', 'tile_1_1', 'tile_1_2'], 'counters': None}, 'tile_0_2': {'player': None, 'neighbours': ['tile_0_1', 'tile_0_3', 'tile_1_2', 'tile_1_3'], 'counters': None}, 'tile_0_3': {'player': None, 'neighbours': ['tile_0_2', 'tile_1_3', 'tile_1_4'], 'counters': None}, 'tile_3_3': {'player': None, 'neighbours': ['tile_3_2', 'tile_3_4', 'tile_2_2', 'tile_4_2', 'tile_2_3', 'tile_4_3'], 'counters': None}, 'tile_3_2': {'player': None, 'neighbours': ['tile_3_1', 'tile_3_3', 'tile_2_1', 'tile_4_1', 'tile_2_2', 'tile_4_2'], 'counters': None}, 'tile_3_1': {'player': None, 'neighbours': ['tile_3_0', 'tile_3_2', 'tile_2_0', 'tile_4_0', 'tile_2_1', 'tile_4_1'], 'counters': None}, 'tile_3_0': {'player': None, 'neighbours': ['tile_3_1', 'tile_2_0', 'tile_4_0'], 'counters': None}, 'tile_3_6': {'player': None, 'neighbours': ['tile_3_5', 'tile_2_5', 'tile_4_5'], 'counters': None}, 'tile_3_5': {'player': None, 'neighbours': ['tile_3_4', 'tile_3_6', 'tile_2_4', 'tile_4_4', 'tile_2_5', 'tile_4_5'], 'counters': None}, 'tile_3_4': {'player': None, 'neighbours': ['tile_3_3', 'tile_3_5', 'tile_2_3', 'tile_4_3', 'tile_2_4', 'tile_4_4'], 'counters': None}, 'tile_2_2': {'player': None, 'neighbours': ['tile_2_1', 'tile_2_3', 'tile_3_2', 'tile_3_3', 'tile_1_1', 'tile_1_2'], 'counters': None}, 'tile_2_3': {'player': None, 'neighbours': ['tile_2_2', 'tile_2_4', 'tile_3_3', 'tile_3_4', 'tile_1_2', 'tile_1_3'], 'counters': None}, 'tile_2_0': {'player': None, 'neighbours': ['tile_2_1', 'tile_3_0', 'tile_3_1', 'tile_1_0'], 'counters': None}, 'tile_2_1': {'player': None, 'neighbours': ['tile_2_0', 'tile_2_2', 'tile_3_1', 'tile_3_2', 'tile_1_0', 'tile_1_1'], 'counters': None}, 'tile_2_4': {'player': None, 'neighbours': ['tile_2_3', 'tile_2_5', 'tile_3_4', 'tile_3_5', 'tile_1_3', 'tile_1_4'], 'counters': None}, 'tile_2_5': {'player': None, 'neighbours': ['tile_2_4', 'tile_3_5', 'tile_3_6', 'tile_1_4'], 'counters': None}, 'tile_5_1': {'player': None, 'neighbours': ['tile_5_0', 'tile_5_2', 'tile_4_1', 'tile_4_2', 'tile_6_0', 'tile_6_1'], 'counters': None}, 'tile_5_0': {'player': None, 'neighbours': ['tile_5_1', 'tile_4_0', 'tile_4_1', 'tile_6_0'], 'counters': None}, 'tile_5_3': {'player': None, 'neighbours': ['tile_5_2', 'tile_5_4', 'tile_4_3', 'tile_4_4', 'tile_6_2', 'tile_6_3'], 'counters': None}, 'tile_5_2': {'player': None, 'neighbours': ['tile_5_1', 'tile_5_3', 'tile_4_2', 'tile_4_3', 'tile_6_1', 'tile_6_2'], 'counters': None}, 'tile_5_4': {'player': None, 'neighbours': ['tile_5_3', 'tile_4_4', 'tile_4_5', 'tile_6_3'], 'counters': None}, 'tile_4_0': {'player': None, 'neighbours': ['tile_4_1', 'tile_3_0', 'tile_3_1', 'tile_5_0'], 'counters': None}, 'tile_4_1': {'player': None, 'neighbours': ['tile_4_0', 'tile_4_2', 'tile_3_1', 'tile_3_2', 'tile_5_0', 'tile_5_1'], 'counters': None}, 'tile_4_2': {'player': None, 'neighbours': ['tile_4_1', 'tile_4_3', 'tile_3_2', 'tile_3_3', 'tile_5_1', 'tile_5_2'], 'counters': None}, 'tile_4_3': {'player': None, 'neighbours': ['tile_4_2', 'tile_4_4', 'tile_3_3', 'tile_3_4', 'tile_5_2', 'tile_5_3'], 'counters': None}, 'tile_4_4': {'player': None, 'neighbours': ['tile_4_3', 'tile_4_5', 'tile_3_4', 'tile_3_5', 'tile_5_3', 'tile_5_4'], 'counters': None}, 'tile_4_5': {'player': None, 'neighbours': ['tile_4_4', 'tile_3_5', 'tile_3_6', 'tile_5_4'], 'counters': None}, 'tile_6_2': {'player': None, 'neighbours': ['tile_6_1', 'tile_6_3', 'tile_5_2', 'tile_5_3'], 'counters': None}, 'tile_6_3': {'player': None, 'neighbours': ['tile_6_2', 'tile_5_3', 'tile_5_4'], 'counters': None}}
board = AddCounter(scores, board, move="tile_2_3", player_id=0)
board = AddCounter(scores, board, move="tile_4_3", player_id=1)
scores = GetScores(board = board, me = me, enemy = enemy)
value = ValueFunction(scores)


    #ALGORITHM
    def MinMax(node, i_depth, i_playerNum):
        if (i_depth == 0) or (abs(node.i_value) == maxsize):
            return node.i_value

        i_bestValue = maxsize * -i_playerNum

        for i in range(len(node.children)):
            child = node.children[i]
            i_val = MinMax(child, i_depth - 1, -i_playerNum)
            if (abs(maxsize * i_playerNum - i_val) < abs(maxsize * i_playerNum - i_bestValue)):
                i_bestValue = i_val

        return i_bestValue


    #ALGORITHM
    def MinMax(node, i_depth, i_playerNum):
        if (i_depth == 0) or (abs(node.i_value) == maxsize):
            return node.i_value

        i_bestValue = maxsize * -i_playerNum

        for i in range(len(node.children)):
            child = node.children[i]
            i_val = MinMax(child, i_depth - 1, -i_playerNum)
            if (abs(maxsize * i_playerNum - i_val) < abs(maxsize * i_playerNum - i_bestValue)):
                i_bestValue = i_val

        return i_bestValue



@weighting_function_one_algo.on_start_game
def start_game(game_id, player_id, boardsize, opponent_id):
    '''
    Example implementation of a start game handler for an algo player in the
    game Hexplode. Your algo does not need to implement this event handler but
    may choose to do so if any form of pre-game preparation or processing is
    required.

    The function takes the the id of the game the algo will be playing in, the
    id of the player the algo will play for, the board size and the id of the
    opposing algorithm. No return value is expected.

    This example algo implementation does not actually need to perform any steps
    at the start of the game but uses the event as a opportunity to update its own
    score of how many game it has played.

    :param game_id:
        The id of the game that the algo was playing in.
    :param player_id:
        The id of the player that the algo was playing on behalf of.
    :param boardsize:
        The board will be a hexagon with side <boardsize> tiles.
    :param opponent_id:
        The id of the opposing algorithm, will be 'Human' if the opponent is
        not an algo player.
    '''
    global games_played
    games_played += 1


games_played = 0


@weighting_function_one_algo.on_game_over
def game_over(board, game_id, player_id, winner_id):
    '''
    Example implementation of a game over handler for an algo player in the game
    Hexplode. Your algo does not need to implement this event handler but may
    choose to do so if any form of post game clean-up or processing is required.

    The function takes the final board state, the id of the game the algo was
    playing in, the id of the player the algo was playing for and the id of the
    winning player. No return value is expected.

    This example algo implementation does not actually need to perform any steps
    at the end of the game but uses the event as a opportunity to update its own
    score of how well it is doing.

    :param board:
        The final state of the board. This is a dict of the form::
            {
                <tile id>: {
                    'counters': <number of counters on tile or None>,
                    'player': <player id of the player who holds the tile or None>,
                    'neighbours': <list of ids of neighbouring tile>
                },
                ...
            }
    :param game_id:
        The id of the game that the algo was playing in.
    :param player_id:
        The id of the player that the algo was playing on behalf of.
    :param winner_id:
        The id of the winning player.
    '''
    global games_won
    if winner_id == player_id:
        games_won += 1


games_won = 0
