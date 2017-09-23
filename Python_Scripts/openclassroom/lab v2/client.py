import socket

def open_connection(host, port):
    socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_.connect((host, port))
    return socket_

def main():
    connexion = open_connection(hote, port)
    while True:
        txt = input('test')
        if txt == "Q":
            break
        else:
            connexion.send(txt.encode())
    connexion.close()


if __name__ == "__main__":
    hote = "localhost"
    port = 12800
    main()


