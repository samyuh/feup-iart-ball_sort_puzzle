import sys
import json
import gym
from gym.envs.registration import register

from algorithms.q_learning import QLearning
from algorithms.sarsa import Sarsa
from algorithms.ppo import run

def parseJson(path):
    with open(path) as json_file:
        return json.load(json_file)
        
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Bad arguments\nUsage:")
        print(" main.py [CONFIG] [ALGORITHM] {<-log> <-render> <-default>}\n\n")
        print("Configuration Files:")
        print("     - More information on README. You can also use one of your config file, by passing \"default.json\" without quotes\n")
        print("Algorithms:")
        print("     - qlearning")
        print("     - sarsa\n")
        print("OPTIONS:")
        print("     -log TODO")
        print("         Save Logs")
        print("     -render TODO")
        print("         Render the game through each episode")
        exit(-1)

    configFilePath = './config/{}'.format(sys.argv[1])
    algorithm = sys.argv[2]

    try:
        data = parseJson(configFilePath)
    except FileNotFoundError:
        print("Config file not found. More information on README")
        exit(-1)

    # Build Environment
    register(id='ball_sort-v1',
            entry_point='gym_game.envs:BallSortEnv',
            kwargs={'board' : data['board'], 
                'bottle_size' : data['bottle_size'],
                'num_bottles' : data['num_bottles'],
                'empty_spaces' : data['empty_spaces'],
                'num_balls' : data['num_balls'],
                'ball_per_color' : data['ball_per_color'],
                'num_colors' : data['num_colors'],
                },
    )
    
    env = gym.make("gym_game:ball_sort-v1")

    # Choose Algorithm
    if algorithm == 'qlearning':
        QLearning(env, data['param'], render=False, log=True).run()
    elif algorithm == 'sarsa':
        Sarsa(env, data['param'], render=True, log=True).run()
    elif algorithm == 'ppo':
        run()
    else:
        print("Valid algorithms:")
        print("     - qlearning")
        print("     - sarsa\n")
        exit(-1)