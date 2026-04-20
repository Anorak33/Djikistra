class InitialisationCSVErreur(Exception):
    """Exception levée lorsque la première ligne du fichier csv n'est pas conforme à ce qui est attendu pour l'importation du graphe"""
    pass

def importation_graphe(adresse_fichier_csv:str)->dict:
    """Importe un graphe à partir d'un fichier csv de la forme :
        depart,depart_abscisse,depart_ordonnee,arrivee,arrivee_abscisse,arrivee_ordonnee
        nom_sommet1,coord_x,coord_y,nom_successeur1,coord_x_successeur1,coord_y_successeur1
        nom_sommet1,coord_x,coord_y,nom_successeur2,coord_x_successeur2,coord_y_successeur2
        nom_sommet2,coord_x,coord_y,nom_successeur1,coord_x_successeur1,coord_y_successeur1
        ...
    Paramètre:
        adresse_fichier_csv (str): adresse du ficher csv

    Renvoie:
        dict: dictionnaire de la forme {"A":((x,y),{successeurs}), "B":((x,y),{successeurs}), ...}
    """
    with open(adresse_fichier_csv, newline='', encoding="utf-8") as csv_file:
        texte = csv_file.read()

    lignes = texte.split()
    if lignes[0] != "depart,depart_abscisse,depart_ordonnee,arrivee,arrivee_abscisse,arrivee_ordonnee":
        raise InitialisationCSVErreur("Le fichier csv n'est pas conforme à ce qui est attendu pour l'importation du graphe, la première ligne doit être : depart,depart_abscisse,depart_ordonnee,arrivee,arrivee_abscisse,arrivee_ordonnee")
   
    lignes_propre = [v.split(',') for v in lignes[1:]] #On enlève la première ligne et on sépare les éléments de chaque ligne
    dictionnaire_graphe = {}

    if lignes_propre == []:
        return dictionnaire_graphe

    for ligne in lignes_propre:
        if ligne[0] not in dictionnaire_graphe.keys():             #Ajoute le sommet au dictionnaire s'il n'exite pas
                dictionnaire_graphe[ligne[0]] = ((float(ligne[1]),float(ligne[2])), set())
        if ligne[3] not in dictionnaire_graphe.keys():             #Ajoute le successeur au dictionaire s'il n'existe pas
            dictionnaire_graphe[ligne[3]] = ((float(ligne[4]),float(ligne[5])), set())
        (dictionnaire_graphe[ligne[0]][1]).add(ligne[3])           #Ajoute le succeseur du sommet à sa liste de successeur
    return dictionnaire_graphe