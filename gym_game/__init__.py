from gym.envs.registration import register

# Default Environment
register(id='ball_sort-v0',
        entry_point='gym_game.envs:BallSortEnv',
        kwargs={'board' : [[1, 1, 0], [1, 0, 0]], 
                'bottle_size' : 3,
                'num_bottles' : 2,
                'empty_spaces' : 3,
                'num_balls' : 3,
                'ball_per_color' : 3,
                'num_colors' : 1,
                },
)
