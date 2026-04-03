import pytest

from importation_graphe import importation_graph

@pytest.fixture
def graphe_l():
    return importation_graph("csv_files/test_files/graphe_test1.csv")

@pytest.fixture
def graphe_n():
    return importation_graph("csv_files/test_files/graphe_test2.csv")

def test_egalite(graphe_l,graphe_n):
    dicol={'Truc' : ((3.0, 12.0), ['Muche', 'Bidule']), 'Muche' : ((45.0, 1.0), []), 'Bidule' : ((0.0, 0.0), ['Muche']), 'Machin' : ((-2.0, -6.0), ['Muche'])}
    assert type(graphe_l)==dict
    assert dicol == graphe_l
    dicon={'1' : ((2.0, 3.0), ['4','3']), '2' : ((3.0,4.0), ['4','6']), '3' : ((4.0, 5.0), ['4']), '4' : ((5.0,6.0), []), '6' : ((7.0,8.0), []) }
    assert type(graphe_n)==dict
    assert dicon == graphe_n