from graphe import *
from importation_graphe import *

class PoidNegatifErreur(Exception):
    """
    Exception levée lorsque le graphe contient un arc avec un poids négatif, ne devrait pas se produire dans ce projet
    """
    pass

def charger_csv(nom_fichier:str)->Graphe:
    """Charge un graphe à partir d'un fichier csv, le format du csv doit être respecté pour que le chargement fonctionne, sinon une erreur sera levée

    Paramètre:
        nom_fichier (str): un nom fichier.csv, le fichier doit être dans le dossier fichiers_csv

    Renvoie:
        Graphe: le graphe chargé à partir du fichier csv
    """
    return Graphe(importation_graphe(f"fichiers_csv/{nom_fichier}"))
    

def reconstruire_chemin(chemin:dict, noeud_source:Point, noeud_cible:Point)->list[Point]:
    """Renvoie la liste des points constituant le chemin entre le noeud source et le noeud cible, à partir du dictionnaire de chemin construit par l'algorithme de Dijkstra

    Paramètre:
        chemin (dict): Dictionnaire de la forme {noeud: noeud_précédent, ...} construit par l'algorithme de Dijkstra
        noeud_source (Point): Le noeud de départ
        noeud_cible (Point): Le noeud d'arrivée

    Renvoie:
        list[Point]: La liste des points constituant le chemin
    """    
    liste_chemin = [noeud_cible]
    while noeud_cible != noeud_source:
        noeud_cible = chemin[noeud_cible]
        liste_chemin.append(noeud_cible)
    liste_chemin.reverse()
    return liste_chemin

def plus_court_chemin(graphe:Graphe, noeud_source:Point, noeud_cible:Point)->tuple[list[Point], float]:
    """Renvoie le plus court chemin entre le noeud source et le noeud cible, ainsi que la distance de ce chemin, en utilisant l'algorithme de Dijkstra

    Paramètre:
        graphe (Graphe): Le graphe dans lequel on cherche le plus court chemin
        noeud_source (Point): Le noeud de départ
        noeud_cible (Point): Le noeud d'arrivée

    Renvoie:
        tuple[list[Point], float]: La liste des points constituant le chemin et la distance de ce chemin
    """

    if noeud_source == noeud_cible: #Pas besoin de faire l'algorithme de Dijkstra si le noeud de départ et le noeud d'arrivée sont les mêmes
        return [noeud_source], 0
    
    distance = {s: 0 if s == noeud_source else float('inf') for s in graphe.sommet.values()}   
    
    non_visites = set(graphe.sommet.values())-{noeud_source}
    successeurs_noeud_visite = set()

    chemin = {}
    #Initialisation pour noeud_source
    for successeur, poids in graphe.successeurs_sommet(noeud_source):
        successeurs_noeud_visite.add(successeur)
        nouvelle_distance = distance[noeud_source] + poids
        distance[successeur] = nouvelle_distance
        chemin[successeur] = noeud_source

    while non_visites != set():
        noeud_actuel = None
        #On trouve le noeud non visité avec la plus petite distance
        for noeud in non_visites&successeurs_noeud_visite:  # Les noeuds qui ne sont pas des successeurs d'un noeud déjà visité ont forcement une distance infinie, on peut donc les ignorer
            if noeud_actuel is None or distance[noeud] < distance_noeud_actuel:
                noeud_actuel = noeud
                distance_noeud_actuel = distance[noeud_actuel]
        
        #Gestion des cas particuliers
        if noeud_actuel is None or distance_noeud_actuel == float('inf'): #Tous les noeuds restants sont inaccessibles depuis noeud_source
            return [], float('inf')

        elif distance_noeud_actuel < 0:   #! Cette erreur ne devrait pas se produire dans ce projet (car une norme est positive)
            raise PoidNegatifErreur(f"L'arc entre {chemin[noeud_actuel][-1]} et {noeud_actuel} contient un poid négatif")

        elif noeud_actuel == noeud_cible: 
            break
        
        #On met à jour les distances des successeurs du noeud actuel
        for successeur, poids in graphe.successeurs_sommet(noeud_actuel):
            successeurs_noeud_visite.add(successeur)
            nouvelle_distance = distance_noeud_actuel + poids
            if nouvelle_distance < distance[successeur]:
                distance[successeur] = nouvelle_distance
                chemin[successeur] = noeud_actuel

        non_visites.remove(noeud_actuel)
    return reconstruire_chemin(chemin,noeud_source,noeud_cible), distance[noeud_cible]

def main(nom_fichier:str, source:str, cible:str)->None:
    """Affiche le plus court chemin entre le noeud source et le noeud cible, ainsi que la distance de ce chemin, à partir d'un fichier csv contenant un graphe, en utilisant l'algorithme de Dijkstra
        On affiche également la route sur une carte si le fichier csv correspond au graphe de Toulouse
        on fait aussi toute la gestion des erreurs ici

    Paramètre:
        nom_fichier (str): Le nom du fichier csv du graphe à charger, le fichier doit être dans le dossier fichiers_csv
        source (str): Le nom du noeud de départ
        cible (str): Le nom du noeud d'arrivée
    """
    try:
        graphe = charger_csv(nom_fichier)
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
        return
    except InitialisationCSVErreur as e:
        print(e)
    except Exception as e: #Une autre erreur peut survenir, si la structure du csv n'est pas respectée
        print(f"Une erreur est survenue lors du chargement du graphe : {e}")
        return

    try:
        noeud_source = graphe.Point_depuis_nom(source)
    except ValueError as e:
        print(e)
        return

    try:
        noeud_cible = graphe.Point_depuis_nom(cible)
    except ValueError as e:
        print(e)
        return

    chemin,distance = plus_court_chemin(graphe, noeud_source, noeud_cible)
    print(f"Distance({source}->{cible}) = {distance:.2f}")
    print("Chemin : ", end="")
    print(" -> ".join(map(str,chemin)))

    if nom_fichier == "toulouse.csv":
        try : 
            from ressources.tracer_toulouse import tracer_route_toulouse
            fichier = "ressources/toulouse.graphml"
            tracer_route_toulouse(fichier, list(map(lambda x: int(str(x)),chemin)))
        except Exception as e: #Simplement pour éviter de faire planter le programme si le tracé ne fonctionne pas pour x ou y raison
            print("Impossible de tracer la route : ", e)


if __name__ == "__main__":
    import argparse     #La bibliothèque la plus pratique pour gérer les arguments dans le terminal, elle fait partie des bibliothèques standards de Python
    parser = argparse.ArgumentParser()

    parser.add_argument("--fichier", required=True, help="Le fichier.csv du graphe") 
    parser.add_argument("--source", required=True, help="Le sommet source") 
    parser.add_argument("--cible", required=True, help="Le sommet cible") 
    args = parser.parse_args()

    main(args.fichier, args.source, args.cible)
