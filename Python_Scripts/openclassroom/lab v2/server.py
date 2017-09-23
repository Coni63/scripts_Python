import socket

if __name__ == "__main__":
    hote = ''
    port = 12800

    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.bind((hote, port))


    while True:
        socket.listen(5)
        client, address = socket.accept()
        print("{} connected".format(address))
        response = client.recv(255)
        if response != "":
            print(response)

    print("Close")
    client.close()
    socket.close()