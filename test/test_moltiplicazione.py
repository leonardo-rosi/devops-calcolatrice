from operazioni import moltiplicazione


def test_moltiplicazione_interi():
    assert moltiplicazione(2, 3) == 6
    assert moltiplicazione(-2, 3) == -6
    assert moltiplicazione(7, -1) == -7


def test_moltiplicazione_decimali():
    assert moltiplicazione(2.5, 2) == 5.0
    assert moltiplicazione(-1.5, 2) == -3.0
    assert moltiplicazione(0.5, 0.2) == 0.1


def test_moltiplicazione_con_stringhe():
    assert moltiplicazione("a", 2) is None
    assert moltiplicazione(2, "b") is None
    assert moltiplicazione("a", "b") is None


def test_moltiplicazione_per_zero():
    assert moltiplicazione(0, 0) == 0
    assert moltiplicazione(0, 10) == 0
    assert moltiplicazione(10, 0) == 0
