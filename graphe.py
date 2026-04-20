class Point :
    """Point répérés par son nom et ses coordonnées"""

    def __init__(self,nom:str, x:float=0, y:float=0):
        """
        Point répérés par son nom et ses coordonnées
        Paramètre:
            nom (str): le nom
            x (float): la coordonnée x.
            y (float): la coordonnée y. 
        """
        self.abs = x
        self.ordo = y
        self.nom = nom
    
    def __str__(self):
        return self.nom

    def __repr__(self):
        return self.nom

    def distance(self,autre:"Point")->float:
        """Renvoie la distance euclidienne entre deux points

        Paramètre:
            autre (Point): le point avec lequel on veut calculer la distance

        Returns:
            float: la distance euclidienne entre les deux points
        """
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
    
class Graphe:
    """Graphe orienté pondéré : prend en argument un dictionnaire 
    Attribut sommet : dictionnaire, sommet associé au point correspondant
    Attribut successeurs : dictionnaire, nom de point associé à un tuple du tuple des coordonnées de ce point et de la liste des noms des successeurs (str)
    """


    def __init__ (self,g_dict:dict): #Le format de dictionnaire de importation_graphe : {"A":((x,y),{successeurs}), "B":((x,y),{successeurs}), ...}
        self.sommet = {} #Dictionnaire de la forme {nom:Sommet, nom:Sommet,...}
        self.successeurs = {} #Dictionnaire de la forme {Sommet: [(Sommet, distance), (Sommet, distance), ...], ...}
        for nom, caracteristique, in g_dict.items():    
            self.sommet[nom] = Point(nom, *caracteristique[0])
        i = len(g_dict)
        for sommet in self.sommet.values():
            # print('c', str(i))
            i-=1
            liste_successeurs = g_dict[sommet.nom][1]
            self.successeurs[sommet] = {(self.Point_depuis_nom(successeur), sommet.distance(self.Point_depuis_nom(successeur))) for successeur in liste_successeurs}

    def successeurs_sommet(self,sommet:Point)->set:
        """Renvoie les successeurs de sommet, et les distances associées

        Paramètre:
            sommet (Point): le sommet pour lequel on veut obtenir les successeurs

        Returns:
            set: l'ensemble des successeurs du sommet avec leurs distances associées, de la forme {(successeur1, distance1), (successeur2, distance2), ...}
        """
        return self.successeurs.get(sommet,{})
                
    def Point_depuis_nom(self, nom:str)->Point:
        """Renvoie l'objet de type Point associé au nom du sommet

        Paramètre:
            nom (str): le nom du point que l'on veut obtenir

        Returns:
            Point: le point correspondant au nom donné
        """
        try:
            return self.sommet[nom]
        except KeyError:
            raise ValueError(f"Le Point '{nom}' n'est pas dans le graphe")
