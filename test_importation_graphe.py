import pytest

from importation_graphe import importation_graph

@pytest.fixture
def graphe():
    return importation_graph("csv_files/test_files/graphe_test1.csv")

def test_egalite(graphe):
    pass