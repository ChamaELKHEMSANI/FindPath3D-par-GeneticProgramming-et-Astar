# d_star.py

"""
**Description :**  
Algorithme de recherche de chemin réactif, adapté aux environnements dynamiques.  

**Méthodes spécifiques :**  
- `initialize()`: Initialise les valeurs des nœuds.  
- `compute_shortest_path()`: Calcule le chemin le plus court en mettant à jour les coûts.  
- `reconstruct_path()`: Reconstruit le chemin optimal après exécution.  

"""

import sys
import heapq
import numpy as np

from point import *
from map_random import *
from map_draw import *


class DStar:
    def __init__(self, map, draw, start_point, end_point):
        self.map = map
        self.draw = draw
        self.start_point = start_point
        self.end_point = end_point
        self.open_set = []
        self.g_values = {}
        self.rhs_values = {}
        self.k_values = {}
        self.initialize()

    def heuristic(self, p):
        return np.sqrt((p.x - self.end_point.x)**2 + (p.y - self.end_point.y)**2 + (p.z - self.end_point.z)**2)

    def cost(self, p1, p2):
        return np.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)

    def initialize(self):
        self.g_values[self.end_point] = float('inf')
        self.rhs_values[self.end_point] = 0
        heapq.heappush(self.open_set, (self.heuristic(self.end_point), self.end_point))

    def get_neighbors(self, p):
        neighbors = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in [-1, 0, 1]:
                    if i == j == k == 0:
                        continue
                    new_x, new_y, new_z = p.x + i, p.y + j, p.z + k
                    if self.map.IsValidPoint(new_x, new_y, new_z) and not self.map.IsObstacle(new_x, new_y, new_z):
                        neighbors.append(Point(new_x, new_y, new_z))
        return neighbors

    def update_vertex(self, p):
        if p != self.end_point:
            self.rhs_values[p] = min(
                [self.g_values.get(n, float('inf')) + self.cost(p, n) for n in self.get_neighbors(p)],
                default=float('inf')
            )
        if (self.g_values.get(p, float('inf')) != self.rhs_values.get(p, float('inf'))):
            heapq.heappush(self.open_set, (self.get_key(p), p))

    def get_key(self, p):
        return (min(self.g_values.get(p, float('inf')), self.rhs_values.get(p, float('inf'))) + self.heuristic(p))

    def compute_shortest_path(self):
        while self.open_set and (self.g_values.get(self.start_point, float('inf')) != self.rhs_values.get(self.start_point, float('inf'))):
            _, p = heapq.heappop(self.open_set)
            if self.g_values.get(p, float('inf')) > self.rhs_values.get(p, float('inf')):
                self.g_values[p] = self.rhs_values[p]
            else:
                self.g_values[p] = float('inf')
                self.update_vertex(p)
            for neighbor in self.get_neighbors(p):
                self.update_vertex(neighbor)

    def run(self, App):
        self.compute_shortest_path()
        return self.reconstruct_path()

    def reconstruct_path(self):
        path = []
        p = self.start_point
        while p in self.g_values and p != self.end_point:
            path.append(p)
            p = min(self.get_neighbors(p), key=lambda n: self.g_values.get(n, float('inf')))
        path.append(self.end_point)
        for p in path:
            self.draw.drawCube(p, couleur='g')
        #self.draw.SaveImage()
        return True