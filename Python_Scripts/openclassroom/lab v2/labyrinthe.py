import os
import sys


class Labyrinthe:
    """
    Class regroupant les méthode utiles pour afficher et se depalcer dans le labyrinthe
    """
    def __init__(self, carte, nom):
        self.carte = carte                                # 2D array representant la carte
        self.nom = nom                                    # nom du level
        self.height = len(self.carte)                     # hauteur du lab
        self.width = len(self.carte[0])                   # largeur du lab
        self.out_position = self.get_out_position()       # tuple reprensentant la position (y,x) de la sortie
        self.robot_position = self.get_robot_position()   # tuple reprensentant la position (y,x) du robot

    def __repr__(self):
        return "Labyrinthe {}".format(self.nom)

    def render(self):
        """
        Affiche la grille du labyrinthe sous forme de string. Attention la position du personnage n'est pas
        présent sur la grille pour le pas effacer les porte si je passe dessus. Je l'ajoute lors de l'affichage
        uniquement (d'où le if).
        :return: None
        """
        print("\n"*10)
        y, x = self.robot_position
        for index, line in enumerate(self.carte):
            l = line[:]                            # creation d'une copie pour la modifier si besoin
            if index == y:                         # si on est sur la ligne ou est le perso
                l[x] = "X"                         # on ajoute X à la position du perso
            print("".join(l))

    def get_robot_position(self):
        """
        Scan la carte pour trouver la position y, x du robot (représenté par X). La position est retourné et ensuite on
        remplace sa représentation par un " " car il n'appartient pas a la carte (voir render() )
        :return: la position y, x du robot dans un tuple
        """
        for index, line in enumerate(self.carte):
            if "X" in line:
                pos = (index, line.index("X"))
                self.carte[index][line.index("X")] = " "
                return pos

    def get_out_position(self):
        """
        Scan la carte pour trouver la position y, x de la sortie (représenté par U).
        :return: la position y, x de la sortie dans un tuple
        """
        for index, line in enumerate(self.carte):
            if "U" in line:
                return (index, line.index("U"))

    def move(self, direction, step):
        """
        deplace le robot dans la direction de n step (sauf s'il y a un obstacle
        :param direction: N, S, E, O
        :param step: un entier reprensentant le nb de step a faire
        :return: un booleen indiquant si on a fini le niveau ou pas
        """
        for i in range(1, step + 1):
            y, x = self.robot_position
            if direction == "N" and y > 0:
                if self.carte[y - 1][x] in [" ", ".", "U"]:
                    self.robot_position = (y - 1, x)
            elif direction == "S" and y <= self.height:
                if self.carte[y + 1][x] in [" ", ".", "U"]:
                    self.robot_position = (y + 1, x)
            elif direction == "E" and x <= self.width+1:
                if self.carte[y][x + 1] in [" ", ".", "U"]:
                    self.robot_position = (y, x + 1)
            elif direction == "O" and x > 0:
                if self.carte[y][x - 1] in [" ", ".", "U"]:
                    self.robot_position = (y, x - 1)

            if self.robot_position == self.out_position:
                print("Bravo vous avez fini")
                return True

        return False