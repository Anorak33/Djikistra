import pytest
from graphe import Graphe
from graphe import Point
from importation_graphe import importation_graph

@pytest.fixture
def graphe1() :
    return Graphe(importation_graph("csv_files/graph1.csv"))

def test_base(graphe1) :
    assert graphe1.sommet == (Point("Truc", 3.0, 12.0), Point("Muche"), Point("Bidule"), Point("Machin"))