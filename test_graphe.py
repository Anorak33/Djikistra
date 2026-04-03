import pytest
from graphe import *
from importation_graphe import importation_graph

@pytest.fixture
def graphe1() :
    return importation_graph("csv_files/graph1.csv")

def test_base(graphe1) :
    