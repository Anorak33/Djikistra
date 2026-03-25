

from graphe import *
from importation_graphe import importation_graph

def charger_csv(nom_fichier):
    return Graphe(importation_graph(f"csv_files/{nom_fichier}"))

def dijkstra(graphe, source, cible):
    C_cible = [-1 for i in range(len(graphe.sommet))]
    for succ in graphe.successeur(source):
        if cible == succ[0]:
            C_cible = succ[1]
            break   
    S = {source}
    R = graphe.sommet-S
    i = 0
    while R != set():
        pass
        
def main(nom_fichier, source, cible):
    graphe = charger_csv(nom_fichier)
    return dijkstra(graphe, source, cible)



if __name__ == "__main__":
    graphe = charger_csv("graph1.csv")
    for s in graphe.sommet:
        print(graphe.chemin(s))


if __name__ == "__main2__":
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("--fichier", required=True, help="Le fichier.csv du graphe") 
    parser.add_argument("--source", required=True, help="Le point source") 
    parser.add_argument("--cible", required=True, help="Le point cible") 

    args = parser.parse_args()
    print(args.fichier, args.source, args.cible)