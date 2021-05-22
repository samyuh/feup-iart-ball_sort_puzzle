import sys

import json
import gym
from gym.envs.registration import register

from algorithms import AlgorithmType, QLearning, Sarsa, DoubleQLearning, Ppo
from utils import Plot, Logger, GameSettings

class App:
    def __init__(self, args):
        if len(args) < 3:
            Logger.errorArgs()
            exit(-1)
        
        self.algorithm = args[1]
        self.configFilePath = './config/{}'.format(args[2])
        self.render = False
        self.verbose = False
        self.plot = False 

        if '-render' in args: self.render = True
        if '-verbose' in args: self.verbose = True
        if '-plot' in args: self.plot = True

        try:
            self.data = self.parseJson(self.configFilePath)
        except FileNotFoundError:
            Logger.error("Config file not found. More information on README.")
            exit(-1)

        self.settings = GameSettings(self.data['board'])

    def parseJson(self, path):
        with open(path) as json_file:
            return json.load(json_file)

    def run(self):
        # Build Environment
        if 'board' not in self.data: 
            Logger.error("Missing board on config file. Check readme.")
            exit(-1)
        elif 'max_steps' not in self.data: 
            Logger.error("Missing max_steps on config file. Check readme.")
            exit(-1)
        elif 'param' not in self.data: 
            Logger.error("Missing param on config file. Check readme.")
            exit(-1)

        env_id = 'ball_sort-v2'
        register(id=env_id,
                entry_point='gym_game.envs:BallSortEnv',
                kwargs={'board' : self.data['board'], 
                        'max_steps' : self.data['max_steps'],
                        'bottle_size' : self.settings.bottle_size,
                        'num_bottles' : self.settings.num_bottles,
                        'empty_spaces' : self.settings.empty_spaces,
                        'num_balls' : self.settings.num_balls,
                        'ball_per_color' : self.settings.ball_per_color,
                        'num_colors' : self.settings.num_colors,
                    },
        )
        
        env = gym.make(env_id)

        # Choose Algorithm
        if self.algorithm == 'qlearning':
            qLearning = QLearning(env, self.data['param'], AlgorithmType.CLASSIC, self.render, self.verbose)
            qLearning.run()

            _, avgValues = qLearning.finishLog()
        elif self.algorithm == 'sarsa':
            sarsa = Sarsa(env, self.data['param'], AlgorithmType.CLASSIC, self.render, self.verbose)
            sarsa.run()

            _, avgValues = sarsa.finishLog()
        elif self.algorithm == 'dqlearning':
            dqLearning = DoubleQLearning(env, self.data['param'], AlgorithmType.CLASSIC, self.render, self.verbose)
            dqLearning.run()

            _, avgValues = dqLearning.finishLog()
        elif self.algorithm == 'ppo':
            ppo = Ppo(env_id, self.data['param'], AlgorithmType.DEEP_LEARNING, self.render, self.verbose)
            ppo.run()

            exit(0)
        else:
            Logger.error("Not a valid algorithm.")
            exit(-1)

        if self.plot:
            graphic = Plot(avgValues)
            graphic.plot()
        elif self.plot:
            Logger.error("Log should be enabled.")
            exit(-1)
        
        exit(0)

if __name__ == "__main__":
    app = App(sys.argv)
    app.run()

    
