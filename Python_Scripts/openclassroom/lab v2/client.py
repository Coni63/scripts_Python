import socket
import threading
import signal
import os
import time

class FiveSec(threading.Thread):
    def restart(self):
        self.my_timer = time.time() + 5
    def run(self, *args):
        self.restart()
        while 1:
            time.sleep(0.1)
            if time.time() >= self.my_timer:
                break
        os.kill(os.getpid(), signal.SIGINT)

class ThreadedClient(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.connect((self.host, self.port))
        self.active = False

    def connect(self):
        size = 1024
        while True:
            try:
                data = self.sock.recv(size)
                if data:
                    response = data
                    if response == b"Max Player limit reached":
                        print("La limite de joueur a été atteinte, vous ne pouvez pas vous connecter au serveur")
                        self.sock.close()
                    else:
                        print(response.decode())
                        self.listener = threading.Thread(target=self.listenToServer).start()
                        self.sender = threading.Thread(target=self.listenToClient).start()
                        break
            except:
                self.sock.close()


    def listenToServer(self):
        size = 1024
        while True:
            try:
                data = self.sock.recv(size)
                if data:
                    response = data
                    if response == b"set_active":
                        self.active = True
                    elif response == b"wait_start":
                        print("en attente de depart")
                        txt = input("Envoyer \"C\" pour demarrer")
                        self.sock.send(txt.encode())
                    elif response == b"game_start":
                        print("C'est parti, Amusez-vous bien !")
                    elif response == b"too_late":
                        print("Trop tard, vous jouerez au prochain tour")
                        self.active = False
                    elif response == b"wait_other":
                        print("Le joueur suivant joue")
                    elif response == b"deco":
                        print("Un joueur s'est deconnecté, fin de partie")
            except:
                self.sock.close()

    def listenToClient(self):
        while True:
            if self.active:
                txt = input('A vous de jouer : ')

                if txt == "Q":
                    self.sock.close()
                    break
                else:
                    if self.active:                  # le input est ecrit quand le joueur est actif mais il peut repondre quand il est inactif donc on verifie
                        self.sock.send(txt.encode())
                        self.active = False
                    else:
                        print("Trop tard, vous jouerez au prochain tour")


if __name__ == "__main__":
    hote = "localhost"
    port = 12800
    ThreadedClient(hote, port).connect()


