import datetime
import time
import socket
import threading


class ThreadedServer(object):
    LIMIT = 2
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.player=[None]*self.LIMIT

    @property
    def nb_player(self):
        return len(list(filter(lambda x: x is not None, self.player)))

    def remove_user(self, user):
        self.player[self.player.index(user)] = None
        user.close()
        print("user disconnected")

    def listen(self):
        self.sock.listen(5)
        print("Serveur lancé, en attente de connexion")
        threading.Thread(target=self.status).start()
        while True:
            client, address = self.sock.accept()
            print(self.nb_player)
            if self.nb_player == self.LIMIT:
                print("rejet de", client)
                client.send(b"Max Player limit reached")
                client.close()
            else:
                num = self.player.index(None)
                self.player[num] = client
                client.send(("Bonjour Player_{}".format(num+1)).encode())
                # client.settimeout(60)
                threading.Thread(target = self.listenToClient, args = (client, address)).start()

    def status(self):
        while True:
            time.sleep(3)
            print("{} : {} client connected".format(datetime.datetime.now(), self.nb_player))

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data
                    response = data
                    print(client, response)
                else:
                    self.remove_user(client)
                    break
            except:
                self.remove_user(client)
                break


if __name__ == "__main__":
    hote = ''
    port = 12800
    ThreadedServer(hote, port).listen()
