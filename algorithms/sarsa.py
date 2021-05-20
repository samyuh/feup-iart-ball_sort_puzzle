import gym
import numpy as np

from algorithms import Algorithm
from utils import Logger

class Sarsa(Algorithm):
    def __init__(self, env, data, render, verbose, log):
        super().__init__(env, data, render, verbose, log)

        self.logger = Logger("Sarsa")

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
        # Starting the SARSA learning
        for episode in range(self.num_episodes):
            if self.verbose: Logger.newEpisode(episode)

            # Reset the envirnoment , start the episode and get the initial observation
            state1 = self.env.reset()
            
            # Get the first action
            action1 = self.choose_action(state1)

            # Initializing the reward
            rewards_current_episode = 0
        
            for step in range(self.max_steps_per_episode):
                if self.render: self.env.render()
                
                # Getting the next state
                state2, reward, done, info = self.env.step(action1)
        
                # Choosing the next action
                action2 = self.choose_action(state2)
                
                # Learning the Q-value
                self.update(state1, state2, reward, action1, action2)

                state1 = state2
                action1 = action2
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

    def choose_action(self, state):
        """
        Choose the next action
        """
        validMoves = self.env.game.getValid()
        action = 0
        if np.random.uniform(0, 1) < self.exploration_rate:
            action = self.env.action_space.sample()
            while action not in validMoves:
                action = self.env.action_space.sample()
        else:
            qtableT = self.q_table[state,:]
            #print(qtableT)
            action = np.argmax(self.q_table[state,:])

            already = False
            arr = qtableT.argsort()[::-1]
            for i in arr:
                if i in validMoves and not already:
                    action = i
                    already = True

        return action
  

    def update(self, state, state2, reward, action, action2):
        """
        Learn the Q-value
        """
        predict = self.q_table[state, action]
        target = reward + self.discount_rate * self.q_table[state2, action2]
        self.q_table[state, action] = self.q_table[state, action] + self.learning_rate * (target - predict)