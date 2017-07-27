from gym.envs.registration import register

register(
    id='MazeExplorerEat-v0',
    entry_point='gym_mazeexplorer.envs:MazeExplorerEnv',
    kwargs={
        "mode_id": 0
    },
    timestep_limit=500, # apples/poison aren't being respawned
    #"nondeterministic": True,
    #tags=''
)

register(
    id='MazeExplorerExplore-v0',
    entry_point='gym_mazeexplorer.envs:MazeExplorerEnv',
    kwargs={
        "mode_id": 1
    }
)
