import csv


def importation_graph_csv(adresse_ficher_csv):
    with open(adresse_ficher_csv, newline='', encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quotechar='|')
        c_dict = {}
        for row in reader:
            c_dict[row[0]] = [row[1], row[2],(row[3], row[4], row[5])]
    return c_dict



if __name__ == "__main__":
    d = importation_graph_csv("csv_files/graph1.csv")
    print(d)