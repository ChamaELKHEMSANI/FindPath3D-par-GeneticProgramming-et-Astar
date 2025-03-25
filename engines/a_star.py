# a_star.py

"""
**Description :**  
Implémente l'algorithme A* pour trouver un chemin optimal dans la carte.  

**Attributs :**  
- `map`, `draw` : Références à la carte et au module de dessin.  
- `open_set`, `close_set` : Listes des points ouverts et fermés.  
- `start_point`, `end_point` : Points de départ et d'arrivée.  

**Méthodes :**  
- `BaseCost(p)`, `HeuristicCost(p)`, `TotalCost(p)`: Fonctions de coût pour A*.  
- `IsValidPoint(x, y, z)`: Vérifie si un point est valide.  
- `ProcessPoint(x, y, z, parent)`: Ajoute un point à l’open list si valide.  
- `BuildPath(p)`: Construit le chemin optimal.  
- `run(App)`: Exécute l'algorithme A*.  

"""

import sys
import numpy as np

from point import *
from map_random import *
from map_draw import *

class AStar:
    def __init__(self, map,draw,start_point,end_point):
        self.map=map
        self.draw=draw
        self.open_set = []
        self.close_set = []
        self.start_point = start_point
        self.end_point = end_point

    def BaseCost(self, p):
        x_dis = p.x
        y_dis = p.y
        z_dis = p.z
        return x_dis + y_dis +  z_dis +(np.sqrt(3) - 3) * min(x_dis, y_dis,z_dis)

    def HeuristicCost(self, p):
        x_dis = self.map.size - 1 - p.x
        y_dis = self.map.size - 1 - p.y
        z_dis = self.map.size - 1 - p.z
        return x_dis + y_dis + z_dis + (np.sqrt(3) - 3) * min(x_dis, y_dis,z_dis)

    def TotalCost(self, p):
        return self.BaseCost(p) + self.HeuristicCost(p)

    def IsValidPoint(self, x, y, z):
        if x < 0 or y < 0 or z < 0:
            return False
        if x >= self.map.size or y >= self.map.size or z >= self.map.size:
            return False
        return not self.map.IsObstacle(x, y, z)

    def IsInPointList(self, p, point_list):
        for point in point_list:
            if point.isEgale(p):
                return True
        return False

    def IsInOpenList(self, p):
        return self.IsInPointList(p, self.open_set)

    def IsInCloseList(self, p):
        return self.IsInPointList(p, self.close_set)

    def IsStartPoint(self, p):
        return p.isEgale(self.start_point)

    def IsEndPoint(self, p):
        return p.isEgale(self.end_point)

    def ProcessPoint(self, x, y, z, parent):
        if not self.IsValidPoint(x, y,z):
            return  
        p = Point(x, y,z)
        if self.IsInCloseList(p):
            return  
        if not self.IsInOpenList(p):
            p.parent = parent
            p.cost = self.TotalCost(p)
            self.open_set.append(p)

    def SelectPointInOpenList(self):
        index = 0
        selected_index = -1
        min_cost = sys.maxsize
        for p in self.open_set:
            cost = self.TotalCost(p)
            if cost < min_cost:
                min_cost = cost
                selected_index = index
            index += 1
        return selected_index

    def BuildPath(self, p):
        path = []
        while True:
            path.insert(0, p) 
            if self.IsStartPoint(p):
                break
            else:
                p = p.parent
        for p in path:
            if not self.IsStartPoint(p)  and not self.IsEndPoint(p) :
                self.draw.drawCube(p,couleur='g')
        self.draw.SaveImage()
        return True

    def run(self,App):

        self.open_set.append(self.start_point)

        while True:
            index = self.SelectPointInOpenList()
            if index < 0:
                print('Aucun chemin trouvé, echec algorithm !!!')
                return False
            p = self.open_set[index]
            self.draw.drawCube(p,couleur='c',alpha=0.1)
            #self.draw.SaveImage()
            App.showIt()
            if App.blRun==False: #stop
                return False
            print(".",end='',flush=True)
            if self.IsEndPoint(p):
                return self.BuildPath(p)

            del self.open_set[index]
            self.close_set.append(p)

            # Process voisins
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    for k in [-1,0,1]:
                        if App.blRun==False: #stop
                            return False
                        if (i==0 and j==0 and k==0):
                            pass
                        else:
                            self.ProcessPoint(p.x+i, p.y+j, p.z+k, p)
        return False
