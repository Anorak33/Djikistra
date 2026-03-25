import csv

def importation_graph_csv(adresse_ficher_csv:str)->dict:
    with open(adresse_ficher_csv, newline='', encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quotechar='|')
        g_dict = {}
        for row in reader:
            if row[0] not in g_dict.keys():             #Ajoute le point au dictionnaire s'il n'exite pas
                g_dict[row[0]] = ((float(row[1]),float(row[2])), [])
            if row[3] not in g_dict.keys():             #Ajoute le successeur au dictionaire s'il n'existe pas
                g_dict[row[3]] = ((float(row[4]),float(row[5])), [])
            g_dict[row[0]][1].append(row[3])            #Ajoute le succeseur du point à sa liste de successeur
    return g_dict



if __name__ == "__main__":
    d = importation_graph_csv("csv_files/graph1.csv")
    print(d)