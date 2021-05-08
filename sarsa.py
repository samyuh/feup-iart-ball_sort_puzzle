import numpy as np
import gym
import itertools

NUM_BOTTLES = 2

def keyActionsDics():
    l = list(itertools.product(list(range(0, NUM_BOTTLES)), repeat=2))
    # l =  list(itertools.permutations(list(range(0, nBottles)), 2))
    return dict(zip(range(len(l)),l)), dict(zip(l, range(len(l))))

def run():
    #Building the environment
    env = gym.make("gym_basic:basic-v0")
    
    #Defining the different parameters
    epsilon = 0.9
    total_episodes = 10000
    max_steps = 100
    alpha = 0.85
    gamma = 0.95
      
    dicta, dicti = keyActionsDics()
    action_space_size = len(dicta)
    state_space_size = env.observation_space.n

    #Initializing the Q-matrix
    q_table = np.zeros((state_space_size, action_space_size))

    #Initializing the reward
    reward=0
    
    # Starting the SARSA learning
    for episode in range(total_episodes):
        t = 0
        state1 = env.reset()
        print("********* EPISODE {} *********".format(episode))
        print(env.game.board)
        env.render()

        action1 = choose_action(state1)
    
        while t < max_steps:
            #Visualizing the training
            env.render()
            
            #Getting the next state
            state2, reward, done, info = env.step(action1)
    
            #Choosing the next action
            action2 = choose_action(state2)
            
            #Learning the Q-value
            update(state1, state2, reward, action1, action2)
    
            state1 = state2
            action1 = action2
            
            #Updating the respective vaLues
            t += 1
            reward += 1
            
            #If at the end of learning process
            if done:
                break

    #Evaluating the performance
    print ("Performace : ", reward/total_episodes)
    
    #Visualizing the Q-matrix
    print(Q)


#Function to choose the next action
def choose_action(state):
    action=0
    if np.random.uniform(0, 1) < epsilon:
        action = env.action_space.sample()
    else:
        action = np.argmax(Q[state, :])
    return action
  
#Function to learn the Q-value
def update(state, state2, reward, action, action2):
    predict = Q[state, action]
    target = reward + gamma * Q[state2, action2]
    Q[state, action] = Q[state, action] + alpha * (target - predict)

run()