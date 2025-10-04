# 3D Pathfinding Visualizer

Une application interactive de recherche de chemin en 3D implémentant plusieurs algorithmes d'IA avec une interface graphique PyQt5.


## 📋 Description

Ce projet permet de visualiser et comparer différents algorithmes de recherche de chemin dans un environnement 3D avec obstacles. L'application génère aléatoirement une carte 3D et trouve un chemin optimal entre un point de départ et une destination en utilisant l'algorithme sélectionné.

## 🚀 Fonctionnalités

- **Environnement 3D interactif** avec génération aléatoire d'obstacles
- **Multiples algorithmes** implémentés :
  - **A*** - Algorithme de recherche heuristique classique
  - **D*** - Algorithme adaptatif pour environnements dynamiques
  - **ARA*** - A* avec décroissance adaptative de l'heuristique
  - **Programmation Génétique** - Approche évolutive pour la recherche de chemin
- **Visualisation en temps réel** de l'exploration et du chemin final
- **Interface utilisateur intuitive** avec contrôles pour paramétrer la simulation
- **Export d'images** des résultats

## 🛠️ Installation

### Prérequis

- Python 3.7+
- PyQt5
- Matplotlib
- NumPy

### Installation des dépendances

```bash
pip install PyQt5 matplotlib numpy


🎮 Utilisation
1-Lancez l'application :
python main.py

2-Configurez les paramètres :
Moteur : Sélectionnez l'algorithme à utiliser
Taille : Dimension de la grille 3D (10-50)
Obstacle : Pourcentage d'obstacles (5-100)

3-Cliquez sur "Executer" pour lancer la simulation

4-Visualisez en temps réel l'exploration de l'espace et le chemin trouvé

📁 Structure du projet
3d-pathfinding/
├── main.py                # Application principale PyQt5
├── point.py               # Classe Point pour la gestion des coordonnées 3D
├── map_random.py          # Génération aléatoire de cartes 3D avec obstacles
├── map_draw.py            # Visualisation 3D avec Matplotlib
├── engines/
│   ├── a_star.py          # Implémentation de l'algorithme A*
│   ├── d_star.py          # Implémentation de l'algorithme D*
│   ├── ara_star.py        # Implémentation de l'algorithme ARA*
│   └── genetic_program.py # Algorithme génétique pour la recherche de chemin
└── images/                # Dossier pour sauvegarder les captures d'écran

🔧 Algorithmes implémentés

A* (A-Star)
Type : Recherche heuristique

Avantages : Optimal et complet

Utilisation : Environnements statiques

D* (D-Star)
Type : Algorithme incrémental

Avantages : Adapté aux environnements dynamiques

Utilisation : Replanification efficace

ARA* (Anytime Repairing A*)
Type : Algorithme anytime

Avantages : Solution rapide améliorable dans le temps

Utilisation : Contraintes de temps réel

Programmation Génétique
Type : Algorithme évolutionniste
Avantages : Exploration large de l'espace de recherche
Utilisation : Problèmes complexes avec multiples solutions

🎯 Exemples d'utilisation
Recherche de chemin basique
# Génération d'une carte 10x10x10 avec 10% d'obstacles
map = MapRandom(10, 10)
start = Point(0, 0, 0)
end = Point(9, 9, 9)

# Utilisation de A*
engine = AStar(map, canvas, start, end)
path = engine.run()

Comparaison d'algorithmes
L'application permet de comparer visuellement les performances et stratégies des différents algorithmes sur la même carte.

📊 Résultats et visualisation
Points bleus : Point de départ
Points rouges : Point d'arrivée
Cubes noirs : Obstacles
Points verts : Chemin final trouvé
Points cyan : Zones explorées pendant la recherche

🤝 Contribution
Les contributions sont les bienvenues ! N'hésitez pas à :

Signaler des bugs
Proposer de nouvelles fonctionnalités
Améliorer la documentation
Ajouter de nouveaux algorithmes

📄 Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

👨‍💻 Auteurs
Développé dans le cadre d'un projet de visualisation d'algorithmes de recherche de chemin en 3D.

Note : Pour de meilleures performances, il est recommandé d'utiliser des tailles de grille inférieures à 20 pour les algorithmes génétiques.



Ce README fournit une documentation complète avec :
- Une description claire du projet
- Des instructions d'installation et d'utilisation
- La structure des fichiers
- La documentation des algorithmes
- Des exemples d'utilisation
- Des informations sur la visualisation
