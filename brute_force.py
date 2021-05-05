import gym
import random
import numpy as np

env = gym.make("gym_basic:basic-v0")
for i_episode in range(200):
    observation = env.reset()
    for t in range(1000):
        #env.render()
        print(env.board)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print(info)
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()