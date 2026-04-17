from time import time

from graphe import *
from importation_graphe import importation_graph


def charger_csv(nom_fichier):
    return Graphe(importation_graph(f"csv_files/{nom_fichier}"))

def dijkstra(graphe, source, cible):
    noeud_source = graphe.get_Point_from_nom(source)
    noeud_cible = graphe.get_Point_from_nom(cible)
    distance = {s: 0 if s == noeud_source else float('inf') for s in graphe.sommet.values()}   
    
    non_visites = set(graphe.sommet.values())-{noeud_source}
    successeurs_noeud_visite = set()

    chemin = {}

    #Initialisation pour noeud_source
    for successeur, poids in graphe.chemin(noeud_source):
        successeurs_noeud_visite.add(successeur)
        nouvelle_distance = distance[noeud_source] + poids
        # if nouvelle_distance < distance[successeur]:
        distance[successeur] = nouvelle_distance
        chemin[successeur] = [noeud_source]

    while non_visites != set():
        print('d', len(non_visites))
        noeud_actuel = None
        
        for noeud in non_visites&successeurs_noeud_visite:
            if noeud_actuel is None or distance[noeud] < distance[noeud_actuel]:
                noeud_actuel = noeud
        
        if distance[noeud_actuel] == float('inf') or noeud_actuel is None: #Tous les noeuds restants sont inaccessibles depuis noeud_source
            break
        for successeur, poids in graphe.chemin(noeud_actuel):
            successeurs_noeud_visite.add(successeur)
            nouvelle_distance = distance[noeud_actuel] + poids
            if nouvelle_distance < distance[successeur]:
                distance[successeur] = nouvelle_distance
                chemin[successeur] = [noeud_actuel]+chemin[noeud_actuel]
        
        non_visites.remove(noeud_actuel)
        
    return distance[noeud_cible],chemin[noeud_cible]

    

def main(nom_fichier, source, cible):
    graphe = charger_csv(nom_fichier)
    return dijkstra(graphe, source, cible)



# if __name__ == "__main__":
#     graphe = charger_csv("graph1.csv")
#     for s in graphe.sommet:
#         print(graphe.chemin(s))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("--fichier", required=True, help="Le fichier.csv du graphe") 
    parser.add_argument("--source", required=True, help="Le point source") 
    parser.add_argument("--cible", required=True, help="Le point cible") 
    args = parser.parse_args()
    distance,chemin = dijkstra(charger_csv(args.fichier),args.source, args.cible)
    # print("{:.2f}".format(dijkstra(charger_csv(args.fichier), args.source, args.cible)))
    print(distance)
    print(chemin)