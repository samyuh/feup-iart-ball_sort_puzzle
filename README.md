# Reinforcement Learning - Ball Sort Puzzle

PYTHON VERSION -> 3.8.9
pip install gym
pip install tensorflow

### Run

Usage:
```
 python main.py [CONFIG] [ALGORITHM]

 python3 main.py [CONFIG] [ALGORITHM]
```

Create a configuration file under the ./config directory (or use one of). The config files have the following layout:

```json
{
    "board" : [[1, 2, 1], [1, 2, 2], [0, 0, 0]],
    "bottle_size" : 3,
    "num_bottles" : 3,
    "param" : {
        "num_episodes" : 100000,
        "max_steps_per_episode" : 20,
        "learning_rate" : 0.1,
        "discount_rate" : 0.95,
        "exploration_rate" : 1,    
        "max_exploration_rate" : 1,
        "min_exploration_rate" : 0.001,
        "exploration_decay_rate" : 0.001
    }
}
```

After that, choose one of the implemented algorithms:
- Q-Learning, by passing "qlearning" as argument
- Sarsa, by passing "sarsa" as argument