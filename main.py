import sys

import json
import gym
from gym.envs.registration import register

from algorithms import QLearning, Sarsa
from utils import Plot, Logger

class App:
    def __init__(self, args):
        if len(args) < 3:
            Logger.errorArgs()
            return -1
        
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
            self.data = self.parseJson(self.configFilePath)
        except FileNotFoundError:
            Logger.error("Config file not found. More information on README.")
            return -1

        self.run()

    def parseJson(self, path):
        with open(path) as json_file:
            return json.load(json_file)

    def run(self):
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
            qLearning = QLearning(env, self.data['param'], self.render, self.verbose, self.log)
            qLearning.run()

            _, avgValues = qLearning.finishLog()
        elif self.algorithm == 'sarsa':
            sarsa = Sarsa(env, self.data['param'], self.render, self.verbose, self.log)
            sarsa.run()

            _, avgValues = sarsa.finishLog()
        else:
            Logger.error("Not a valid algorithm.")
            return -1

        if self.plot and self.log:
            graphic = Plot(avgValues)
            graphic.plot()
        elif self.plot:
            Logger.error("Log should be enabled.")
            return -1
        
        return 0

if __name__ == "__main__":
    app = App(sys.argv)

    
