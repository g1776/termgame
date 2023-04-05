import pytest
from termgame import Engine, Gameobject


@pytest.fixture
def full_engine_fixture() -> Engine:
    """
    Create a full engine with a few gameobjects.
    """
    engine = Engine(10, 10)
    go_d1 = Gameobject(name="d1", depth=1)
    go_d2 = Gameobject(name="d2", depth=2)
    go_d0 = Gameobject(name="d0", depth=0)
    go_dn1 = Gameobject(name="dn1", depth=-1)
    engine.add_gameobject(go_d1)
    engine.add_gameobject(go_d2)
    engine.add_gameobject(go_d0)
    engine.add_gameobject(go_dn1)
    return engine


def test_add_gameobject():
    """
    Test adding gameobjects to the engine, and that they are sorted by depth.
    """
    engine = Engine(10, 10)

    go_d1 = Gameobject(name="d1", depth=1)
    go_d2 = Gameobject(name="d2", depth=2)
    go_d0 = Gameobject(name="d0", depth=0)
    go_dn1 = Gameobject(name="dn1", depth=-1)
    engine.add_gameobject(go_d1)
    engine.add_gameobject(go_d2)
    engine.add_gameobject(go_d0)
    engine.add_gameobject(go_dn1)
    assert engine.gameobjects == [go_dn1, go_d0, go_d1, go_d2]


def test_get_gameobjects(full_engine_fixture: Engine):
    """
    Test getting gameobjects by name.
    """

    assert full_engine_fixture.get_gameobjects("d1") == [full_engine_fixture.gameobjects[2]]
    assert full_engine_fixture.get_gameobjects(["d1", "d2"]) == [
        full_engine_fixture.gameobjects[2],
        full_engine_fixture.gameobjects[3],
    ]
    assert full_engine_fixture.get_gameobjects() == full_engine_fixture.gameobjects
