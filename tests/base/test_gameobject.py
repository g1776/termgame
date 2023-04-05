import pytest
from termgame import Gameobject, Screen, Engine


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


def test_width_and_height():

    screen1 = Screen(10, 15)
    screen2 = Screen(20, 25)

    go = Gameobject(sprites=[screen1, screen2])

    assert go.width == 0
    assert go.height == 0

    # attach to engine so we can test on start and update
    e = Engine(100, 100, [go])
    go.on_start(e)

    # these values should come from the first sprite
    assert go.width == 10
    assert go.height == 15

    # call on_update to change the active sprite
    go.on_update(1, e)

    # now it should be the width and height of the second sprite
    assert go.width == 20
    assert go.height == 25


def test_width_height_no_sprites():
    go = Gameobject(sprites=None)
    assert go.width == 0
    assert go.height == 0


def test_name():
    go = Gameobject(name="test")
    assert go.name == "test"


def test_get_sprites():

    screen1 = Screen(10, 15)
    screen2 = Screen(20, 25)

    go = Gameobject(sprites=[screen1, screen2])

    assert go.get_sprites() == [screen1, screen2]


def test_get_sprites_no_sprites():

    go = Gameobject(sprites=None)

    assert go.get_sprites() == []


def test_get_active_sprite():

    screen1 = Screen(10, 15)
    screen2 = Screen(20, 25)

    go = Gameobject(sprites=[screen1, screen2])

    # attach to engine so we can test on start and update
    e = Engine(100, 100, [go])
    go.on_start(e)

    assert go.get_active_sprite() == screen1

    # call on_update to change the active sprite
    go.on_update(1, e)

    assert go.get_active_sprite() == screen2


def test_get_active_sprite_no_sprites():

    go = Gameobject(sprites=None)

    assert go.get_active_sprite() is None
