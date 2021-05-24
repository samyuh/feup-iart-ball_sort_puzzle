
# -- Imports -- #
import gym
import numpy as np

# -- Personal Imports -- #
from math import perm, comb, factorial
from copy import deepcopy
from gym_game.envs.ball_sort_puzzle import BallSortPuzzle

class BallSortEnv(gym.Env):
    """
    clas to represent the Ball Sort Puzzle environment
    """
    metadata = {'render.modes': ['human']}

    def __init__(self, board, max_steps, bottle_size, num_bottles, empty_spaces, num_balls, ball_per_color, num_colors):
        self.orig_board = board
        self.max_steps = max_steps
        self.bottle_size = bottle_size
        self.num_bottles = num_bottles

        self.empty_spaces = empty_spaces
        self.num_balls = num_balls
        self.ball_per_color = ball_per_color
        self.num_colors = num_colors

        # Action Space
        # (Z) ->
        #  Which is mapped to a value (X, Y), where: 
        #       X is the bottle the ball is picked
        #       Y is the bottle the ball is put on
        self.action_space = gym.spaces.Discrete(perm(self.num_bottles, 2))

        # Observation Space
        # Number of States
        empty_spaces = self.emptySpacesComb(self.empty_spaces, self.num_bottles, self.bottle_size) 
        ball_permutations = comb(self.num_balls, self.ball_per_color) / self.num_balls
        value = int(empty_spaces * ball_permutations)

        self.observation_space = gym.spaces.Discrete(value)

        # Init Game
        self.reset()

    def emptySpacesComb(self, n, k, w):
        """
        Number of ways to put n identic balls, in k bottles each one with capacity of w
        Source: https://math.stackexchange.com/questions/620640/stars-and-bars-with-restriction-of-size-between-bars-via-generating-functions
        """

        firstSeries = []
        secondSeries = []
        valueList = []
        factor = w + 1

        for i in range(k + 1):
            value = comb(10, i) * pow(-1, i)
            firstSeries.append(value)
        
        for i in range(n + 1):
            value = factorial(k + i - 1) / (factorial(k - 1) * factorial(i))
            secondSeries.append(int(value))

        result = 0
        for idx, i in enumerate(firstSeries):
            currentFactor = factor * idx
            missingFactor = n - currentFactor

            if currentFactor <= n and missingFactor >= 0:
                valueList.append(i * secondSeries[missingFactor])

        return sum(valueList)

    def argMax(self, validMoves, q_table_line):
        """
        Get the action with maximum value

        validMoves : list of Moves
            - List containing all the valid moves
        
        q_table_line : List
            - Single q_table row
        """
        action = np.argmax(q_table_line)

        stateValues = q_table_line.argsort()[::-1]
        for i in stateValues:
            if i in validMoves:
                return i

        return action    


    def validSample(self, validMoves):
        """
        Action validation

        validMoves : list of Moves
            - List containing all the valid moves
        """
        action = self.action_space.sample()
        if action not in validMoves:
            return np.random.choice(validMoves)
        
        return action


    def step(self, action):
        """
        Apply movement in the game

        action : action
            - ACtion to be executed

        """
        self.iteration += 1

        reward = self.game.applyMovement(action)
        done = self.game.isGoal()
        stuck = self.game.isStuck()
        state = self.game.getState()

        if done: reward = self.num_balls

        over = True if self.iteration > self.max_steps else False

        return state, reward, done or stuck or over, {"state" : self.game.board}
    
    def render(self, mode="human", close=False):
        """
        Print the game
        """
        print("Bottles - Move {}".format(self.iteration))
        for idx in range(self.bottle_size):
            for bottle_num in range(self.num_bottles):
                print("|" + str(self.game.board[bottle_num][self.bottle_size - idx - 1]) + "|", end="")
            print("\n", end="")

    def reset(self):
        """
        Reset the game
        """
        board_copy = deepcopy(self.orig_board)
        self.game = BallSortPuzzle(board_copy, self.bottle_size, self.num_bottles)

        self.iteration = 0
        self.state = 0
        self.done = False    

        return self.state