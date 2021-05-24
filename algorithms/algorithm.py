# -- Personal Imports -- #

from enum import Enum


class AlgorithmType(Enum):
    """
    Python enumeration class for the distinguishing the algorithms 
    """
    VANILLA = 0
    STABLE_BASELINES_PPO = 1

class Algorithm:
    """
    Class for defining an algorithm in our project

    Arguments
    ---------
    env: Environment
        - OpenAI Gym environment

    render: Render
        - OpenAI Gym environment rendering

    verbose: bool
        - Boolean value used for printing the values obtained in the algorithm
    
    num_episodes : int
        - number of episodes to be used in the algorithm 
    
    learning_rate : double
        - learning rate value to be used in the algorithm (Alpha value)

    discount_rate : double 
        - discount rate value to be used in the algorithm (Gama value)

    exploration_rate : double
        - exploration rate value to be used in the algorithm (Epsion value)

    max_exploration_rate = double # Max Epsilon
         - maximum exploration rate value to be used in the algorithm (Max Epsilon value)

    min_exploration_rate = double # Min Epsilon
         - minimum exploration rate value to be used in the algorithm (Min Epsilon value)

    exploration_decay_rate = double # Decay Rate
        - Decay rate value to be used in the algorithm (Decay rate value)


    clip_range : double
        - learning rate range : 0.003 to 5e-6

    gamma : double 
        - Discount Factor Gamma Range: 0.99 (most common), 0.8 to 0.9997
    
    gae_lambda : double
        - GAE Parameter Lambda Range: 0.9 to 1

    ent_coef : double 
        - Entropy Coefficient Range: 0 to 0.01
    
    max_grad_norm : double
        - Value Function Coefficient Range: 0.5, 1

    vf_coef : double 
        - Value fucntion coeficient

    num_cpu : double 
        - number of CPUs

    iteration_test : double 
        - number of times we are running the model after it has been trained

    """
    def __init__(self, env, data, algorithmType, render, verbose):
        """
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
        # Set Environment
        self.env = env

        # Render, Log, Verbose
        self.render = render
        self.verbose = verbose

        # Define Hyper Parameters
        missingValues = False
        
        if algorithmType == AlgorithmType.VANILLA:
            if 'num_episodes' not in data: missingValues = True
            if 'max_steps_per_episode' not in data: missingValues = True
            if 'learning_rate' not in data: missingValues = True
            if 'discount_rate' not in data: missingValues = True
            if 'exploration_rate' not in data: missingValues = True
            if 'max_exploration_rate' not in data: missingValues = True
            if 'min_exploration_rate' not in data: missingValues = True
            if 'exploration_decay_rate' not in data: missingValues = True

            if missingValues:
                print("Missing values in JSON File. More on readme")
                exit(-1)
            
            self.num_episodes = data['num_episodes']
            self.max_steps_per_episode = data['max_steps_per_episode']
            self.learning_rate = data['learning_rate'] # Alpha
            self.discount_rate = data['discount_rate'] # Gamma
            self.exploration_rate = data['exploration_rate']  # Epsilon
            self.max_exploration_rate = data['max_exploration_rate'] # Max Epsilon
            self.min_exploration_rate = data['min_exploration_rate'] # Min Epsilon
            self.exploration_decay_rate = data['exploration_decay_rate'] # Decay Rate
        else:
            if 'learning_rate' not in data: missingValues = True
            if 'clip_range' not in data: missingValues = True
            if 'gamma' not in data: missingValues = True
            if 'gae_lambda' not in data: missingValues = True
            if 'ent_coef' not in data: missingValues = True
            if 'max_grad_norm' not in data: missingValues = True
            if 'vf_coef' not in data: missingValues = True
            if 'num_cpu' not in data: missingValues = True
            if 'num_episodes' not in data: missingValues = True
            if 'iteration_test' not in data: missingValues = True

            if missingValues:
                print("Missing values in JSON File. More on readme")
                exit(-1)

            self.learning_rate = data['learning_rate'] # Learning Rate Range: 0.003 to 5e-6
            self.clip_range = data['clip_range'] # Clipping Range: 0.1, 0.2, 0.3
            self.gamma = data['gamma'] # Discount Factor Gamma Range: 0.99 (most common), 0.8 to 0.9997
            self.gae_lambda = data['gae_lambda'] # GAE Parameter Lambda Range: 0.9 to 1
            self.ent_coef = data['ent_coef'] # Entropy Coefficient Range: 0 to 0.01
            self.max_grad_norm = data['max_grad_norm'] # Value Function Coefficient Range: 0.5, 1
            self.vf_coef = data['vf_coef']
            self.num_cpu = data['num_cpu']
            self.num_episodes = data['num_episodes']
            self.iteration_test = data['iteration_test']