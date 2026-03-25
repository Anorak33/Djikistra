import sys

# sys.argv[0] est le nom du script (main.py)
# On récupère les valeurs aux positions 2, 4 et 6 basées sur ta commande



from graphe import Graphe
from importation_graphe import importation_graph_csv

def charger_csv(nom_fichier):
    return Graphe(importation_graph_csv(f"csv_files/{nom_fichier}"))

def dijkstra(graphe, source, cible):
    

def main(nom_fichier, source, cible):
    graphe = charger_csv(nom_fichier)
    return 


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("--fichier", required=True, help="Le fichier.csv du graphe") 
    parser.add_argument("--source", required=True, help="Le point source") 
    parser.add_argument("--cible", required=True, help="Le point cible") 

    args = parser.parse_args()
    main(args.fichier, args.source, args.cible)