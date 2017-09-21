# -*-coding:Utf-8 -*

import os
import sys
import pickle

from labyrinthe import Labyrinthe

def is_valid(x, type_="int", choix=None):
    """
    Vérifie la validité de l'input de l'utilisateur en fonction du type et d'une liste de choix (optionnelle)
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
    """
    Affiche la liste des niveaux dispo et propose a l'utilisateur de choisir son level
    Verifie la validité de l'input
    :param url_map: url du dossier avec les maps (par defaut c'est un dossier map au meme niveau)
    :return: l'instance de labyrinthe choisie par l'utilisateur
    """

    print("Selectionnez le level :\n")

    try:
        list_level = [f for f in os.listdir(url_map) if os.path.isfile(os.path.join(url_map, f))]
    except FileNotFoundError:
        print("Dossier non trouvé. Fermeture")
        sys.exit(0)

    if len(list_level) == 0:
        print("Aucun niveau trouvé. Fermeture")
        sys.exit(0)

    for index, level in enumerate(list_level):
        print("[{}] : {}".format(index, level[:-4]))

    choix = input("Quel level souhaitez vous faire ?")
    while not is_valid(choix, type_="int", choix=list(range(len(list_level)))):
        choix = input("Mauvaise entrée! Quel level souhaitez vous faire ?")

    choix = int(choix)
    file_url = os.path.join(url_map, list_level[choix])
    niveau = []
    with open(file_url, "r") as f:
        for line in f.read().splitlines():
            niveau.append(list(line))

    niveau = Labyrinthe(niveau, list_level[choix])
    save(niveau)
    return niveau

def load_savegame(url_save = "./save/"):
    """
    Vérifie la présence d'une sauvegarde, si elle existe, on propose de continuer la partie ou d'en faire une nouvelle
    :param url_save: url du dossier avec les maps (par defaut c'est un dossier map au meme niveau)
    :return: l'instance de labyrinthe choisie ou chargée
    """
    save_url = os.path.join(url_save, "save.pickle")
    if os.path.isfile(save_url):
        choix = input("Une sauvegarde a été trouvée, voulez-vous la continuer ? (Y/N)").upper()
        while not is_valid(choix, type_="str", choix=["Y", "N"]):
            choix = input("Mauvaise entrée! Voulez-vous continuer la partie ? (Y/N)").upper()

        if choix == "Y":
            with open(save_url, "rb") as f:
                selected_level = pickle.load(f)
        else:
            selected_level = select_level()
    else:
        selected_level = select_level()

    return selected_level

def save(data, url_save = "./save/"):
    """
    Sauvegarde le labirynthe dans le fichier pickle
    :param data: l'instance de labyrinthe
    :param url_save: url du dossier avec les maps (par defaut c'est un dossier map au meme niveau)
    :return: None
    """
    save_url = os.path.join(url_save, "save.pickle")
    pickle.dump(data, open(save_url, "wb"))

def delete_save(url_save = "./save/"):
    """
    Quand la partie est gagné, la sauvegarde est supprimée car elle n'a plus aucun sens
    :param url_save: url du dossier avec les maps (par defaut c'est un dossier map au meme niveau)
    :return: None
    """
    save_url = os.path.join(url_save, "save.pickle")
    os.remove(save_url)

if __name__ == "__main__":
    level = load_savegame()
    while True:
        level.render()
        commande = input("\nEntrez une commande (Direction et Nombre de pas)")
        direction, qte = commande[0].upper(), commande[1:]
        if direction in ["N", "S", "E", "O"] and (qte.isnumeric() or len(qte) == 0):
            if qte.isnumeric():
                qte = int(qte)
            else:
                qte=1
            fin = level.move(direction, qte)
            save(level)
        elif direction == "Q":
            save(level)
            sys.exit(0)
        else:
            fin = False
            print("entrée incorrecte, pas de mouvements")

        if fin:
            delete_save()
            break