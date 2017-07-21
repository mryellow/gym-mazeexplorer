import unittest

import numpy as np
import gym
from gym_mazeexplorer.envs.mazeexplorer_env import MazeExplorerEnv
from time import sleep

class TestMazeExplorerEnv(unittest.TestCase):

    def test_env(self):

        env = MazeExplorerEnv()
        env.reset()
        for _ in range(50):

            #env.render()
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)

            self.assertTrue(type(observation) == np.ndarray)
            self.assertTrue(type(reward) == int or type(reward) == float)
            self.assertTrue(type(done) == bool)
            self.assertTrue(type(info) == dict)

            sleep(0.05)

        return True


if __name__ == '__main__':
    unittest.main()
