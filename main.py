import sys
import time
import numpy as np
from PyQt5.QtCore import QCoreApplication,    Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout,QHBoxLayout, QWidget,QComboBox, QPushButton,QLineEdit, QLabel
from point import *
from map_random import *
from engines.a_star import *
from engines.d_star import *
from engines.ara_star import *
from engines.genetic_program import *
from map_draw import *



class FindPath3DApp(QMainWindow):
    """Application principale PyQt5."""
    def __init__(self):
        super().__init__()
        self.blRun=False
        self.engines=["GeneticProgram","A-star","D-DStar","ARA-Star"]

        self.setWindowTitle("Trouver un chemin")
        self.setGeometry(100, 100, 800, 600)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
       
        # Ajouter le widget Matplotlib
        self.canvas = MapDraw(self)
        layout.addWidget(self.canvas)

        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Moteur:"))
        self.comboEngine = QComboBox()
        for strItem in self.engines:
            self.comboEngine.addItem(strItem,strItem)
        self.comboEngine.setCurrentIndex(self.comboEngine.findData("GeneticProgram"))
        input_layout.addWidget(self.comboEngine)
        self.size_input = QLineEdit("10")
        self.size_input.setPlaceholderText("Taille (10 - 50)")
        input_layout.addWidget(QLabel("Taille:"))
        input_layout.addWidget(self.size_input)
        self.obstacle_input = QLineEdit("10")
        self.obstacle_input.setPlaceholderText("Obstacle (5-100)")
        input_layout.addWidget(QLabel("Obstacle:"))
        input_layout.addWidget(self.obstacle_input)  

        layout.addLayout(input_layout)

        button_layout = QHBoxLayout()
        self.button = QPushButton("Executer") 
        self.button.clicked.connect(lambda: self.RunIt())
        button_layout.addWidget(self.button)
        self.button = QPushButton("Stop")
        self.button.clicked.connect(lambda: self.StopIt())
        button_layout.addWidget(self.button)
        self.button = QPushButton("Quitter")
        self.button.clicked.connect(lambda: self.endIt())
        button_layout.addWidget(self.button)
        layout.addLayout(button_layout)

    def  showIt(self):
        self.canvas.show()
        QCoreApplication.processEvents() 

    def StopIt(self):
        self.blRun=False

    def  endIt(self):
        self.blRun=False
        QCoreApplication.processEvents() 
        sys.exit(0)

    def RunIt(self):
        if self.blRun==True:
            return
        map_taille=int(self.size_input.text()) 
        map_obstacle=int(self.obstacle_input.text()) 
        engineIndx=self.comboEngine.currentIndex()
        self.blRun=True
        self.pnt_src=Point(0,0,0,0)
        self.pnt_dest=Point(map_taille-1,map_taille-1,map_taille-1)
        self.map = MapRandom(map_taille,map_obstacle)
        self.canvas.draw_map(self.map,self.pnt_src,self.pnt_dest)
        QCoreApplication.processEvents() 

        if engineIndx==0:
            engine = GeneticProgram(self.map,self.canvas,self.pnt_src,self.pnt_dest,population_size=10, generations=50, mutation_rate=0.5) 
        elif engineIndx==1:
            engine = AStar(self.map,self.canvas,self.pnt_src,self.pnt_dest)
        elif engineIndx==2:
           engine = DStar(self.map,self.canvas,self.pnt_src,self.pnt_dest)            
        else:
           engine = ARAStar(self.map,self.canvas,self.pnt_src,self.pnt_dest)

        start_time = time.time()
        if engine.run(self):
            end_time = time.time()
            print('\n ===== fin Algorithm ', int(end_time-start_time), ' seconds')

        self.canvas.show()
        self.blRun=False

#------------------------------------------------------------
# Exécuter l'application PyQt5
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FindPath3DApp()
    window.show()
    sys.exit(app.exec_())
