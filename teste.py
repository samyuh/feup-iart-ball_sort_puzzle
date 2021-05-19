import gym
from stable_baselines3 import DQN
from stable_baselines3.common.monitor import Monitor
from gym.envs.registration import register

register(id='ball_sort-v1',
        entry_point='gym_game.envs:BallSortEnv',
        kwargs={'board' : [[1, 2, 1], [1, 2, 2], [0, 0, 0]],
            'bottle_size' : 3,
            'num_bottles' : 3,
            'empty_spaces' : 3,
            'num_balls' : 6,
            'ball_per_color' : 3,
            'num_colors' : 2,
            },
)

env = gym.make("ball_sort-v1")

model = DQN("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=100000, log_interval=4)
model.save("dqn_cartpole")

del model # remove to demonstrate saving and loading

model = DQN.load("dqn_cartpole")

obs = env.reset()
while True:
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
        obs = env.reset()
