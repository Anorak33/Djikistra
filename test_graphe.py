import pytest
from graphe import Graphe
from graphe import Point
from importation_graphe import importation_graph

@pytest.fixture
def graphe1() :
    return Graphe(importation_graph("csv_files/test_files/graph_test1.csv"))

def test_base(graphe1) :
    assert graphe1.sommet == {"Truc" : Point("Truc", 3.0, 12.0), "Muche" : Point("Muche", 45, 1), "Bidule" : Point("Bidule"), "Machin" : Point("Machin", -2, -6)}
    #assert graphe1.successeur == {"Truc" : [("Muche", ]

def test_get_Point_from_nom(graphe1) :
    pass

def chemin(graphe1) :
    pass