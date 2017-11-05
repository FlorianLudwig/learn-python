import gol


def test_gol():
    assert gol.decide_alive(False, 2) == False
    assert gol.decide_alive(False, 3) == True
    assert gol.decide_alive(True, 2) == True
    assert gol.decide_alive(True, 1) == False
    assert gol.decide_alive(True, 4) == False
    assert gol.decide_alive(False, 5) == False


def check_field_basics(field):
    # basic field should be empty
    assert field.get(0, 0) == False
    assert field.get(1, 0) == False
    assert field.get(1, 4) == False

    field.set(0, 0, True)
    assert field.get(0, 0) == True
    # all neighbours should be still dead
    for pos in gol.neighbour_iter(0, 0):
        assert field.get(*pos) == False
    assert field.count_neighbours(0, 0) == 0
    assert field.count_neighbours(0, 1) == 1

def test_infinite_field():
    field = gol.InfiniteField()
    check_field_basics(field)

    # negative values should work
    assert field.get(-1, 4) == False
    assert field.get(1, -4) == False


def test_fixed_field():
    field = gol.FixedField(10, 10)
    check_field_basics(field)

    # setting out of bound should do nothing
    field.set(-1, -1, True)
    assert field.get(-1, -1) == False
