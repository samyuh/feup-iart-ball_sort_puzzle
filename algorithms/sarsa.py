import numpy as np
import gym

class Sarsa:
    def __init__(self, env, data):
        self.env = env

        # Set the action and state spaces
        self.dicta, self.dicti = self.env.game.actions
        self.action_space_size = len(self.dicta)
        self.state_space_size = self.env.observation_space.n

        # Initializing the Q-matrix
        self.q_table = np.zeros((self.state_space_size, self.action_space_size))
        
        # Defining the different parameters
        self.num_episodes = data['num_episodes'] # Total episodes
        self.max_steps_per_episode = data['max_steps_per_episode']

        self.learning_rate = data['learning_rate'] # Learning rate (learning_rate)
        self.discount_rate = data['discount_rate'] # Discounting rate (discount_rate)

        # Exploration Parameters
        self.exploration_rate = data['exploration_rate']  # Exploration rate (epsilon)
        self.max_exploration_rate = data['max_exploration_rate'] # Exploration probability at start
        self.min_exploration_rate = data['min_exploration_rate'] # Minimum exploration probability
        self.exploration_decay_rate = data['exploration_decay_rate'] # Exponential decay rate for exploration prob (if we decrease it, will learn slower)

        # List of rewards
        self.rewards_all_episodes = []

    def run(self):
        # Initializing the reward
        rewards_current_episode = 0
        
        # Starting the SARSA learning
        for episode in range(self.num_episodes):
            print("********* EPISODE {} *********".format(episode))

            # Reset the envirnoment , start the episode and get the initial observation
            state1 = self.env.reset()
            # Get the first action
            action1 = self.choose_action(state1)
        
            for step in range(self.max_steps_per_episode):
                # Visualizing the training
                #self.env.render()
                
                # Getting the next state
                state2, reward, done, info = self.env.step(action1)
        
                # Choosing the next action
                action2 = self.choose_action(state2)
                
                # Learning the Q-value
                self.update(state1, state2, reward, action1, action2)

                # Set current values as previous values
                state1 = state2
                action1 = action2
                
                # Updating the respective vaLues
                rewards_current_episode += reward

                # If at the end of learning process
                if done:
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

        # Evaluating the performance
        print ("Performace: " +  str(sum(self.rewards_all_episodes)/self.num_episodes))
            
        # Print updated Q-table
        print("\n\n********** Q-table **********\n")
        print(self.q_table)


    # Function to choose the next action
    def choose_action(self, state):
        action = 0
        if np.random.uniform(0, 1) < self.exploration_rate:
            action = self.env.action_space.sample()
        else:
            action = np.argmax(self.q_table[state, :])
            action = self.dicta[action]

        return action
  
    # Function to learn the Q-value
    def update(self, state, state2, reward, action, action2):
        action = self.dicti[action]
        action2 = self.dicti[action2]

        predict = self.q_table[state, action]
        target = reward + self.discount_rate * self.q_table[state2, action2]
        self.q_table[state, action] = self.q_table[state, action] + self.learning_rate * (target - predict)