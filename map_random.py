# map_random.py
"""

**Description :**  
Génère une carte 3D avec des obstacles aléatoires.  

**Attributs :**  
- `size` : Taille de la grille.  
- `obstacle` : Nombre d'obstacles.  
- `obstacle_point` : Liste des points représentant les obstacles.  

**Méthodes :**  
- `GenerateObstacle()`: Génère des obstacles de différentes formes.  
- `AddObstaclePoint(x, y, z)`: Ajoute un point obstacle si valide.  
- `IsObstacle(i, j, k)`: Vérifie si un point est un obstacle.  
- `IsValidPoint(x, y, z)`: Vérifie si un point est dans les limites de la carte.  

"""
import numpy as np
from point import *

class MapRandom:
    def __init__(self, size=50,obstacle=10):
        self.size = size
        self.obstacle = obstacle
        self.GenerateObstacle()

    def GenerateObstacle(self):
        self.obstacle_point = []

        for i in range(self.obstacle):
            x = np.random.randint(0, self.size)
            y = np.random.randint(0, self.size)
            z = np.random.randint(0, self.size)

            randObstacle=np.random.rand()
            lenObstacle=np.random.randint(self.size//2)
            HautObstacle=np.random.randint(self.size//2)
            if (randObstacle > 0.75):       
                for k in range(HautObstacle):
                    for i in range(lenObstacle-4, lenObstacle+4):
                        self.AddObstaclePoint(x+i, y+lenObstacle-i,z+k)
                        self.AddObstaclePoint(x+i, y+lenObstacle-i-1,z+k)
                        self.AddObstaclePoint(x+lenObstacle-i, y+i,z+k)
                        self.AddObstaclePoint(x+lenObstacle-i, y+i-1,z+k)
            elif (randObstacle > 0.5):
                for k in range(HautObstacle):
                    for i in range(lenObstacle-4, lenObstacle+4):
                        self.AddObstaclePoint(x+i, y+lenObstacle-i,z+k)
                        self.AddObstaclePoint(x+i, y+lenObstacle-i-1,z+k)
                        self.AddObstaclePoint(x+lenObstacle-i, y+i,z+k)
                        self.AddObstaclePoint(x+lenObstacle-i, y+i-1,z+k)
            elif (randObstacle > 0.25):
                for k in range(HautObstacle):
                    for l in range(lenObstacle):
                        self.AddObstaclePoint(x, y+l,z+k)
            else:
                for k in range(HautObstacle):
                    for l in range(lenObstacle):
                        self.AddObstaclePoint(x+l, y,z+k)

    def AddObstaclePoint(self,x,y,z):
        if not self.IsValidPoint(x, y, z):
            return 
        self.obstacle_point.append(Point(x, y,z))

    def IsObstacle(self, i ,j, k):
        for p in self.obstacle_point:
            if i==p.x and j==p.y and k==p.z:
                return True
        return False

    def IsValidPoint(self,x, y, z):
        if x < 0 or y < 0 or z < 0:
            return False
        if x >= self.size or y >= self.size or z >= self.size:
            return  False
        return True
