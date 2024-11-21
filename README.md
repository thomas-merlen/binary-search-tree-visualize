# Binary Search Tree Visualizer 🌳

**Binary Search Tree Visualizer** est une application interactive, développée avec Python et Tkinter, permettant de manipuler et de visualiser des arbres binaires de recherche (BST). Ce projet combine des fonctionnalités pratiques pour l'apprentissage des structures de données et des algorithmes de manipulation d'arbres binaires.

## Fonctionnalités principales 🚀

- **Visualisation dynamique** : Ajoutez ou supprimez des valeurs pour observer l'évolution de la structure de l'arbre.
- **Informations détaillées** : Consultez la taille, la profondeur et le nombre de feuilles de l'arbre.
- **Parcours d'arbres** : Affichez les résultats des parcours infixe, préfixe, postfixe et en largeur.
- **Exportation** : Exportez l'arbre sous forme de triplets pour une représentation textuelle.
- **Réduction** : Réorganisez l'arbre pour minimiser sa hauteur.

## Structure des fichiers 📂

- **`binary_search_tree_visualizer.py`**  
  Gère l'interface utilisateur avec Tkinter. Ce fichier inclut la gestion des onglets pour les actions (ajout/suppression), les commandes (parcours/exportation/réduction) et les statistiques sur l'arbre.
  
- **`binary_search_tree.py`**  
  Implémente les opérations fondamentales sur les arbres binaires de recherche, notamment :  
  - Insertion, suppression, et recherche.  
  - Calcul de la taille, de la profondeur et des feuilles.  
  - Parcours (infixe, préfixe, postfixe, largeur).  
  - Réduction et exportation.

- **`visualizer_tabs.py`**  
  Contient les classes pour les onglets de l'interface utilisateur :  
  - **Onglet de modification** : Ajouter ou supprimer des valeurs.  
  - **Onglet d'information** : Afficher des statistiques sur l'arbre.  
  - **Onglet de commandes** : Exécuter des parcours et exporter l'arbre.
