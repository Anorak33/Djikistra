import pytest

from importation_graphe import importation_graphe

@pytest.fixture
def graphe_l(): 
    """Importe le 1er graphe des fichiers test, les noms de point sont des mots"""
    return importation_graphe("fichiers_csv/fichiers_test/graphe_test1.csv")

@pytest.fixture
def graphe_n():
    """Importe le 2ème graphe des fichiers test, les noms de point sont des chiffres"""
    return importation_graphe("fichiers_csv/fichiers_test/graphe_test2.csv")

def test_egalite(graphe_l,graphe_n):
    """Vérifie l'égalité entre le graphe créé correspondand au fichier et l'importation par importation_graphe
    Vérifie également le type de l'objet crée (ici doit être dictionnaire)"""
    dico_l={'Truc' : ((3.0, 12.0), {'Muche', 'Bidule'}), 'Muche' : ((45.0, 1.0), set()), 'Bidule' : ((0.0, 0.0), {'Muche'}), 'Machin' : ((-2.0, -6.0), {'Muche'})}
    assert type(graphe_l) == dict
    assert dico_l == graphe_l
    dico_n={'1' : ((2.0, 3.0), {'4','2','3'}), '2' : ((3.0,4.0), {'4','6'}), '3' : ((4.0, 5.0), {'4'}), '4' : ((5.0,6.0), set()), '6' : ((7.0,8.0), set()) }
    assert type(graphe_n) == dict
    assert dico_n == graphe_n

def test_graphe_vide():
    """Importe un graphe vide"""
    dico_v = importation_graphe("fichiers_csv/fichiers_test/graphe_vide.csv")
    assert type(dico_v) == dict
    assert dico_v == {}
