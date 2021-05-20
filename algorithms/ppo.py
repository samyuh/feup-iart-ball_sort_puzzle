import gym

from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.env_checker import check_env

from gym.envs.registration import register

def run():
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

    env = make_vec_env("gym_game:ball_sort-v1", n_envs=3)

    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=25000)
    model.save("ppo_cartpole")

    del model # remove to demonstrate saving and loading

    model = PPO.load("ppo_cartpole")

    obs = env.reset()
    while True:
        action, _states = model.predict(obs)
        obs, rewards, dones, info = env.step(action)
        print(dones)
        #env.render()