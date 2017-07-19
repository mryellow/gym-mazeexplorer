from gym.envs.registration import register

register(
    id='MazeExplorer-v0',
    entry_point='gym_mazeexplorer.envs:MazeExplorerEnv',
    timestep_limit=1000,
)
