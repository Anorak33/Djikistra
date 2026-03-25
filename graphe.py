class Point :
    """Point répérés par son nom et ses coordonnées"""

    def __init__(self,nom:str, x:float, y:float):
        self.abs = x
        self.ordo = y
        self.nom = nom

    def distance(self,autre:"Point") :
        x1 = self.abs
        y1 = self.ordo
        x2 = autre.abs
        y2 = autre.ordo
        distance = ((x1-x2)**2 + (y1-y2)**2)**(0.5)
        return distance
        
class Graphe :
    """Graphe orienté pondéré
    liste de sommet associé à un tuple (coordonnées) et liste arcs"""

    def __init__ (self,g_dict:dict): #Le format de dictionnaire de importation_graph_csv : {"A":((x,y),[successeurs]), "B":((x,y),[successeurs]), ...}
        self.sommet = set()
        for nom, caracteristique in g_dict.items():
            self.sommet.add(Point(nom, *caracteristique[0]))


    def truc(self):
        pass