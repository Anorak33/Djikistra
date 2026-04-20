import pytest

from graphe import Point

@pytest.fixture
def A():
    """Crée un point A avec des coordonnées en float"""
    return Point("A", 4.5, 7.8)

@pytest.fixture
def B():
    """Crée un point B avec les coordonnées par défaut"""
    return Point("B")

def test_coordonnées(A,B):
    """Vérifie l'attribution des caractéristiques et le fonctionnement de l'attricution par défaut"""
    assert A.nom == "A"
    assert A.abs == 4.5
    assert A.ordo == 7.8
    assert B == Point("B", 0, 0)

def test_distance(A,B):
    """Vérifie la distance entre A et B"""
    m = A.distance(B)
    assert m == (81.09)**0.5
    assert A.distance(A) == 0 #test distance point et lui même
    assert Point("C", -3, -4).distance(Point("D", -1, 0)) == (20)**0.5