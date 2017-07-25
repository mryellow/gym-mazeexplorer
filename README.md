# gym-mazeexplorer

A maze exploration environment for OpenAIGym wrapping [maze_explorer](https://github.com/mryellow/maze_explorer).

## Installation

### Source

```bash
git clone https://github.com/mryellow/gym-mazeexplorer.git
cd gym-mazeexplorer
pip install -e .
```

### Package

* Note: Not registered yet.

```bash
pip install gym_mazeexplorer
```

## Quick example

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

## Test

```bash
python -m unittest discover
```

## Cite

If you use Maze Explorer in your academic research, we would be grateful if you could cite it as follows:

@misc{king2017mazeexplorer,
    author = {King},
    title = {Maze Explorer: A maze exploration game for AI agents},
    howpublished={Web page},
    url = {https://github.com/mryellow/maze_explorer},
    year = {2017}
}
