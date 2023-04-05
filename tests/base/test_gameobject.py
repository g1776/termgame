import pytest
from termgame import Gameobject, Screen


def test_init():

    screen1 = Screen(10, 10)
    screen2 = Screen(20, 20)

    go = Gameobject(
        x=1,
        y=2,
        depth=-1,
        update_order=3,
        sprites=[screen1, screen2],
        # on_start=fake_start,
        # on_update=fake_update,
        name="test",
    )

    assert go.x == 1
    assert go.y == 2
    assert go.depth == -1
    assert go.update_order == 3
    assert go.get_sprites() == [screen1, screen2]
    # assert go.on_start == fake_start
    # assert go.on_update == fake_update
    assert go.name == "test"


def test_width():

    screen1 = Screen(10, 10)
    screen2 = Screen(20, 20)

    go = Gameobject(sprites=[screen1, screen2])

    assert go.width == 0

    # TODO: test after start and update
