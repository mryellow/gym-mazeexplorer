from gym.envs.registration import register

register(
    id='MazeExplorer-v0',
    entry_point='gym_mazeexplorer.envs:MazeExplorerEnv',
    kwargs={
        "mode_id": 0
    },
    timestep_limit=10000, # apples/poison aren't being respawned
    #"nondeterministic": True,
    #tags=''
)

register(
    id='MazeExplorer-v1',
    entry_point='gym_mazeexplorer.envs:MazeExplorerEnv',
    kwargs={
        "mode_id": 1
    }
)
