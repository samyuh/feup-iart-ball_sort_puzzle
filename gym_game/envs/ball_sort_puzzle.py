from itertools import permutations 
from math import perm

class BallSortPuzzle:
    """
    Class to apply the game mechanics of the Ball Sort Puzzle
    """
    def __init__(self, board, bottle_size, num_bottles):
        """
        Constructor for the BallSortPuzzle object

        Attributes
        ----------
        
        board : list of lists
            - list of lists representing the game
        
        bottle_size : int
            - number of balls that can fit in each bottle
        
        num_bottles : int
            - number of bottles in the game
        
        actions : Action
            - permutations of possible actions in the game

        states : List
            - List of Game States
        
        numStatesDiscovered : int
            - Number of discovered Stares
        

        """
        self.board = board
        self.bottle_size = bottle_size
        self.num_bottles = num_bottles

        self.actions = self.getActions()

        self.states = {}
        self.numStatesDiscovered = 0

        self.alreadyFull = 0
    
    def getState(self):
        """
        Returns the game state
        """
        tup = tuple(tuple(sub) for sub in self.board)
        if tup not in self.states.keys():    
            self.states[tup] = self.numStatesDiscovered
            self.numStatesDiscovered += 1
            return self.states[tup]
        else:
            return self.states[tup]

    def applyMovement(self, action):
        """
        Applies a given action to the game

        Parameter
        ---------

        action : Action
            - Action to be applied 
        
        Returns
        -------

        int - reward of the applied movement

        """
        action = self.actions[action]
        # Get pieces to toggle
        first, second = self.pickPiece(self.board[action[0]]), self.getFirstEmpty(self.board[action[1]])

        # Invalid Move
        if first == -1 or second == -1:
             return self.calculateReward() - 10

        # Get Color to Swap
        color = self.board[action[0]][first]
        # Invalid Move: a ball must be placed on top of a ball of the same color or on an empty tube
        if not self.checkColor(color, self.board[action[1]], second-1):
             return self.calculateReward() - 10

        # Do the action
        self.board[action[0]][first] = 0
        self.board[action[1]][second] = color

        return self.calculateReward()


    def calculateReward(self):
        """
        Calculates the rewards from the game

        Returns
        -------
        int - reward value of the game

        """
        value = 0
        for tubeIdx, tube in enumerate(self.board):
            prevBall = -1
            for idx, ball in enumerate(tube):
                if prevBall != -1 and prevBall != ball and ball != 0:
                    for i in range(idx, len(tube)):
                        if tube[i] != 0:
                            value -= 1
                    break
                prevBall = ball
        return value

    def checkColor(self, color, bottle, index):
        """
        Check the color on a certain place

        Parameters
        ----------

        color : int
            - color of the ball to check
        
        bottle : int
            - bottle to check for the ball

        index : int
            - index of the bottle to check for the color

        Returns
        -------

        bool - True if the color of the ball is the same as the one given by the parameters

        """
        if index == -1:
            return True
        if color == bottle[index]:
            return True
        return False
    
    def pickPiece(self, targetBoard):
        """
        Select a Piece from the top of the bottle

        targetBoard - list of int
            - game bottle to select the piece from
        
        Returns
        -------
        int - returns the selected piece, if found

        """
        for idx, i in enumerate(targetBoard):
            if i == 0:
                return idx - 1
        return self.bottle_size - 1

    def getFirstEmpty(self, targetBoard):
        """
        returns the first empty space on the bottle

        argetBoard - list of int
            - game bottle to select the piece from

        Returns
        -------

        int - the index of the first empty place in the bottle

        """
        for idx, i in enumerate(targetBoard):
            if i == 0:
                return idx
        return -1

    def isGoal(self):
        """
        Cheks if the game puzzle has been solved

        Returns
        -------

        bool - true if it the puzzle has been solved, false otherwise

        """
        for i in self.board:
            if not all(element == i[0] for element in i):
                return False
        return True
    
    def getActions(self):
        """
        Returns a list of permutations of all actions of the game
        """
        l = list(permutations(list(range(0, self.num_bottles)), 2))
        return dict(zip(range(len(l)),l))

    def isStuck(self):
        """
        Verifiies if the player entered a stuck state of the game, losing

        Returns
        -------

        bool - true if the player is stuck, false otherwise
        """
        isStuck = True
        allActions = list(permutations(list(range(0, self.num_bottles)), 2))
        for a in allActions:
            if a[0] == a[1]:
                continue
            first, second = self.pickPiece(self.board[a[0]]), self.getFirstEmpty(self.board[a[1]])
            if first == -1 or second == -1:
                continue
            color = self.board[a[0]][first]
            if not self.checkColor(color, self.board[a[1]], second-1):
                continue
            return False
        return isStuck

    def getValid(self):
        """
        Returns all valid actions from the game

        Returns
        -------

        List of actions - Returns a list of valid actions from the game
        """
        numActions = perm(self.num_bottles, 2)
        validActions = []

        for num in range(numActions):
            action = self.actions[num]
            # Get pieces to toggle
            first, second = self.pickPiece(self.board[action[0]]), self.getFirstEmpty(self.board[action[1]])

            # Invalid Move
            if first == -1 or second == -1:
                continue

            # Get Color to Swap
            color = self.board[action[0]][first]
            # Invalid Move: a ball must be placed on top of a ball of the same color or on an empty tube
            if not self.checkColor(color, self.board[action[1]], second-1):
                continue

            validActions.append(num)

        return validActions

        
