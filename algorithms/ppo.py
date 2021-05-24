import gym
import numpy as np

from algorithms import Algorithm
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

class Ppo(Algorithm):
    """
    A class to use to run the Proximal Policy Optimization (PPO) algorithm

    Attributes
    ----------

    env: Environment
        - OpenAI Gym environment

    data: list of parameters
        - list containing the necessary parameters for the class

    algorithmType: Algorithm
        - Chosen algorithm

    render: Render
        - OpenAI Gym environment rendering

    verbose: bool
        - Boolean value used for printing the values obtained in the algorithm
    
    logger: Logger
        - logger class for printing the values obtained from the algorithm
    
    q_table : List of lists of doubles
        - Q-table containing the values fo the actions of the Q-learning algorithm
    """
    def __init__(self, env, data, algorithmType, render, verbose):
        """
        Constructor for the Proximal Policy Optimization (PPO) algorithm class

        Parameters
        ----------
        env: Environment
            - OpenAI Gym environment

        data: list of parameters
            - list containing the necessary parameters for the class

        algorithmType: Algorithm
            - Chosen algorithm

        render: Render
            - OpenAI Gym environment rendering

        verbose: bool
            - Boolean value used for printing the values obtained in the algorithm


        """
        super().__init__(env, data, algorithmType, render, verbose)

    def run(self):
        """
        Method for running the Proximal Policy Optimization (PPO) algorithm
        """

        # Create the vectorized environment
        env = make_vec_env(self.env, n_envs=self.num_cpu)

        model = PPO('MlpPolicy', 
                    env,
                    learning_rate=self.learning_rate,
                    clip_range = self.clip_range,
                    gamma = self.gamma,
                    gae_lambda=self.gae_lambda,
                    ent_coef=self.ent_coef,
                    max_grad_norm=self.max_grad_norm,
                    vf_coef=self.vf_coef,
                    verbose=1)

        model.learn(total_timesteps=self.num_episodes)

        obs = env.reset()
        for i in range(self.iteration_test):
            action, _states = model.predict(obs)
            obs, rewards, gameStates, info = env.step(action)

            if self.verbose: print(gameStates)
            if self.render:
                for board in info:
                    print(board)
        

        