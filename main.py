import gym
from algorithms.q_learning import QLearning
from algorithms.sarsa import Sarsa

import json

# Build Environment
env = gym.make("gym_basic:basic-v0")

def parseJson(path):
    with open(path) as json_file:
        return json.load(json_file)
        
if __name__ == "__main__":
    configFilePath = './config/default.json'
    algorithm = 'QLearning'
    try:
        data = parseJson(configFilePath)
    except FileNotFoundError:
        print("File config.json missing. More information on README")
        exit()

    if algorithm == 'QLearning':
        QLearning(env, data).run()
    else:
        Sarsa(env).run()