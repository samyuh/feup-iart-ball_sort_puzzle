
import gym
import numpy as np
import itertools

from math import factorial, perm

class BallSortPuzzle():
    def __init__(self, board, bottle_size, num_bottles):
        self.board = board
        self.bottle_size = bottle_size
        self.num_bottles = num_bottles

        self.actions = self.getActions()

        self.states = {}
        self.numStatesDiscovered = 0
    
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
            return -999

        # Get Color to Swap
        color = self.board[action[0]][first]
        # Invalid Move: a ball must be placed on top of a ball of the same color or on an empty tube
        if not self.checkColor(color, self.board[action[1]], second-1):
            return -999

        # Do the action
        self.board[action[0]][first] = 0
        self.board[action[1]][second] = color

        # print("heuristic = ", self.heuristic())
        return self.heuristic()

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

    def heuristic(self):
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

    def isGoal(self):
        for i in self.board:
            if len(i) == 0:
                continue
            if not all(element == i[0] for element in i):
                return False
        return True
    
    def getActions(self):
        l = list(itertools.permutations(list(range(0, self.num_bottles)), 2))
        return dict(zip(range(len(l)),l))

    def isStuck(self):
        isStuck = True
        allActions = list(itertools.permutations(list(range(0, self.num_bottles)), 2))
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


class BallSortEnv(gym.Env):
    def __init__(self):
        self.bottle_size = 3
        self.num_bottles = 3

        # Action Space
        # (Z) ->
        #  Which is mapped to a value (X, Y), where: 
        #       X is the bottle the ball is picked
        #       Y is the bottle the ball is put on
        self.action_space = gym.spaces.Discrete(perm(self.num_bottles, 2))

        # Observation Space
        # Number of States
        self.observation_space = gym.spaces.Discrete(99999)

        # Observation Space - 
        # TODO: Find a way to get the exact number os states
        # value = 1
        # k = BOTTLE_SIZE
        # for i in range(BOTTLE_SIZE-1):
        #     n = (NUM_BOTTLES*BOTTLE_SIZE - BOTTLE_SIZE * i)
        #     value *= factorial(n) / (factorial(k) * factorial(n - k))
        
        # print(value)
        #self.observation_space = gym.spaces.Discrete(int(value))

        # Init Game
        self.reset()
 
    def step(self, action):
        #assert self.action_space.contains(action)

        reward = self.game.applyMovement(action)
        done = self.game.isGoal()
        stuck = self.game.isStuck()
        state = self.game.getState()

        if done:
            reward = 10
        elif stuck:
            reward = -10
        
        self.iteration += 1
        
        return state, reward, done or stuck, self.game.board
    
    def render(self, mode="human", close=False):
        print("Bottles - Move {}".format(self.iteration))
        for idx in range(self.bottle_size):
            for bottle_num in range(self.num_bottles):
                print("|" + str(self.game.board[bottle_num][self.bottle_size - idx - 1]) + "|", end="")
            print("\n", end="")

    def reset(self):
        self.game = BallSortPuzzle([[1, 2, 1], [1, 2, 2], [0, 0, 0]], self.bottle_size, self.num_bottles)

        self.iteration = 0
        self.state = 0
        self.done = False    

        return self.state