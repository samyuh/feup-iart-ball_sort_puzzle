
# Artificial Intelligence - Reinforcement Learning with Ball Sort Puzzle
![University](https://img.shields.io/badge/FEUP-MIEIC-red)

- **Institution**: [FEUP](https://sigarra.up.pt/feup/en/web_page.Inicial)
- **Course**: [MIEIC](https://sigarra.up.pt/feup/en/cur_geral.cur_view?pv_curso_id=742&pv_ano_lectivo=2020)
- **Curricular Unit**: [Subject](https://sigarra.up.pt/feup/en/ucurr_geral.ficha_uc_view?pv_ocorrencia_id=459487)

### Group Members
- Diana Freitas, up201806230
- Diogo Samuel Fernandes, up201806250
- Hugo Guimarães, up201806490

### Description

Ball Sort Puzzle is a color sorting game, in which the balls must be sorted in
the tubes until all the balls of the same color are stacked together in the
same tube.
A ball can only be placed on top of another ball if both of them have the
same color and if the tube has enough space.

---

### Setup

We used python version 3.8.9 on Windows.

Dependecies:
```
    pip install gym
    pip install stable_baselines3
```

You can also config the project with our setup.py instead of running these pip commands.
Create a virtual env (if you want)

On Windows, run:
```
    python -m venv iart
    iart\Scripts\activate.bat
```
On Unix or MacOS, run:
```
    python -m venv iart
    source iart/bin/activate
```
After that, install all dependecies using:
```
    pip install .
```

Now you're ready! To run our program, run in the terminal:
```
 python main.py [ALGORITHM] [CONFIG] [-verbose -log -plot]

 python3 main.py [ALGORITHM] [CONFIG] [-verbose -log -plot]
```


##### Algorithms
qlearning
sarsa
dqlearning
ppo

##### Configuration Files
Create a configuration file under the ./config directory (or use one of). 
The config files have the following layout if you're using one of the following algorithms: [qlearning, dqlearning, sarsa]
You can also use one of your config file, by passing "level1.json" without quotes.

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

If you want to use ppo, the layout of the config file should be the following. You can also use our config file "level1-ppo.json".
```json
{
    "board" : [[1, 2, 1], [1, 2, 2], [0, 0, 0]],
    "max_steps" : 20,
    "param" : {
        "learning_rate" : 0.003,
        "clip_range" : 0.2,
        "gamma" : 0.99,
        "gae_lambda" : 0.95,
        "ent_coef" : 0.0,
        "max_grad_norm" : 0.5,
        "vf_coef" : 0.5,
        "num_cpu" : 4,
        "num_episodes" : 100000
    }
}
```

##### Options
- -verbose
- -render
- -plot

We recommend use the options: '-verbose -plot'

**Note 1**: If you don't choose anything on options, nothing will be printed or appear on your screen.
**Note 2**: If you want to see the reward plot, using -plot, you should have -log too.

---

#### Example 

Use QLearning with the definitions of first_level.json with plot and verbose
```
python main.py qlearning first_level.json -verbose -plot
```

Use Sarsa with the definitions of first_level.json with plot, verbose and render
```
python main.py sarsa first_level.json -verbose -render -plot
```
