import pytest

from graphe import Point

@pytest.fixture
def A():
    return Point("A", 4.5, 7.8)

@pytest.fixture
def B():
    return Point("B")

def test_coordonnées(A,B):
    assert A.nom == "A"
    assert A.abs == 4.5
    assert A.ordo == 7.8
    assert B == Point("B", 0, 0)

def test_distance(A,B):
    m = A.distance(B)
    assert m == (81.09)**0.5