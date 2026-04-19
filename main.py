import time
from graphe import *
from importation_graphe import importation_graphe

class PoidNegatifErreur(Exception):
    pass

def charger_csv(nom_fichier:str)->Graphe:
    return Graphe(importation_graphe(f"csv_files/{nom_fichier}"))

def reconstruire_chemin(chemin, noeud_source, noeud_cible):
    print(chemin)
    liste_chemin = [noeud_cible]
    while noeud_cible != noeud_source:
        noeud_cible = chemin[noeud_cible]
        liste_chemin.append(noeud_cible)
        print(noeud_cible)
        print(noeud_source)
    return reversed(liste_chemin)

def dijkstra(graphe, noeud_source, noeud_cible):
    
    distance = {s: 0 if s == noeud_source else float('inf') for s in graphe.sommet.values()}   
    
    non_visites = set(graphe.sommet.values())-{noeud_source}
    successeurs_noeud_visite = set()

    chemin = {}
    
    #Initialisation pour noeud_source
    for successeur, poids in graphe.chemin(noeud_source):
        successeurs_noeud_visite.add(successeur)
        nouvelle_distance = distance[noeud_source] + poids
        distance[successeur] = nouvelle_distance
        chemin[successeur] = noeud_source
    x = time.time()

    while non_visites != set():
        # print('d', len(non_visites))
        noeud_actuel = None
        # a = time.time()
        for noeud in non_visites&successeurs_noeud_visite:
            if noeud_actuel is None or distance[noeud] < distance_noeud_actuel:
                noeud_actuel = noeud
                distance_noeud_actuel = distance[noeud_actuel]
        
        if noeud_actuel is None or distance_noeud_actuel == float('inf'): #Tous les noeuds restants sont inaccessibles depuis noeud_source
            return float('inf'),[]

        if distance_noeud_actuel < 0:
            raise PoidNegatifErreur(f"L'arc entre {chemin[noeud_actuel][-1]} et {noeud_actuel} contient un poid négatif")

        if noeud_actuel == noeud_cible: 
            break
  
        for successeur, poids in graphe.chemin(noeud_actuel):
            successeurs_noeud_visite.add(successeur)
            nouvelle_distance = distance[noeud_actuel] + poids
            if nouvelle_distance < distance[successeur]:
                distance[successeur] = nouvelle_distance
                chemin[successeur] = noeud_actuel

        non_visites.remove(noeud_actuel)
    print(time.time()-x)

        
    return distance[noeud_cible],reconstruire_chemin(chemin,noeud_source,noeud_cible)

def main(nom_fichier, source, cible):
    graphe = charger_csv(nom_fichier)
    noeud_source = graphe.get_Point_from_nom(source)
    noeud_cible = graphe.get_Point_from_nom(cible)
    return dijkstra(graphe, noeud_source, noeud_cible)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("--fichier", required=True, help="Le fichier.csv du graphe") 
    parser.add_argument("--source", required=True, help="Le point source") 
    parser.add_argument("--cible", required=True, help="Le point cible") 
    args = parser.parse_args()
    x = time.time()
    distance,chemin = main((args.fichier),args.source, args.cible)
    print(time.time()-x)
    print(f"Distance({args.source}->{args.cible}) = {(distance//0.01)/100}")
    print("Chemin : ", end="")
    print("->".join(map(str,chemin)))
    # from ressources.tracer_toulouse import tracer_route_toulouse
    # fichier = "ressources/toulouse.graphml"
    # tracer_route_toulouse(fichier, list(map(int,chemin)))
