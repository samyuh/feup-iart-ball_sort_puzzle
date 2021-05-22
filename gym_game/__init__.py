from gym.envs.registration import register

# Default Environment
register(id='ball_sort-v0',
        entry_point='gym_game.envs:BallSortEnv',
        kwargs={'board' : [[1, 2, 1], [1, 2, 2], [0, 0, 0]],
            'max_steps' : 30,
            'bottle_size' : 3,
            'num_bottles' : 3,
            'empty_spaces' : 3,
            'num_balls' : 6,
            'ball_per_color' : 3,
            'num_colors' : 2,
            },
)

register(id='ball_sort-v1',
        entry_point='gym_game.envs:BallSortEnv',
        kwargs={'board' : [[1, 2, 3, 1], [1, 2, 3, 3], [2, 3, 1, 2], [0, 0, 0, 0], [0, 0, 0, 0]],
                'max_steps' : 40,
                'bottle_size' : 4,
                'num_bottles' : 5,
                'empty_spaces' : 8,
                'num_balls' : 12,
                'ball_per_color' : 4,
                'num_colors' : 3,
            },
)


