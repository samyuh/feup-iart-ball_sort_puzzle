import gym
import numpy as np

from algorithms import Algorithm
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

class Ppo(Algorithm):
    def __init__(self, env, data, render, verbose, cpu):
        super().__init__(env, data, render, verbose)

        self.num_cpu = cpu

    def run(self):
        # Create the vectorized environment
        env = make_vec_env(self.env, n_envs=self.num_cpu)

        model = PPO('MlpPolicy', 
                    env,
                    #learning_rate=0.01,
                    #ent_coef = 0.01,
                    #n_steps = 15,
                    verbose=1)

        model.learn(total_timesteps=self.num_episodes)

        obs = env.reset()
        for i in range(50):
            action, _states = model.predict(obs)
            obs, rewards, gameStates, info = env.step(action)

            if self.verbose: print(gameStates)
            if self.render:
                for board in info:
                    print(board)
        

        