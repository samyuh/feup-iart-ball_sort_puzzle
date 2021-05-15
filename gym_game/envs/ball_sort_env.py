
import gym

from math import perm, factorial
from copy import deepcopy
from gym_game.envs.ball_sort_puzzle import BallSortPuzzle

class BallSortEnv(gym.Env):
    def __init__(self, board, bottle_size, num_bottles):
        self.orig_board = board
        self.bottle_size = bottle_size
        self.num_bottles = num_bottles

        # Action Space
        # (Z) ->
        #  Which is mapped to a value (X, Y), where: 
        #       X is the bottle the ball is picked
        #       Y is the bottle the ball is put on
        self.action_space = gym.spaces.Discrete(perm(self.num_bottles, 2))

        # Observation Space
        # Number of States
        # TODO: Find a way to get the exact number os states
        value = 1
        k = self.bottle_size
        for i in range(self.bottle_size-1):
            n = (self.num_bottles*self.bottle_size - self.bottle_size * i)
            value *= factorial(n) / (factorial(k) * factorial(n - k))
        
        print(value)
        self.observation_space = gym.spaces.Discrete(30000000)

        # Init Game
        self.reset()
 
    def step(self, action):
        reward = self.game.applyMovement(action)
        done = self.game.isGoal()
        stuck = self.game.isStuck()
        state = self.game.getState()

        if done: reward = 10
        elif stuck: reward = -10
        
        self.iteration += 1
        
        return state, reward, done or stuck, self.game.board
    
    def render(self, mode="human", close=False):
        print("Bottles - Move {}".format(self.iteration))
        for idx in range(self.bottle_size):
            for bottle_num in range(self.num_bottles):
                print("|" + str(self.game.board[bottle_num][self.bottle_size - idx - 1]) + "|", end="")
            print("\n", end="")

    def reset(self):
        # TODO: check if orig board is the same at start of each episode
        board_copy = deepcopy(self.orig_board)
        self.game = BallSortPuzzle(board_copy, self.bottle_size, self.num_bottles)

        self.iteration = 0
        self.state = 0
        self.done = False    

        return self.state