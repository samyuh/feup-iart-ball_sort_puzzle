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
    "num_episodes" : 10000,
    "max_steps_per_episode" : 1000,
    "learning_rate" : 0.4,
    "discount_rate" : 0.95,
    "exploration_rate" : 1,    
    "max_exploration_rate" : 1,
    "min_exploration_rate" : 0.01,
    "exploration_decay_rate" : 0.01
}
```

After that, choose one of the implemented algorithms:
- Q-Learning, by passing "qlearning" as argument
- Sarsa, by passing "sarsa" as argument