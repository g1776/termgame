import pytest
import pymunk
from termgame import PhysicsEngine, PhysicsGameobject, Gameobject


def test_init():
    """
    Test initializing the physics engine.
    """
    engine = PhysicsEngine(10, 10, gravity=(5, 9.3))
    assert engine.width == 10
    assert engine.height == 10
    assert engine.space.gravity == (5, 9.3)


def test_add_gameobject():
    """
    Test adding a PhysicsGameobject to the engine.
    """

    engine = PhysicsEngine(10, 10)

    # add a PhysicsGameobject
    go = PhysicsGameobject(name="test", x=5, y=5)
    engine.add_gameobject(go)
    assert engine.gameobjects == [go]
    assert engine.space.bodies == [go.rb]

    # add a Gameobject (should be converted to a PhysicsGameobject)
    go2 = Gameobject(name="test2", x=5, y=5)
    engine.add_gameobject(go2)

    # make sure the first gameobject is still the same,
    # and the second is a static PhysicsGameobject with the same name
    assert engine.gameobjects[0] == go
    assert isinstance(engine.gameobjects[1], PhysicsGameobject)
    assert engine.gameobjects[1].name == "test2"
    assert engine.gameobjects[1].rb.body_type == pymunk.Body.STATIC
