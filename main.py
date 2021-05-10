import gym
from algorithms.q_learning import QLearning
from algorithms.sarsa import Sarsa

# Build Environment
env = gym.make("gym_basic:basic-v0")

if __name__ == "__main__":
    QLearning(env).run()
    Sarsa(env).run()