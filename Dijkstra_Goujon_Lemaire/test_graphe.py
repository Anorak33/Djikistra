import pytest
from graphe import Graphe
from graphe import Point
from importation_graphe import importation_graphe

@pytest.fixture
def graphe1() :
    """Importe le 1er graphe des fichiers test, les noms de point sont des mots"""
    return Graphe(importation_graphe("fichiers_csv/fichiers_test/graphe_test1.csv"))

def test_base(graphe1) :
    """Teste les attributions des caractéristiques du graphe"""
    Truc = Point("Truc", 3.0, 12.0)
    Muche = Point("Muche", 45, 1)
    Bidule = Point("Bidule")
    Machin = Point("Machin", -2, -6)
    assert graphe1.sommet == {"Truc" : Truc, "Muche" : Muche, "Bidule" : Bidule, "Machin" : Machin}
    assert graphe1.successeurs == {Truc : {(Muche, Truc.distance(Muche)), (Bidule, Truc.distance(Bidule))}, Muche : set(), Bidule : {(Muche, Bidule.distance(Muche))}, Machin : {(Muche, Machin.distance(Muche))}}

def test_Point_depuis_nom(graphe1) :
    """Vérifie que la fonction récupère bien le point associé au même nom"""
    assert graphe1.Point_depuis_nom("Muche")==Point("Muche", 45, 1)

def test_successeurs_sommet(graphe1) :
    """Vérifie que la fonction récupère les successeurs du point demandé"""
    Truc = Point("Truc", 3.0, 12)
    Muche = Point("Muche", 45, 1)
    Bidule = Point("Bidule")
    assert graphe1.successeurs_sommet(Truc) == {(Muche, Truc.distance(Muche)), (Bidule,Truc.distance(Bidule))} #fonctionnement classique
    assert graphe1.successeurs_sommet(Muche) == set() #pas de successeurs

def test_graphe_vide():
    """Vérifie que le graphe vide a ses attributs successeurs et sommets vides"""
    assert Graphe({}).sommet == {}
    assert Graphe({}).successeurs == {}








