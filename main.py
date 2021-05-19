import sys
import json
import gym

from gym.envs.registration import register

from algorithms.q_learning import QLearning
from algorithms.sarsa import Sarsa
#from algorithms.ppo import run

from utils.plot import Plot
from utils.logger import Logger

class App:
    def __init__(self, args):
        if len(args) < 3:
            Logger.errorArgs()
            exit(-1)
        
        self.algorithm = args[1]
        self.configFilePath = './config/{}'.format(args[2])
        self.render = False
        self.verbose = False
        self.log = False
        self.plot = False 

        if '-render' in args: self.render = True
        if '-verbose' in args: self.verbose = True
        if '-log' in args: self.log = True
        if '-plot' in args: self.plot = True

        try:
            self.data = parseJson(self.configFilePath)
        except FileNotFoundError:
            Logger.fileNotFound("Config")
            exit(-1)

        self.run()

    def run(self):
        # TODO: check if data is right

        # Build Environment
        register(id='ball_sort-v1',
                entry_point='gym_game.envs:BallSortEnv',
                kwargs={'board' : self.data['board'], 
                        'bottle_size' : self.data['bottle_size'],
                        'num_bottles' : self.data['num_bottles'],
                        'empty_spaces' : self.data['empty_spaces'],
                        'num_balls' : self.data['num_balls'],
                        'ball_per_color' : self.data['ball_per_color'],
                        'num_colors' : self.data['num_colors'],
                    },
        )
        
        env = gym.make("gym_game:ball_sort-v1")

        # Choose Algorithm
        if self.algorithm == 'qlearning':
            QLearning(env, self.data['param'], self.render, self.log).run()
        elif self.algorithm == 'sarsa':
            Sarsa(env, self.data['param'], self.render, self.log).run()
        elif self.algorithm == 'ppo':
            #run()
        else:
            print("Valid algorithms:")
            print("     - qlearning")
            print("     - sarsa\n")
            exit(-1)

        if self.plot:
            a = Plot('filePath')
            a.plot()

def parseJson(path):
    with open(path) as json_file:
        return json.load(json_file)
        
if __name__ == "__main__":
    app = App(sys.argv)

    
