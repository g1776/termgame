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
