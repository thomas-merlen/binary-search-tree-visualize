import tkinter as tk
from tkinter import Frame, Label, Entry, Button
from binary_search_tree import * 

class VisualizerEditTab:
    def __init__(self, visualizer, x, y):
        # Initialise l'onglet de l'éditeur avec les éléments nécessaires
        self.visualizer = visualizer
        self.frame = Frame(self.visualizer.window, width=220, height=100, bd=1, relief=tk.SOLID)
        self.frame.place(x=x, y=y)

        self.add_label = Label(self.frame, text="Ajouter valeur :", bg="lightgrey")
        self.add_label.place(x=10, y=15)

        self.add_entry = Entry(self.frame, width=6) # Champ de saisie pour entrer la valeur à ajouter
        self.add_entry.place(x=110, y=15)

        self.add_button = Button(self.frame, text="OK", command=self.on_add)
        self.add_button.place(x=170, y=15)

        self.del_label = Label(self.frame, text="Enlever valeur :", bg="lightgrey")
        self.del_label.place(x=10, y=60)

        self.del_entry = Entry(self.frame, width=6) # Champ de saisie pour entrer la valeur à supprimer
        self.del_entry.place(x=110, y=60)

        self.del_button = Button(self.frame, text="OK", command=self.on_del)
        self.del_button.place(x=170, y=60)

    def on_add(self):
        # Méthode appelée lors du clic sur le bouton d'ajout
        valeur = int(self.add_entry.get())
        if self.visualizer.tree.insert(valeur):
            self.visualizer.update()
        self.add_entry.delete(0, tk.END)

    def on_del(self):
        # Méthode appelée lors du clic sur le bouton de suppression
        valeur = int(self.del_entry.get())
        self.visualizer.tree.remove(valeur) 
        self.visualizer.update()
        self.del_entry.delete(0, tk.END)


class VisualizerInfoTab:
    def __init__(self, visualizer, x, y):
        # Initialise l'onglet d'informations avec les éléments nécessaires
        self.visualizer = visualizer
        self.frame = Frame(self.visualizer.window, width=200, height=100, bd=1, relief=tk.SOLID)
        self.frame.place(x=x, y=y)

        self.size_label = Label(self.frame, text="Taille de l'arbre : ")
        self.size_label.place(x=10, y=5)
     
        self.depth_label = Label(self.frame, text="Profondeur de l'arbre : ")
        self.depth_label.place(x=10, y=35)

        self.leaf_label = Label(self.frame, text="Nombres de feuilles : ")
        self.leaf_label.place(x=10, y=65)

    def update(self):
        # Met à jour les labels d'informations avec les valeurs actuelles de l'arbre
        size = self.visualizer.tree.size()
        depth = self.visualizer.tree.depth()
        leaves = self.visualizer.tree.leaves()

        self.size_label.config(text="Taille de l'arbre : " + str(size))
        self.depth_label.config(text="Profondeur de l'arbre : " + str(depth))
        self.leaf_label.config(text="Nombres de feuilles : " + str(leaves))

class VisualizerCommandTab:
    def __init__(self, visualizer, x, y):
        # Initialise l'onglet des commandes avec les éléments nécessaires
        self.visualizer = visualizer
        self.frame = Frame(self.visualizer.window, width=764, height=80, bd=1, relief=tk.SOLID)
        self.frame.place(x=x, y=y)

        # Boutons pour exécuter les différentes commandes
        self.bouton_nouveau = Button(self.frame, text="Nouveau", command=self.nouveau)
        self.bouton_nouveau.place(x=10, y=10)

        self.bouton_largeur = Button(self.frame, text="Largeur", command=self.largeur)
        self.bouton_largeur.place(x=120, y=10)

        self.bouton_prefixe = Button(self.frame, text="Préfixe", command=self.prefixe)
        self.bouton_prefixe.place(x=230, y=10)

        self.bouton_infixe = Button(self.frame, text="Infixe", command=self.infixe)
        self.bouton_infixe.place(x=330, y=10)

        self.bouton_postfixe = Button(self.frame, text="Postfixe", command=self.postfixe) 
        self.bouton_postfixe.place(x=440, y=10)

        self.bouton_exporter = Button(self.frame, text="Exporter", command=self.exporter) 
        self.bouton_exporter.place(x=550, y=10)

        self.bouton_reduire = Button(self.frame, text="Réduire", command=self.reduire)
        self.bouton_reduire.place(x=660, y=10)

        # Champ de saisie pour afficher les résultats des commandes
        self.output_entry = Entry(self.frame, width=92)
        self.output_entry.place(x=10, y=50)

    # Méthodes pour chaque commande
    def nouveau(self):
        self.visualizer.tree = BinarySearchTree()
        self.visualizer.update()

    def infixe(self):
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, self.visualizer.tree.infix())

    def prefixe(self):
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, self.visualizer.tree.prefix())

    def postfixe(self):
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, self.visualizer.tree.postfix())

    def largeur(self):
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, self.visualizer.tree.breadth())

    def exporter(self):
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, self.visualizer.tree.export())

    def reduire(self):
        self.visualizer.tree.reduce()
        self.visualizer.update()
