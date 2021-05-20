import gym
import numpy as np
import random

from algorithms import Algorithm
from utils import Logger
    
class QLearning(Algorithm):
    def __init__(self, env, data, render, verbose, log):
        super().__init__(env, data, render, verbose, log)
        
        self.logger = Logger("QLearning")

        # Set the action and state spaces
        action_space_size = self.env.action_space.n
        state_space_size = self.env.observation_space.n

        # Initializing the Q-matrix
        self.q_table = np.zeros((state_space_size, action_space_size))

        # List of rewards
        self.rewards_all_episodes = []

    def finishLog(self):
        if self.log:
            return self.logger.closeLogs()
        return None, None

    def run(self):
        # Q-Learning algorithm
        for episode in range(self.num_episodes):
            if self.verbose: Logger.newEpisode(episode)

            # Reset the environment
            done = False
            state = self.env.reset()
            rewards_current_episode = 0
            
            for step in range(self.max_steps_per_episode):
                if self.render: self.env.render()

                # Get a move
                validMoves = self.env.game.getValid()
                exploration_rate_threshold = random.uniform(0, 1)

                if exploration_rate_threshold > self.exploration_rate:
                    action = self.env.argMax(validMoves, self.q_table[state,:])
                else:
                    action = self.env.validSample(validMoves)
                
                # Take the action and observe the outcome state and reward
                new_state, reward, done, info = self.env.step(action)

                # Update Q-table for Q(s,a)
                self.q_table[state, action] = self.q_table[state, action] + \
                    self.learning_rate * (reward + self.discount_rate * np.max(self.q_table[new_state, :]) - \
                    self.q_table[state, action])
                
                state = new_state
                rewards_current_episode += reward
                
                if done: 
                    if self.verbose: 
                        Logger.finishStep(step)
                        self.env.render()
                    break
                    
            # Exploration rate decay
            # Reduce exploration rate (epsilon), because we need less and less exploration
            self.exploration_rate = self.min_exploration_rate + \
                (self.max_exploration_rate - self.min_exploration_rate) * np.exp(-self.exploration_decay_rate * episode)
            
            self.rewards_all_episodes.append(rewards_current_episode)
            
            if self.render: self.env.render()
            if self.log: self.logger.writeLog(episode, rewards_current_episode)
            
        # Calculate and print the average reward per 10 episodes
        rewards_per_thousand_episodes = np.split(np.array(self.rewards_all_episodes), self.num_episodes / 100)

        count = 100
        for r in rewards_per_thousand_episodes:
            if self.log: self.logger.writeAvgRewards(count, r)
            if self.verbose: Logger.printAvgRewards(count, r)
            count += 100

        if self.verbose: Logger.finish(self.rewards_all_episodes, self.num_episodes, self.exploration_rate)