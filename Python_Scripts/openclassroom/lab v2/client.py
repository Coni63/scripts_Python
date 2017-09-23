import socket
import threading

class ThreadedClient(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.connect((self.host, self.port))

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
            except:
                self.sock.close()


    def listenToServer(self):
        size = 1024
        while True:
            try:
                data = self.sock.recv(size)
                if data:
                    response = data
                    print(response)
            except:
                self.sock.close()

    def listenToClient(self):
        while True:
            txt = input('test')
            if txt == "Q":
                self.sock.close()
                break
            else:
                self.sock.send(txt.encode())


if __name__ == "__main__":
    hote = "localhost"
    port = 12800
    ThreadedClient(hote, port).connect()


