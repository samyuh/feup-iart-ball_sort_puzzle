import gym
import numpy as np

NUM_BOTTLES = 2
BOTTLE_SIZE = 3
"""
bottle_list = [["yellow"], [ "yellow", "yellow"]]
move_list = []

def ansiEncodeGame():
    for idx, i in enumerate(bottle_list):
        print("Bottle" + str(idx))
        start = MAX_BALLS - len(i)
        for value in range(MAX_BALLS):
            if value >= start:
                print("|" + i[value-start] + "|")
            else:
                print("|    |")
        print("\n")

def moves():
    for idxA, a in enumerate(bottle_list): # Pick from this bottle
        for idxB, b in enumerate(bottle_list): # To this bottle
            if not a:
                continue
            elif not b:
                move_list.append([a[0], idxA, idxB])
            elif (a[0] == b[0]) and isNotFull(b) and a != b:
                move_list.append([a[0], idxA, idxB])
"""

class BasicEnv(gym.Env):
    def __init__(self):
        # Duas ações -> um para o dois ou dois para um
        self.action_space = gym.spaces.Tuple((gym.spaces.Discrete(NUM_BOTTLES), gym.spaces.Discrete(NUM_BOTTLES)))

        # 2 boxes, de tamnho 3 -> para que raio é preciso isto
        self.observation_space = gym.spaces.Discrete(4) #gym.spaces.Box(low=0, high=1, shape=(NUM_BOTTLES, BOTTLE_SIZE), dtype=np.int32) 
        self.reset()
 
    def step(self, action):
        #assert self.action_space.contains(action)
        self.ite += 1
        reward = self.applyMovement(action) / self.ite
        
        done = self.isGoal()    
        return 1, reward, done, self.board
    
    def applyMovement(self, action):
        # Invalid Move
        print(action)
        
        if (action[0] == action[1]):
            return -999
        
        # Get pieces to toggle
        first, second = self.getFirstNotEmpty(self.board[action[0]]), self.getFirstEmpty(self.board[action[1]])

        # Invalid Move
        if first == -1 or second == -1:
            return -999

        # Get Color to Swap
        color = self.board[action[0]][first]
        # Invalid Move
        if not self.checkColor(color, self.board[action[1]], second-1):
            return -999

        # Do the action
        self.board[action[0]][first] = 0
        self.board[action[1]][second] = color

        return 1
    
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
        return -1   

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

    def reset(self):
        self.ite = 0
        self.board = [[1, 1, 0], [1, 0, 0]]
        self.done = False       
        return tuple(self.board)