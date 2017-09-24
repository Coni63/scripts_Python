import os
import sys
import pickle
import datetime
import time
import socket
import threading
import select
import itertools
import signal

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


class ThreadedServer(object):
    MAX_PLAYER = 5
    MIN_PLAYER = 2
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.player_list=[None]*self.MAX_PLAYER
        self.turn = 0
        self.select_level()
        self.started = False

    @property
    def nb_player(self):
        return len(list(filter(lambda x: x is not None, self.player_list)))

    def remove_user(self, user):
        """
        Lors d'une deconnexion, on supprime l'utilisateur de la liste des joueurs.
        Cela permet par exemple a une 3eme personne de replacer joueur1 qui est parti
        :param user: la connexion qui a été interrompu
        :return: None
        """
        self.player_list[self.player_list.index(user)] = None
        user.close()
        print("user disconnected")

    def select_level(self, url_map="./map/"):
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

        # for index, level in enumerate(list_level):
        #     print("[{}] : {}".format(index, level[:-4]))
        #
        # choix = input("Quel level souhaitez vous faire ?")
        # while not is_valid(choix, type_="int", choix=list(range(len(list_level)))):
        #     choix = input("Mauvaise entrée! Quel level souhaitez vous faire ?")
        #
        # choix = int(choix)
        choix = 1

        file_url = os.path.join(url_map, list_level[choix])
        niveau = []
        with open(file_url, "r") as f:
            for line in f.read().splitlines():
                niveau.append(list(line))

        self.niveau = Labyrinthe(niveau, list_level[choix])
        #self.niveau.render()

    def listen(self):
        """
        Accepte toutes les connexion jusqu'a atteindre max_joueurs. Après il rejette la connexion et informe le client.
        Une fois le nb de joueurs atteint, un thread est lancé pour gérer la partie
        :return:
        """
        self.sock.listen(5)
        print("Serveur lancé, en attente de connexion")
        threading.Thread(target=self.status).start()
        while True:
            client, address = self.sock.accept()
            if self.nb_player == self.MAX_PLAYER or self.started:
                print("rejet de", client)
                client.send(b"Max Player limit reached")
                client.close()
            else:
                num = self.player_list.index(None)
                self.player_list[num] = client
                client.send(("Bonjour Player_{}".format(num+1)).encode())

            if self.nb_player >= self.MIN_PLAYER:
                threading.Thread(target=self.wait_start).start()


    def wait_start(self):
        self.broadcast("wait_start")
        while True:
            rlist, wlist, xlist = select.select(self.player_list, [], [], 10)
            start = False
            for client in rlist:
                try:
                    msg_recu = client.recv(1024)
                    msg_recu = msg_recu.decode()
                    if msg_recu == "C":
                        start = True
                        break
                except:
                    self.remove_user(client)
                    self.broadcast("deco")
                    if self.nb_player < self.MIN_PLAYER:
                        return False
            if start:
                threading.Thread(target=self.start_game).start()
                return False

    def status(self):
        """
        Thread en parralèle pour afficher le status du serveur toutes les n-secondes
        :return: None
        """
        while True:
            time.sleep(3)
            print("{} : {} client connected".format(datetime.datetime.now(), self.nb_player))

    def start_game(self):
        self.broadcast("game_start")
        self.started = True
        time.sleep(0.5)
        loop_player = itertools.cycle(self.player_list)
        while True:
            active_player = next(loop_player)
            active_player.send(b"set_active")
            self.broadcast("wait_other", except_=active_player)
            rlist, wlist, xlist = select.select([active_player], [], [], 1000)
            if rlist == []:
                active_player.send(b"too_late")
            else:
                for client in rlist:
                    try:
                        msg_recu = client.recv(1024)
                        msg_recu = msg_recu.decode()
                        print("Reçu {}".format(msg_recu))
                    except:
                        self.remove_user(client)
                        self.broadcast("deco")
                        return False


    def broadcast(self, phrase, except_=None):
        """
        Envoie un message a tous les joueurs connecté sauf celui mentionné dans le except
        :param phrase: la phrase a envoyer
        :param except_: le joueur à exclure dans l'envoi
        :return: None
        """
        for player in self.player_list:
            if player in [except_, None]:
                pass
            else:
                try:
                    player.send(phrase.encode())
                except:
                    self.remove_user(player)
                    self.broadcast("deco")


if __name__ == "__main__":
    hote = ''
    port = 12800
    ThreadedServer(hote, port).listen()
