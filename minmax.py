from hexplode import algo_player
from sys import maxsize
from copy import copy

@algo_player(name="Minimax",
             description="assigning values to positions")

def Minimax(board, game_id, player_id):

    def CalculateScores(board, player_id):
        scores = {}
        for tile_id, tile in board.items():
            if tile["player"] == None:
                scores[tile_id] = 0
            elif tile["player"] == player_id:
                scores[tile_id] = int(tile["counters"])
            elif tile["player"] is not player_id:
                scores[tile_id] = int(tile["counters"]) * -1
        return(scores)


    def CalculateValue(scores, player_id):
        """Heuristic value function to estimate how favourable
        the given board state is for the player"""

        # count counters
        OwnCounters = 0
        EnemyCounters = 0
        for tile_id in scores:
            if scores[tile_id] > 0:
                OwnCounters += abs(scores[tile_id])
            elif scores[tile_id] < 0:
                EnemyCounters += abs(scores[tile_id])
        # Check for game-over
        if OwnCounters == 0:
            #Lost
            return(-maxsize)
        elif EnemyCounters == 0:
            #Won
            return(maxsize)
        else:
            value = OwnCounters - EnemyCounters
            return(value)


    def AddCounter(scores, board, tile_id, player_id, player_current):
        if (True in [score > 0 for score in scores.values()]) and (True in [score < 0 for score in scores.values()]):
            #If player, counters are positive
            if player_current == player_id:
                add = +1
            #If enemy, counters are negative
            else:
                add = -1
            #If placing counter on own tile, increase counters
            if (add > 0 and scores[tile_id] >= 0) or (add < 0 and scores[tile_id] <= 0):
                counter = scores[tile_id] + add
            #If placing counter on enemy tile, change and increase counters
            else:
                counter = (scores[tile_id] * -1) + add
            #If field full, hexplode (recursive)
            if abs(counter) == len(board[tile_id]["neighbours"]):
                scores[tile_id] = 0
                for neighbour in board[tile_id]["neighbours"]:
                    scores = AddCounter(scores, board, neighbour, player_id, player_current)
            else:
                scores[tile_id] = counter
            return(scores)
        else:
            return(scores)
            
            
    class Node(object):
        
        def __init__(self, board, player_id, player_current, scores, depth, move=None):
            self.player_current = player_current
            self.move = move
            self.scores = scores

            #Check if game is over
            if (True in [score > 0 for score in self.scores.values()]) and (True in [score < 0 for score in self.scores.values()]):
                self.depth = depth
            else:
                self.depth = 0

            #If this is not a terminal node, generate the children
            if self.depth > 0:
                #Prefix for use with score
                if (self.player_current == player_id):
                    self.prefix = 1
                else:
                    self.prefix = -1
                self.children = []
                self.CreateChildren(scores)

            #If this is terminal node, calculate value
            elif self.depth == 0:
                #Get Value
                self.value = CalculateValue(scores, player_id)

        def CreateChildren(self, scores):
            for tile_id in scores.keys():
                if ((scores[tile_id] >= 0) and (self.prefix > 0)) or ((scores[tile_id] <= 0) and (self.prefix < 0)):
                    future_scores = copy(scores)
                    future_scores = AddCounter(future_scores, board, tile_id, player_id, self.player_current)
                    self.children.append(Node(
                        board,
                        player_id,
                        (self.player_current + 1) % 2,
                        future_scores,
                        self.depth -1,
                        tile_id))


    def Maxvalue(node):
        """Function to identify most advantageous player move"""
        if (node.depth == 0):
            return node.value
        else:
            best_value = -maxsize
            for child in node.children:
                best_value = max(best_value, Minvalue(child))
            return best_value

    def Minvalue(node):
        """Function to identify most likely enemy move"""
        if (node.depth == 0):
            return node.value
        else:
            best_value = maxsize
            for child in node.children:
                best_value = min(best_value, Maxvalue(child))
            return best_value


    # Run algorithm
    depth = 4
    scores = CalculateScores(board, player_id)
    moves = sum([abs(score) for score in scores.values()])

    # If the game is only starting, pick first tile
    if moves < 2:
        possible_moves = {}
        for tile_id, tile in board.items():
            if tile["player"] is None:
                possible_moves.setdefault(len(tile["neighbours"]), []).append(tile_id)
        # Pick the moves closest to an explosion
        best_move = possible_moves[min(possible_moves)][2]

        return best_move

    else:
        node_tree = Node(board, player_id, player_id, scores, depth)
        candidate_moves = {}
        for child in node_tree.children:
            candidate_moves[child.move] = Minvalue(child)
        best_move = max(candidate_moves.keys(), key=(lambda k: candidate_moves[k]))

        return best_move

