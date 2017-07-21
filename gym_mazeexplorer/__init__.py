from gym.envs.registration import register

register(
    id='MazeExplorer-v0',
    entry_point='gym_mazeexplorer.envs:MazeExplorerEnv',
    kwargs={
        "mode": 0
    },
    #timestep_limit=1000,
    #"nondeterministic": True,
    #tags=''
)

register(
    id='MazeExplorer-v1',
    entry_point='gym_mazeexplorer.envs:MazeExplorerEnv',
    kwargs={
        "mode": 1
    }
)
