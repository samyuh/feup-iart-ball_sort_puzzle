from itertools import permutations 
from math import perm

class BallSortPuzzle:
    def __init__(self, board, bottle_size, num_bottles):
        self.board = board
        self.bottle_size = bottle_size
        self.num_bottles = num_bottles

        self.actions = self.getActions()

        self.states = {}
        self.numStatesDiscovered = 0

        self.alreadyFull = 0
    
    def getState(self):
        tup = tuple(tuple(sub) for sub in self.board)
        if tup not in self.states.keys():    
            self.states[tup] = self.numStatesDiscovered
            self.numStatesDiscovered += 1
            return self.states[tup]
        else:
            return self.states[tup]

    def applyMovement(self, action):
        action = self.actions[action]
        # Get pieces to toggle
        first, second = self.pickPiece(self.board[action[0]]), self.getFirstEmpty(self.board[action[1]])

        # Invalid Move
        if first == -1 or second == -1:
            return -26*2

        # Get Color to Swap
        color = self.board[action[0]][first]
        # Invalid Move: a ball must be placed on top of a ball of the same color or on an empty tube
        if not self.checkColor(color, self.board[action[1]], second-1):
            return -26*2

        # Do the action
        self.board[action[0]][first] = 0
        self.board[action[1]][second] = color

        return self.calculateReward()

    def checkColor(self, color, bottle, index):
        if index == -1:
            return True
        if color == bottle[index]:
            return True
        return False
    
    def pickPiece(self, targetBoard):
        for idx, i in enumerate(targetBoard):
            if i == 0:
                return idx - 1
        return self.bottle_size - 1

    def getFirstEmpty(self, targetBoard):
        for idx, i in enumerate(targetBoard):
            if i == 0:
                return idx
        return -1

    def calculateReward(self):
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

        numCurrentFull = 0
        for i in self.board:
            if not all(element == i[0] for element in i) and i[0] != 0:
                numCurrentFull += 1

        if self.alreadyFull < numCurrentFull:
            value = numCurrentFull - self.alreadyFull
            self.alreadyFull = numCurrentFull

        return value

    def isGoal(self):
        for i in self.board:
            if not all(element == i[0] for element in i):
                return False
        return True
    
    def getActions(self):
        l = list(permutations(list(range(0, self.num_bottles)), 2))
        return dict(zip(range(len(l)),l))

    def isStuck(self):
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
