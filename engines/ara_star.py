# ara_star.py

"""
**Description :**  
Version adaptative de A* qui ajuste dynamiquement son heuristique.  

**Méthodes spécifiques :**  
- `heuristic(p)`: Calcule une heuristique basée sur la distance euclidienne.  
- `initialize()`: Initialise les valeurs `g` et `rhs`.  
- `compute_or_improve_path()`: Calcule un chemin optimal en plusieurs passes.  

 

"""

import sys
import numpy as np
import heapq

from point import *
from map_random import *
from map_draw import *




class ARAStar:
    def __init__(self, map, draw, start_point, end_point, epsilon=2.5, epsilon_decay=0.9):
        self.map = map
        self.draw = draw
        self.start_point = start_point
        self.end_point = end_point
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.open_set = []
        self.inconsistent_set = []
        self.close_set = set()
        self.g_values = {}
        self.rhs_values = {}

    def heuristic(self, p):
        return np.sqrt((p.x - self.end_point.x)**2 + (p.y - self.end_point.y)**2 + (p.z - self.end_point.z)**2)

    def cost(self, p1, p2):
        return np.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)

    def initialize(self):
        self.g_values = {self.start_point: float('inf')}
        self.rhs_values = {self.start_point: 0}
        heapq.heappush(self.open_set, (self.get_key(self.start_point), self.start_point))

    def get_key(self, p):
        g = self.g_values.get(p, float('inf'))
        rhs = self.rhs_values.get(p, float('inf'))
        return (min(g, rhs) + self.epsilon * self.heuristic(p), min(g, rhs))

    def update_vertex(self, p):
        if p != self.start_point:
            self.rhs_values[p] = min(
                [self.g_values.get(n, float('inf')) + self.cost(p, n) for n in self.get_neighbors(p)],
                default=float('inf')
            )
        if p in self.open_set:
            self.open_set.remove((self.get_key(p), p))
        if self.g_values.get(p, float('inf')) != self.rhs_values.get(p, float('inf')):
            heapq.heappush(self.open_set, (self.get_key(p), p))

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

    def compute_or_improve_path(self):
        while self.open_set and (self.get_key(self.open_set[0][1]) < self.get_key(self.end_point) or self.rhs_values[self.end_point] > self.g_values.get(self.end_point, float('inf'))):
            _, p = heapq.heappop(self.open_set)
            self.close_set.add(p)
            if self.g_values.get(p, float('inf')) > self.rhs_values[p]:
                self.g_values[p] = self.rhs_values[p]
                for neighbor in self.get_neighbors(p):
                    self.update_vertex(neighbor)
            else:
                self.g_values[p] = float('inf')
                self.update_vertex(p)
                for neighbor in self.get_neighbors(p):
                    self.update_vertex(neighbor)

    def run(self, App):
        self.initialize()
        self.compute_or_improve_path()
        while self.epsilon > 1:
            self.epsilon *= self.epsilon_decay
            self.compute_or_improve_path()
        return self.reconstruct_path()

    def reconstruct_path(self):
        path = []
        p = self.end_point
        while p in self.g_values and p != self.start_point:
            path.append(p)
            p = min(self.get_neighbors(p), key=lambda n: self.g_values.get(n, float('inf')))
        path.reverse()
        for p in path:
            self.draw.drawCube(p, couleur='g')
        #self.draw.SaveImage()
        return True
