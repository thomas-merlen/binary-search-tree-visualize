class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def insert(self, valeur, depth=1):
        # Vérifie si la valeur est dans la plage autorisée et si la profondeur est inférieure ou égale à 6
        if not (0 <= valeur <= 999):
            return False
        if depth > 6:
            return False

        # Si l'arbre est vide, insère la valeur à la racine
        if self.root == None:
            self.root = valeur
            self.left = BinarySearchTree()  # Crée un sous-arbre gauche vide
            self.right = BinarySearchTree()  # Crée un sous-arbre droit vide
            return True

        # Si la valeur est inférieure à la valeur de la racine, insère dans le sous-arbre gauche
        elif valeur < self.root:
            if self.left == None:
                self.left = BinarySearchTree()
            return self.left.insert(valeur, depth + 1)

        # Si la valeur est supérieure à la valeur de la racine, insère dans le sous-arbre droit
        elif valeur > self.root:
            if self.right == None:
                self.right = BinarySearchTree()
            return self.right.insert(valeur, depth + 1)

        else:
            return False


    def remove(self, value):
        # Si l'arbre est vide, ne rien faire
        if self.root == None:
            return

        if value == self.root:
            # Cas où la valeur à supprimer est trouvée à la racine
            if self.left.root == None:
                return self.right
            elif self.right.root == None:
                return self.left
            else:
                # Trouver la plus petite valeur dans le sous-arbre droit pour remplacer la racine
                min_val = self.right.minimum()
                self.root = min_val
                self.right = self.right.remove(min_val)

        elif value < self.root:
            # Si la valeur à supprimer est inférieure à la racine, supprimer du sous-arbre gauche
            self.left = self.left.remove(value)
        
        else:
            # Si la valeur à supprimer est supérieure à la racine, supprimer du sous-arbre droit
            self.right = self.right.remove(value)

        return self

    def minimum(self):
        # Trouve et renvoie la plus petite valeur dans l'arbre
        if self.left.root == None:
            return self.root
        return self.left.minimum()

    def size(self):
        # Calcule et renvoie la taille de l'arbre
        if self.root == None:
            return 0
        left_size = self.left.size() if self.left else 0
        right_size = self.right.size() if self.right else 0
        return 1 + left_size + right_size


    def depth(self):
        # Calcule et renvoie la profondeur de l'arbre
        if self.root == None:
            return 0
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return 1 + max(left_depth, right_depth)


    def leaves(self):
        # Calcule et renvoie le nombre de feuilles dans l'arbre
        if self.root == None:
            return 0
        left_leaves = self.left.leaves() if self.left else 0
        right_leaves = self.right.leaves() if self.right else 0
        # Vérification si le nœud actuel est une feuille
        if left_leaves == 0 and right_leaves == 0:
            return 1
        return left_leaves + right_leaves




    def infix(self):
        # Parcours l'arbre en ordre infixe 
        if self.root == None:
            return ""
        return self.left.infix() + str(self.root) + ", " + self.right.infix()

    def prefix(self):
        # Parcours l'arbre en préfixe
        if self.root == None:
            return ""
        return str(self.root) + ", " + self.left.prefix() + self.right.prefix()

    def postfix(self):
        # Parcours l'arbre en postfixe 
        if self.root == None:
            return ""
        return self.left.postfix() + self.right.postfix() + str(self.root) + ", "

    def breadth(self):
        # Parcours l'arbre en largeur
        noeud = [self]
        result = ""
        while noeud:
            current = noeud.pop(0)
            if current.root != None:
                result += str(current.root) + ", "
                noeud.append(current.left)
                noeud.append(current.right)
        return result

    def export(self):
        # Exporte l'arbre sous forme de triplets
        if self.root == None:
            return "()"
        return "(" + str(self.root) + ", " + self.left.export() + ", " + self.right.export() + ")"

    def get_sorted_values(self):
        # Renvoie les valeurs de l'arbre triées dans l'ordre croissant
        return list(self.infix().split(", "))[:-1]  # On utilise la méthode infix pour obtenir les valeurs triées

    def build_reduced_tree(self, values):
        # Construit un arbre de profondeur minimale à partir d'une liste triée de valeurs
        if not values:
            return None
        milieu = len(values) // 2
        self.root = int(values[milieu])
        self.left = BinarySearchTree()
        self.right = BinarySearchTree()
        self.left.build_reduced_tree(values[:milieu])
        self.right.build_reduced_tree(values[milieu+1:])

    def reduce(self):
        # Réduit la hauteur de l'arbre tout en conservant les valeurs
        values = self.get_sorted_values()
        self.root = None
        self.left = None
        self.right = None
        self.build_reduced_tree(values)

