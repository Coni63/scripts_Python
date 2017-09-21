import os
import sys
import pickle


class Map:
    def __init__(self, carte, nom):
        self.carte = carte
        self.nom = nom
        self.get_robot_position()
        self.get_out_position()

    def render(self):
        for each in self.carte:
            print("".join(each))

    def __repr__(self):
        "{}".format(self.nom)

    def get_robot_position(self):
        for index, line in enumerate(self.carte):
            if "X" in line:
                return (index, line.index("X"))

    def get_out_position(self):
        for index, line in enumerate(self.carte):
            if "U" in line:
                return (index, line.index("U"))


class Robot:
    def __init__(self, carte):
        self.carte = carte
        self.x = 0
        self.y = 0
        #self.set_position()

    def set_position(self):
        pass
        #for i in range(len(carte)):


def is_valid(x, type_="int", choix=None):
    """
    :param x: L'entrée que vous voulez tester (int ou str)
    :param type_: Le type de donnée voulue (int ou str)
    :param choix: Une liste de choix que vous voulez imposer
    :return: Un booleen précisant si l'entrée est valide ou pas
    """
    if choix is None:
        if type_ == "int":
            return x.isnumeric()
        elif type_ == "":
            return True
    else:
        if type_ == "int" and x.isnumeric():
            return (int(x) in choix)
        else:
            return (x in choix)

def select_level(url_map = "./map/"):
    # print("Selectionnez le level :")

    try:
        list_level = [f for f in os.listdir(url_map) if os.path.isfile(os.path.join(url_map, f))]
    except FileNotFoundError:
        print("Dossier non trouvé. Fermeture")
        sys.exit(0)

    if len(list_level) == 0:
        print("Aucun niveau trouvé. Fermeture")
        sys.exit(0)
    #
    # for index, level in enumerate(list_level):
    #     print("[{}] : {}".format(index, level[:-4]))
    #
    # choix = input("Quel level souhaitez vous faire ?")
    # while not is_valid(choix, type_="int", choix=list(range(len(list_level)))):
    #     choix = input("Mauvaise entrée! Quel level souhaitez vous faire ?")

    choix = "1"

    choix = int(choix)
    file_url = os.path.join(url_map, list_level[choix])
    niveau = []
    with open(file_url, "r") as f:
        for line in f:
            niveau.append(list(line[:-2]))

    niveau = Map(niveau, list_level[choix])
    save(niveau)
    return niveau

def load_save(url_save = "./save/"):
    save_url = os.path.join(url_save, "save.pickle")
    if os.path.isfile(save_url):
        choix = input("Une sauvegarde a été trouvée, voulez-vous la continuer ? (Y/N)")
        while not is_valid(choix, type_="str", choix=["Y", "N"]):
            choix = input("Mauvaise entrée! Voulez-vous continuer la partie ? (Y/N)")

        if choix == "Y":
            with open(save_url, "rb") as f:
                selected_level = pickle.load(f)
        else:
            selected_level = select_level()
    else:
        selected_level = select_level()

    return selected_level

def save(data, url_save = "./save/"):
    save_url = os.path.join(url_save, "save.pickle")
    pickle.dump(data, open(save_url, "wb"))

if __name__ == "__main__":
    selected_level = load_save()
    selected_level.render()