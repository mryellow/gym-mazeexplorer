# gym-mazeexplorer

A maze exploration environment for openai/gym.

# Installation

```bash
pip install gym-mazeexplorer
```

# Quick example

```python

  import gym
  import gym_mazeexplorer

  env = gym.make('MazeExplorer-v0')
  env.reset()

  for _ in range(50):
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
```
