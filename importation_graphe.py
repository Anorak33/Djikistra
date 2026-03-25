def importation_graph(adresse_fichier_csv:str):
    with open(adresse_fichier_csv, newline='', encoding="utf-8") as csv_file:
        texte = csv_file.read()
    lignes = texte.split()
    lignes_propre = [v.split(',') for v in lignes]
    dictionnaire_graphe = {}

    for ligne in lignes_propre:
        if ligne[0] not in dictionnaire_graphe.keys():             #Ajoute le point au dictionnaire s'il n'exite pas
                dictionnaire_graphe[ligne[0]] = ((float(ligne[1]),float(ligne[2])), [])
        if ligne[3] not in dictionnaire_graphe.keys():             #Ajoute le successeur au dictionaire s'il n'existe pas
            dictionnaire_graphe[ligne[3]] = ((float(ligne[4]),float(ligne[5])), [])
        dictionnaire_graphe[ligne[0]][1].append(ligne[3])            #Ajoute le succeseur du point à sa liste de successeur
    return dictionnaire_graphe 

if __name__ == "__main__":
    d = importation_graph("csv_files/graph1.csv")
    print(d)