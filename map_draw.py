# map_draw.py

"""
**Description :**  
Gère l'affichage graphique 3D de la carte et des obstacles avec `matplotlib`.  

**Méthodes :**  
- `draw_map(map, pnt_src, pnt_dest)`: Affiche la carte avec obstacles, point de départ et destination.  
- `drawCube(p, couleur, alpha)`: Dessine un cube représentant un point dans l'espace 3D.  
- `SaveImage()`: Sauvegarde une image de la carte.  
- `rotate()`: Modifie l'angle de vue de la carte.  
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import numpy as np

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


from point import *
from map_random import *


class MapDraw(FigureCanvas):

    def __init__(self, parent ):
        self.fig, self.ax = plt.subplots(subplot_kw={'projection': '3d'})  # Création d'un axe 3D
        super().__init__(self.fig)
        self.setParent(parent)
        self.cptImg=0


    def draw_map(self,map,pnt_src,pnt_dest):
        self.ax.clear()

        self.ax.set_xlabel('x')
        self.ax.set_xlim(0, map.size)
        self.ax.set_xticklabels([])

        self.ax.set_ylabel('y')
        self.ax.set_ylim(0, map.size)
        self.ax.set_yticklabels([])


        self.ax.set_zlabel('z')
        self.ax.set_zlim(0, map.size)
        self.ax.set_zticks([])
        self.ax.set_zticklabels([])

        for p in map.obstacle_point:
            self.drawCube(p,couleur='black',alpha=0.9) 

        self.drawCube(pnt_src, couleur='b') 
        self.drawCube(pnt_dest, couleur='r') 
        self.draw()   

    def drawCube(self,p,couleur='black',alpha=0.9):
        points = np.array([
                        [p.x, p.y, p.z], [p.x+1, p.y, p.z], [p.x+1, p.y+1, p.z], [p.x, p.y+1, p.z],  # Face inférieure
                        [p.x, p.y, p.z+1], [p.x+1, p.y, p.z+1], [p.x+1, p.y+1, p.z+1], [p.x, p.y+1, p.z+1]   # Face supérieure
                        ])  
        faces = [
            [points[0], points[1], points[2], points[3]],  # Bas
            [points[4], points[5], points[6], points[7]],  # Haut
            [points[0], points[1], points[5], points[4]],  # Devant
            [points[2], points[3], points[7], points[6]],  # Derrière
            [points[1], points[2], points[6], points[5]],  # Droite
            [points[4], points[7], points[3], points[0]]   # Gauche
            ]
        self.ax.add_collection3d(Poly3DCollection(faces, facecolors=couleur, linewidths=1, edgecolors=couleur,alpha=alpha))


    def show(self):
        #self.ax.view_init(elev=20, azim=30)  # Angle de vue initial
        self.draw()   

    def SaveImage(self):
        plt.draw()
        self.cptImg+=1
        filename = './images/' + str(self.cptImg) + '.png'
        plt.savefig(filename)
 
    def rotate(self):
        """Fait tourner la vue du cube."""
        self.ax.view_init(elev=20, azim=(self.ax.azim + 30) % 360)
        self.draw()
