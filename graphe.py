class Point :
    """Point répérés par son nom et ses coordonnées"""

    def __init__(self,nom:str, x:float=0, y:float=0):
        self.abs = x
        self.ordo = y
        self.nom = nom
    
    def __str__(self):
        return self.nom

    def __repr__(self):
        return self.nom

    def distance(self,autre:"Point") :
        x1 = self.abs
        y1 = self.ordo
        x2 = autre.abs
        y2 = autre.ordo
        distance = ((x1-x2)**2 + (y1-y2)**2)**(0.5)
        return distance
    
    def __eq__(self, autre:"Point") :
        return self.nom == autre.nom and self.abs == autre.abs and self.ordo == autre.ordo

    def __hash__(self):
        return hash((self.nom, self.abs, self.ordo))
    
class Graphe :
    """Graphe orienté pondéré
    liste de sommet associé à un tuple (coordonnées) et liste arcs"""
    # TODO Gérer les points pareils

    def __init__ (self,g_dict:dict): #Le format de dictionnaire de importation_graph_csv : {"A":((x,y),[successeurs]), "B":((x,y),[successeurs]), ...}
        self.sommet = set()
        self.successeur = []
        for nom, caracteristique, in g_dict.items():    
            self.sommet.add(Point(nom, *caracteristique[0]))
        for nom, caracteristiques in g_dict.items() :
            for point in self.sommet :
                if nom==point.nom :
                    truc=[]
                    for caracteristique in caracteristiques[1] :
                        for pointgraphe in self.sommet :
                            if caracteristique==pointgraphe.nom :
                                truc.append((pointgraphe, point.distance(pointgraphe)))
                    self.successeur.append((point,truc))
                    
    def __eq__ (self, autre:"Graphe"):
        pass

    def chemin(self,point:Point):
        """Renvoie les successeurs d'un point au sein du graphe"""
        for s in self.successeur:
                if s[0]==point :
                    return s[1]
    def get_Point_from_nom(self, nom:str):
        for point in self.sommet:
            if point.nom == nom:
                return point
        raise ValueError(f"Le point avec le nom {nom} n'existe pas dans le graphe.")  

if __name__=="__main__" :
    A=Point("A",0,2)
    B=Point("B",0,3)
    print(A.distance(B))
