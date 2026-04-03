from graphe import *
from importation_graphe import importation_graph

def charger_csv(nom_fichier):
    return Graphe(importation_graph(f"csv_files/{nom_fichier}"))

def dijkstra(graphe, source, cible):
    # C_cible = [-1 for i in range(len(graphe.sommet))]   #todo comprhension
    # for succ in graphe.successeur(source):
    #     if cible == succ[0]:
    #         C_cible = succ[1]
    #         break   
    S = {source}
    distance = {s: 0 if s == source else float('inf') for s in graphe.sommet}  
    distance[source] = 0
    

    non_visites = graphe.sommet-S
    i = 0
    s
    while non_visites != set():
        noeud_actuel = None
        for noeud in non_visites&graphe.successeur(source):
            if noeud_actuel is None or distance[noeud] < distance[noeud_actuel]:
                noeud_actuel = noeud

        if distance[noeud_actuel] == float('inf'):
            break

        S.add(noeud_actuel)
        non_visites.remove(noeud_actuel)

        for succ in graphe.successeur(noeud_actuel):
            voisin, poids = succ
            if voisin in non_visites:
                nouvelle_distance = distance[noeud_actuel] + poids
                if nouvelle_distance < distance[voisin]:
                    distance[voisin] = nouvelle_distance

    return distance[cible]

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