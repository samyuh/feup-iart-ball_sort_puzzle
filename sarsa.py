import numpy as np
import gym
import itertools

NUM_BOTTLES = 2

class Sarsa:
    def __init__(self):
        #Building the environment
        self.env = gym.make("gym_basic:basic-v0")
        
        #Defining the different parameters
        self.epsilon = 0.9
        self.total_episodes = 1000
        self.max_steps = 10
        self.alpha = 0.1
        self.gamma = 0.99

        self.dicta, self.dicti = self.keyActionsDics()
        self.action_space_size = len(self.dicta)
        self.state_space_size = self.env.observation_space.n


    def keyActionsDics(self):
        l = list(itertools.product(list(range(0, NUM_BOTTLES)), repeat=2))
        # l =  list(itertools.permutations(list(range(0, nBottles)), 2))
        return dict(zip(range(len(l)),l)), dict(zip(l, range(len(l))))

    def run(self):

        #Initializing the Q-matrix
        self.q_table = np.zeros((self.state_space_size, self.action_space_size))

        #Initializing the reward
        reward=0
        
        # Starting the SARSA learning
        for episode in range(self.total_episodes):
            t = 0
            state1 = self.env.reset()
            print("********* EPISODE {} *********".format(episode))

            action1 = self.choose_action(state1)
        
            while t < self.max_steps:
                #Visualizing the training
                self.env.render()
                
                #Getting the next state
                state2, reward, done, info = self.env.step(action1)
        
                #Choosing the next action
                action2 = self.choose_action(state2)
                
                #Learning the Q-value
                self.update(state1, state2, reward, action1, action2)
        
                state1 = state2
                action1 = action2
                
                #Updating the respective vaLues
                t += 1
                reward += 1

                #If at the end of learning process
                if done:
                    print("Found Solution")
                    break


        #Evaluating the performance
        print ("Performace : ", reward/self.total_episodes)
            
        # Print updated Q-table
        print("\n\n********** Q-table **********\n")
        print(self.q_table)


    #Function to choose the next action
    def choose_action(self, state):
        action = 0
        if np.random.uniform(0, 1) < self.epsilon:
            action = self.env.action_space.sample()
        else:
            action = np.argmax(self.q_table[state, :])
            action = self.dicta[action]

        return action
  
    #Function to learn the Q-value
    def update(self, state, state2, reward, action, action2):
        action = self.dicti[action]
        action2 = self.dicti[action2]

        predict = self.q_table[state, action]
        target = reward + self.gamma * self.q_table[state2, action2]
        self.q_table[state, action] = self.q_table[state, action] + self.alpha * (target - predict)

Sarsa().run()