import gym
import random
import numpy as np

def run():
    # Building the environment
    env = gym.make("gym_basic:basic-v0")

    # Set the action and state spaces
    dicta, dicti = env.game.actions
    action_space_size = len(dicta)
    state_space_size = env.observation_space.n

    # Create Q-table
    q_table = np.zeros((state_space_size, action_space_size))

    # Set hyperparameters for Q-learning
    num_episodes = 1000         # Total episodes
    max_steps_per_episode = 10  # but it won't go higher than 1

    learning_rate = 0.1         # Learning rate (alpha)
    discount_rate = 0.99        # Discounting rate (gamma)

    # Exploration Parameters
    exploration_rate = 1        # Exploration rate (epsilon)
    max_exploration_rate = 1    # Exploration probability at start
    min_exploration_rate = 0.01 # Minimum exploration probability 
    exploration_decay_rate = 0.01  # Exponential decay rate for exploration prob (if we decrease it, will learn slower)

    # List of rewards
    rewards_all_episodes = []

    # Q-Learning algorithm
    for episode in range(num_episodes):
        print("********* EPISODE {} *********".format(episode))

        # Reset the environment
        state = env.reset()
        done = False
        rewards_current_episode = 0
        
        for step in range(max_steps_per_episode):
            # Visualizing the training
            env.render()

            # Exploration -exploitation trade-off
            exploration_rate_threshold = random.uniform(0,1)

            ## If this number > greater than epsilon --> exploitation 
            if exploration_rate_threshold > exploration_rate: 
                action = np.argmax(q_table[state,:])
                action = dicta[action]
            # Else doing a random choice --> exploration
            else:
                action = env.action_space.sample()
            
            # Take the action and observe the outcome state and reward
            new_state, reward, done, info = env.step(action)
            action = dicti[action]

            # Update Q-table for Q(s,a)
            # Q(s,a):= Q(s,a) + lr [R(s,a) + gamma * max Q(s',a') - Q(s,a)]
            # qtable[new_state,:] : all the actions we can take from new state
            q_table[state, action] = q_table[state, action] + \
                learning_rate * (reward + discount_rate * np.max(q_table[new_state, :]) - q_table[state, action])
            
            # Our new state is state
            state = new_state
            rewards_current_episode += reward
            
            # If done : finish episode
            if done == True: 
                print("Found Solution")
                env.render()
                break
                
        # Exploration rate decay
        # Reduce exploration rate (epsilon), because we need less and less exploration
        exploration_rate = min_exploration_rate + \
            (max_exploration_rate - min_exploration_rate) * np.exp(-exploration_decay_rate * episode)
        
        rewards_all_episodes.append(rewards_current_episode)
        
    # Calculate and print the average reward per 10 episodes
    rewards_per_thousand_episodes = np.split(np.array(rewards_all_episodes), num_episodes / 100)
    count = 100
    print("********** Average  reward per thousand episodes **********\n")

    for r in rewards_per_thousand_episodes:
        print(count, ": ", str(sum(r / 100)))
        count += 100
        
    # Print updated Q-table
    # print(dicta)
    print("\n\n********** Q-table **********\n")
    print(q_table)
    print ("Performace: " +  str(sum(rewards_all_episodes)/num_episodes))
    print("Exploration Rate: ", exploration_rate)