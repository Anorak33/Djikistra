import pytest
from graphe import *
from main import plus_court_chemin
from importation_graphe import importation_graphe

@pytest.fixture
def graphe1() :
    """Importe le 1er graphe des fichiers test, les noms de point sont des mots"""
    return Graphe(importation_graphe("fichiers_csv/fichiers_test/graphe_test1.csv"))

@pytest.fixture
def graphe2():
    """Importe le 2ème graphe des fichiers test, les noms de point sont des chiffres"""
    return Graphe(importation_graphe("fichiers_csv/fichiers_test/graphe_test2.csv"))

def test_plus_court_chemin(graphe1, graphe2):
    """Vérifie que plus_court_chemin renvoie le plus court chemin"""
    Truc = graphe1.Point_depuis_nom("Truc")
    Muche = graphe1.Point_depuis_nom("Muche")
    Bidule = graphe1.Point_depuis_nom("Bidule")
    assert plus_court_chemin(graphe1, Truc, Muche) == ([Truc, Muche], (42**2+121)**0.5) #test fonctionnement normal
    assert plus_court_chemin(graphe2, graphe2.Point_depuis_nom("1"), graphe2.Point_depuis_nom("4"))[0] in [[Point("1", 2, 3), Point("4", 5, 6)], [Point("1", 2, 3), Point("2", 3, 4), Point("4", 5, 6)], [Point("1", 2, 3), Point("3", 4, 5), Point("4", 5, 6)]] #1 parmi 3 chemins de même poids
    assert plus_court_chemin(graphe1, Truc, Truc) == ([Point("Truc",3,12)], 0) #test même départ et même arrivée
    assert plus_court_chemin(graphe1, Muche, Bidule) == ([], float("inf")) #test départ point qui n'a pas de successeur