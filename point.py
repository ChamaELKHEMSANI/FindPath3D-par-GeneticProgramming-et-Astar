# point.py
import numpy as np
import sys
import random
"""
**Description :**  
Représente un point en 3D avec des coordonnées `(x, y, z)` et un coût associé.  

**Attributs :**  
- `x, y, z` : Coordonnées du point.  
- `cost` : Coût associé au point (par défaut, une grande valeur).  

**Méthodes :**  
- `isEgaleCoord(x, y, z)`: Vérifie si les coordonnées du point correspondent à `(x, y, z)`.  
- `isEgale(pnt)`: Vérifie si deux points sont identiques.  
- `distance(pnt)`: Calcule la distance de Manhattan entre ce point et un autre.  
- `rand(size)`: Génère un point aléatoire dans une grille de taille donnée.  
"""

class Point:
    def __init__(self, x, y,z=0,cost=sys.maxsize):
        self.x = x
        self.y = y
        self.z = z
        self.cost = cost

    def isEgaleCoord(self,x, y, z):
        return self.x ==x and  self.y ==y and  self.z ==z 

    def isEgale(self,pnt):
        return self.x ==pnt.x and  self.y ==pnt.y and  self.z ==pnt.z 

    def distance(self,pnt):
        return abs(self.x - pnt.x) + abs(self.y - pnt.y) + abs(self.z - pnt.z)
        
    def rand(size):
        x = np.random.randint(0, size)
        y = np.random.randint(0, size)
        z = np.random.randint(0, size)
        return Point(x,y,z)
