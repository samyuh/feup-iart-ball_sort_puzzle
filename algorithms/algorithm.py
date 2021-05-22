class Algorithm:
    def __init__(self, env, data, render, verbose):
        # Set Environment
        self.env = env

        # Render, Log, Verbose
        self.render = render
        self.verbose = verbose

        # Define Hyper Parameters
        missingValues = False

        if 'num_episodes' not in data: missingValues = True
        if 'max_steps_per_episode' not in data: missingValues = True
        if 'learning_rate' not in data: missingValues = True
        if 'discount_rate' not in data: missingValues = True
        if 'exploration_rate' not in data: missingValues = True
        if 'max_exploration_rate' not in data: missingValues = True
        if 'min_exploration_rate' not in data: missingValues = True
        if 'exploration_decay_rate' not in data: missingValues = True

        if missingValues:
            print("Missing values in JSON File")
            exit(-1)
        
        self.num_episodes = data['num_episodes']
        self.max_steps_per_episode = data['max_steps_per_episode']
        self.learning_rate = data['learning_rate'] # Alpha
        self.discount_rate = data['discount_rate'] # Gamma
        self.exploration_rate = data['exploration_rate']  # Epsilon
        self.max_exploration_rate = data['max_exploration_rate'] # Max Epsilon
        self.min_exploration_rate = data['min_exploration_rate'] # Min Epsilon
        self.exploration_decay_rate = data['exploration_decay_rate'] # Decay Rate