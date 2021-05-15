import gym
from algorithms.q_learning import QLearning
from algorithms.sarsa import Sarsa

import json
import sys

# Build Environment
env = gym.make("ball_sort_game:basic-v0")

def parseJson(path):
    with open(path) as json_file:
        return json.load(json_file)
        
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Bad arguments\nUsage:")
        print(" main.py [CONFIG] [ALGORITHM]\n\n")
        print("Configuration Files:")
        print("     - More information on README. You can also use one of your config file, by passing \"default.json\" without quotes\n")
        print("Algorithms:")
        print("     - qlearning")
        print("     - sarsa\n")
        exit(-1)

    configFilePath = './config/{}'.format(sys.argv[1])
    algorithm = sys.argv[2]

    try:
        data = parseJson(configFilePath)
    except FileNotFoundError:
        print("Config file not found. More information on README")
        exit(-1)

    if algorithm == 'qlearning':
        QLearning(env, data).run()
    elif algorithm == 'sarsa':
        Sarsa(env, data).run()
    else:
        print("Valid algorithms:")
        print("     - qlearning")
        print("     - sarsa\n")
        exit(-1)