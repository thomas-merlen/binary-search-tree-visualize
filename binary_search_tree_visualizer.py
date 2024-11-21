from tkinter import *  # Importation de toutes les classes et fonctions de tkinter
from visualizer_tabs import *  # Importation des classes définies dans visualizer_tabs.py

class BinarySearchTreeVisualizer:
    def __init__(self):

        # Initialisation de la fenêtre Tkinter
        self.window = Tk()
        self.window.title("Binary Search Tree Visualizer par ROTAR Daniel & MERLEN Thomas")  # Titre de la fenêtre
        self.window.geometry("800x600")  # Dimensions de la fenêtre
        self.window.resizable(0, 0)  # Empêche le redimensionnement de la fenêtre
        self.window.config(bg="white")  # Couleur de fond de la fenêtre

        # Initialisation du Canvas pour afficher l'arbre
        self.canvas = Canvas(self.window, bg="white", width=800, height=400, highlightthickness=0)
        self.canvas.place(x=0, y=120) 

        # Initialisation des onglets de l'interface
        self.edit_tab = VisualizerEditTab(self, 20, 5)  # Onglet de modification
        self.info_tab = VisualizerInfoTab(self, 580, 5)  # Onglet d'informations
        self.command_tab = VisualizerCommandTab(self, 18, 510)  # Onglet de commande

        # Initialisation de l'arbre binaire de recherche
        self.tree = BinarySearchTree()

        # Lancement de la boucle principale de la fenêtre
        self.window.mainloop()

    # Méthode pour dessiner l'arbre
    def draw(self, tree, x, y, depth=1):
        if tree.root != None:
            rayon = 11  # Rayon des noeuds
            x_decalement = 6 * (2 ** (6 - depth))  # Décalage horizontal
            y_decalement = 70  # Décalage vertical

            # Dessin du noeud
            self.canvas.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, outline="black", fill="white")
            self.canvas.create_text(x, y, text=str(tree.root))

            # Coordonnées du point de départ des branches
            x_bas = x
            y_bas = y + rayon

            # Dessin des branches
            if tree.left != None and tree.left.root != None:
                self.canvas.create_line(x_bas, y_bas, x - x_decalement, y + y_decalement)
                self.draw(tree.left, x - x_decalement, y + y_decalement, depth + 1)
            if tree.right != None and tree.right.root != None:
                self.canvas.create_line(x_bas, y_bas, x + x_decalement, y + y_decalement)
                self.draw(tree.right, x + x_decalement, y + y_decalement, depth + 1)


    # Méthode pour mettre à jour l'affichage de l'arbre et des onglets
    def update(self):
        self.canvas.delete("all")  # Effacement du contenu du canevas
        self.info_tab.update()  # Mise à jour des informations affichées
        self.draw(self.tree, 400, 15)  # Redessin de l'arbre avec les modifications

# Création d'une instance de la classe BinarySearchTreeVisualizer pour lancer l'application
BinarySearchTreeVisualizer()
