import gym
from gym import spaces
from gym.utils import seeding

import pyglet
import numpy as np

import mazeexp as mx

class MazeExplorerEnv(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second' : 20
    }

    def __init__(self, mode_id=0):
        # Start engine, invisible
        self.engine = mx.MazeExplorer(mode_id, False)

        self.action_space = spaces.Discrete(self.engine.actions_num)
        # Use `observation_chans` to multichannel with `item` sensors.
        if self.engine.observation_chans > 1:
            self.shape = (self.engine.observation_num, self.engine.observation_chans)
        else:
            self.shape = (self.engine.observation_num,)

        self.observation_space = spaces.Box(low=0, high=1, shape=self.shape)

        self.viewer = None
        self.state = None

        self._seed()

    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def _step(self, action):
        assert self.action_space.contains(action), "%r (%s) invalid"%(action, type(action))

        # Act in the environment
        self.state, reward, terminal, info = self.engine.act(action)

        #assert self.observation_space.contains(self.state), 'Step observation: {!r} not in space'.format(self.state)

        # observation, reward, done, info.
        return np.array(self.state), reward, terminal, info

    def _reset(self):
        # TODO: Reset to `ones`?
        #self.state = self.np_random.uniform(low=0, high=1, size=self.shape)
        self.state = self.engine.reset()
        return np.array(self.state)

    def _render(self, mode='human', close=False):
        if close:
            return

        #if self.viewer is None:
        #    self.viewer = self.engine.director.window

        if self.state is None: return None

        #self.viewer.switch_to()
        #self.viewer.dispatch_events()
        #self.viewer.dispatch_event('on_draw')

        arr = None
        if mode == 'rgb_array':
            buffer = pyglet.image.get_buffer_manager().get_color_buffer()
            image_data = buffer.get_image_data()
            arr = np.fromstring(image_data.data, dtype=np.uint8, sep='')
            # In https://github.com/openai/gym-http-api/issues/2, we
            # discovered that someone using Xmonad on Arch was having
            # a window of size 598 x 398, though a 600 x 400 window
            # was requested. (Guess Xmonad was preserving a pixel for
            # the boundary.) So we use the buffer height/width rather
            # than the requested one.
            arr = arr.reshape(buffer.height, buffer.width, 4)
            arr = arr[::-1,:,0:3]

        #self.viewer.flip()
        # Ticking before events caused glitches.
        #pyglet.clock.tick()

        return arr
