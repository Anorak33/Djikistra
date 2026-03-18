class Point :
    """Point répérés par son nom et ses coordonnées"""

    def __init__(self,x:float,y:float,nom:str):
        self.abs=x
        self.ordo=y
        self.nom=nom

    def distance(self,autre:"Point") :
        x1=self.abs
        y1=self.ordo
        x2=autre.abs
        y2=autre.ordo
        distance=((x1-x2)**2+(y1-y2)**2)**(0.5)
        return distance
        
class Graphe :
    """Graphe orienté pondéré
    liste de sommet associé à un tuple (coordonnées) et liste arcs"""

    def __init__ (self,sommet,arc) :
       self.sommet=sommet
       self.arc=arc
    
    def truc(self):
        pass