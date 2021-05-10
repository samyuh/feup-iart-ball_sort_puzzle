import gym
import random
import numpy as np

class QLearning:
    def __init__(self, env):
        self.env = env

        # Set the action and state spaces
        self.dicta, self.dicti = self.env.game.actions
        action_space_size = len(self.dicta)
        state_space_size = self.env.observation_space.n

        # Create Q-table
        self.q_table = np.zeros((state_space_size, action_space_size))

        # Set hyperparameters for Q-learning
        self.num_episodes = 1000         # Total episodes
        self.max_steps_per_episode = 10  # but it won't go higher than 1

        self.learning_rate = 0.1         # Learning rate (alpha)
        self.discount_rate = 0.99        # Discounting rate (gamma)

        # Exploration Parameters
        self.exploration_rate = 1        # Exploration rate (epsilon)
        self.max_exploration_rate = 1    # Exploration probability at start
        self.min_exploration_rate = 0.01 # Minimum exploration probability 
        self.exploration_decay_rate = 0.01  # Exponential decay rate for exploration prob (if we decrease it, will learn slower)

        # List of rewards
        self.rewards_all_episodes = []

    def run(self):
        # Q-Learning algorithm
        for episode in range(self.num_episodes):
            print("********* EPISODE {} *********".format(episode))

            # Reset the environment
            state = self.env.reset()
            done = False
            rewards_current_episode = 0
            
            for step in range(self.max_steps_per_episode):
                # Visualizing the training
                self.env.render()

                # Exploration -exploitation trade-off
                exploration_rate_threshold = random.uniform(0,1)

                ## If this number > greater than epsilon --> exploitation 
                if exploration_rate_threshold > self.exploration_rate: 
                    action = np.argmax(self.q_table[state,:])
                    action = self.dicta[action]
                # Else doing a random choice --> exploration
                else:
                    action = self.env.action_space.sample()
                
                # Take the action and observe the outcome state and reward
                new_state, reward, done, info = self.env.step(action)
                action = self.dicti[action]

                # Update Q-table for Q(s,a)
                # Q(s,a):= Q(s,a) + lr [R(s,a) + gamma * max Q(s',a') - Q(s,a)]
                # qtable[new_state,:] : all the actions we can take from new state
                self.q_table[state, action] = self.q_table[state, action] + \
                    self.learning_rate * (reward + self.discount_rate * np.max(self.q_table[new_state, :]) - self.q_table[state, action])
                
                # Our new state is state
                state = new_state
                rewards_current_episode += reward
                
                # If done : finish episode
                if done == True: 
                    print("Found Solution")
                    self.env.render()
                    break
                    
            # Exploration rate decay
            # Reduce exploration rate (epsilon), because we need less and less exploration
            self.exploration_rate = self.min_exploration_rate + \
                (self.max_exploration_rate - self.min_exploration_rate) * np.exp(-self.exploration_decay_rate * episode)
            
            self.rewards_all_episodes.append(rewards_current_episode)
            
        # Calculate and print the average reward per 10 episodes
        rewards_per_thousand_episodes = np.split(np.array(self.rewards_all_episodes), self.num_episodes / 100)
        count = 100
        print("********** Average  reward per thousand episodes **********\n")

        for r in rewards_per_thousand_episodes:
            print(count, ": ", str(sum(r / 100)))
            count += 100
            
        # Print updated Q-table
        # print(dicta)
        print("\n\n********** Q-table **********\n")
        print(self.q_table)
        print ("Performace: " +  str(sum(self.rewards_all_episodes)/self.num_episodes))
        print("Exploration Rate: ", self.exploration_rate)