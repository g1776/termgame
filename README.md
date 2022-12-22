[![python](https://img.shields.io/badge/Python-3.10-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)

# Termgame

## Terminal-based graphical game engine

Created by Gregory Glatzer.

<!-- Load termgame.gif and center -->
<div style="text-align: center">
    <img src="termgame.gif" width="500px" alt="termgame wave machine example with physics"/>
</div>

## Features

-   Simple, easy-to-use API inspired by Unity.
-   Physics engine powered by [Pymunk](https://www.pymunk.org/)
-   Ability to read and render sprites from image files.
-   Framerate and physics timestep control.
-   Statically typed with [mypy](http://mypy-lang.org/).
-   User input with [keyboard](https://github.com/boppreh/keyboard).

## Examples

To run the examples from the source code, first "build" the package by running `pip install .` from the root directory of the project (where `setup.py` is). Then, you can run any of the examples by running

```bash
python termgame/examples/<example_name>/game.py
```

## Contributing

Contributions are welcome! Please open an issue or pull request if you have any suggestions or bug reports. The main branch is used for releases, so please open pull requests against the `development` branch.

### Before Committing

Before committing, please run the following commands to ensure that your code is formatted correctly and passes all tests:

```bash
cd termgame
black src
mypy src
flake8 src --max-line-length=99
pylint src
```
