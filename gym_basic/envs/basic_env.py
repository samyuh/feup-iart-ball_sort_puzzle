import gym
import numpy as np

NUM_BOTTLES = 2
BOTTLE_SIZE = 3

STATES = {
    tuple([tuple([1, 1, 0]), tuple([1, 0, 0])]) : 0,
    tuple([tuple([1, 1, 1]), tuple([0, 0, 0])]) : 1,
    tuple([tuple([1, 0, 0]), tuple([1, 1, 0])]) : 2,
    tuple([tuple([0, 0, 0]), tuple([1, 1, 1])]) : 3,
}

class BallSortPuzzle():
    def __init__(self, board):
        self.board = board
    
    def getState(self):
        tup = tuple(tuple(sub) for sub in self.board)
        return STATES[tup]

    def applyMovement(self, action):
        # Invalid Move
        if (action[0] == action[1]):
            return -2

        # Get pieces to toggle
        first, second = self.getFirstNotEmpty(self.board[action[0]]), self.getFirstEmpty(self.board[action[1]])

        # Invalid Move
        if first == -1 or second == -1:
            return -2

        # Get Color to Swap
        color = self.board[action[0]][first]
        # Invalid Move
        if not self.checkColor(color, self.board[action[1]], second-1):
            return -2

        # Do the action
        self.board[action[0]][first] = 0
        self.board[action[1]][second] = color

        return 5

    def checkColor(self, color, bottle, index):
        if index == -1:
            return True
        if color == bottle[index]:
            return True
        return False
    
    def getFirstNotEmpty(self, targetBoard):
        for idx, i in enumerate(targetBoard):
            if i == 0:
                return idx-1
        return BOTTLE_SIZE - 1

    def getFirstEmpty(self, targetBoard):
        for idx, i in enumerate(targetBoard):
            if i == 0:
                return idx
        return -1

    def isGoal(self):
        for i in self.board:
            if len(i) == 0:
                continue
            if not all(element == i[0] for element in i):
                return False
        return True

class BasicEnv(gym.Env):
    def __init__(self):
        # Action Space
        # (X, Y) ->
        #   Where X is the Bottle where the Ball is picked and Y the Bottle where the Ball is put
        self.action_space = gym.spaces.Tuple((gym.spaces.Discrete(NUM_BOTTLES), gym.spaces.Discrete(NUM_BOTTLES)))

        # Observation Space
        #   Number of States
        self.observation_space = gym.spaces.Discrete(4)

        # Init Game
        self.reset()
 
    def step(self, action):
        #assert self.action_space.contains(action)

        self.iteration += 1

        reward = self.game.applyMovement(action) / self.iteration
        done = self.game.isGoal()

        state = self.game.getState()
        
        print(state, reward, done, self.game.board)
        return state, reward, done, self.game.board
    
    def render(self, mode="human", close=False):
        print("Bottles - Move {}".format(self.iteration))
        for idx in range(BOTTLE_SIZE):
            for bottle_num in range(NUM_BOTTLES):
                print("|" + str(self.game.board[bottle_num][idx]) + "|", end="")
            print("\n", end="")

    def reset(self):
        self.game = BallSortPuzzle([[1, 1, 0], [1, 0, 0]])
        self.state = 0
        self.iteration = 0
        self.done = False    

        return self.state