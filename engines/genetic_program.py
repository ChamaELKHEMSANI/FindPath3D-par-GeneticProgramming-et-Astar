# genetic_program.py
"""
**Description :**  
Implémente un algorithme génétique pour trouver un chemin dans la carte.  

**Méthodes spécifiques :**  
- `generate_random_path()`: Génère un chemin aléatoire.  
- `fitness(path)`: Évalue la qualité d’un chemin.  
- `crossover(parent1, parent2)`: Combine deux chemins pour créer une nouvelle solution.  
- `run(App)`: Exécute l’algorithme génétique jusqu’à convergence.  

"""


import sys
import heapq
import numpy as np

from point import *
from map_random import *
from map_draw import *

class GeneticProgram:
    def __init__(self, map, draw, start_point, end_point, population_size=10, generations=50, mutation_rate=0.1):
        self.map = map
        self.draw = draw
        self.start_point = start_point
        self.end_point = end_point
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.population = []

    def generate_random_path(self):
        path = [self.start_point]
        current = self.start_point
        while not self.is_end_point(current):
            next_moves = self.get_valid_moves(path,current)
            if not next_moves:
                break  # Pas de mouvement possible
            if len(next_moves)==1:
                current = next_moves[0]
            else:
                current = next_moves[random.choice([0,1])]
            path.append(current)
        self.print_path(path)
        return path

    def print_path(self,path):
        strval="\n["
        for p in path:
            strval+='('+str(p.x)+','+str(p.y)+','+str(p.z)+'),'
        strval+="]\n"
        print(strval)

    def IsInpath(self,path,x, y, z):
        for p in path:
            if p.isEgaleCoord(x, y, z):
                return True
        return False

    def get_valid_moves(self,path, point):
        moves = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in [-1, 0, 1]:
                    if i == j == k == 0:
                        continue
                    new_x, new_y, new_z = point.x + i, point.y + j, point.z + k
                    if not self.IsInpath(path,new_x, new_y, new_z) and self.map.IsValidPoint(new_x, new_y, new_z) and not self.map.IsObstacle(new_x, new_y, new_z):
                        moves.append(Point(new_x, new_y, new_z))
        if len(moves)>0:
            moves.sort(key=self.distance)
        return moves

    def distance(self, pnt):
        return pnt.distance(self.end_point)

    def fitness(self, path):
        if not path:
            return float('inf')
        last_point = path[-1]
        distance = last_point.distance(self.end_point)   
        return distance + len(path)  # Favoriser les chemins courts

    def select_best(self):
        self.population.sort(key=self.fitness)
        return self.population[:self.population_size // 2]

    def crossover(self, parent1, parent2):
        min_length = min(len(parent1), len(parent2))
        crossover_point = random.randint(1, min_length - 1)
        return parent1[:crossover_point] + parent2[crossover_point:]

    def mutate(self, path):
        if random.random() < self.mutation_rate:
            index = random.randint(1, len(path) - 2)
            valid_moves = self.get_valid_moves(path,path[index])
            if valid_moves:
                path[index] = random.choice(valid_moves)
        return path

    def run(self, App):
        print('\n ===== Debut Generation population')
        self.population=[]
        for i in range(self.population_size):
            print(i)
            if App.blRun==False: #stop
                return False
            self.population.append(self.generate_random_path() )
        print('\n ===== Fin Generation population')
        for _ in range(self.generations):
            print(".",end='',flush=True)
            if App.blRun==False: #stop
                return False

            self.population = self.select_best()
            new_population = []
            while len(new_population) < self.population_size:
                if App.blRun==False: #stop
                    return False
                p1, p2 = random.sample(self.population, 2)
                child = self.crossover(p1, p2)
                #child = self.mutate(child)
                new_population.append(child)
            self.population = new_population
            if self.fitness(self.population[0]) == 0:
                break
        best_path = self.population[0]
        for p in best_path:
            if not self.is_start_point(p) and not self.is_end_point(p):
                self.draw.drawCube(p, couleur='g')
        self.print_path(best_path)
        return True

    def is_end_point(self, p):
        return p.x == self.end_point.x and p.y == self.end_point.y and p.z == self.end_point.z

    def is_start_point(self, p):
        return p.x == self.start_point.x and p.y == self.start_point.y and p.z == self.start_point.z

