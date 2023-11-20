import socket
from threading import Thread


def accept_incoming_connections():

    while True:
        client, client_address = SERVER.accept()
        print("%s:%s se ha conectado." %client_address)
        client.send(bytes("Saludos! Escribe un usuario y presiona enter!", "UTF-8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.

    name = client.recv(1024).decode("UTF-8")
    info = 'Bienvenido %s! Para salir del chat escribir: "salir".' % name
    client.send(bytes(info, "utf8"))
    msg = "%s se ha unido al chat!" % name
    #broadcast(bytes(msg, "UTF-8"))
    clients[client] = name
    lista = [""]
    i = 1
    while True:
        msg = client.recv(1024)
        if msg != bytes("salir", "utf8") and msg!= "Enviar":
            broadcast(msg, name + ": ")
        elif msg == "Enviar":
            leer = client.recv(2014)
            # sc, address = s.accept()
            # print(address)
            f = open('descarga_' + str(i) + ".pdf", 'wb')  # open in binary
            i = i + 1
            print(i)
            while True:
                while leer:
                    f.write(leer)
                    leer = client.recv(1024)
                f.close()
            #client.close()
        else:
            #client.send(bytes("salir", "UTF-8"))
            print(name, 'ha dejado el chat')
            del clients[client]
            broadcast(bytes("%s ha dejado el chat." % name, "UTF-8"))
            break
        #client.close()


def broadcast(msg, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "UTF-8") + msg)


if __name__ == "__main__":
    clients = {}
    addresses = {}
    # HOST = ''
    nombreEquipo = socket.gethostname()
    print("Contectando...")
    HOST = socket.gethostbyname(nombreEquipo)
    PORT = 33000
    # BUFSIZ = 1024
    ADDR = ('localhost', 9999)
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind(ADDR)
    SERVER.listen(10)

    while True:
        try:
            #newsocket, fromaddr = SERVER.accept()
            ACCEPT_THREAD = Thread(target=accept_incoming_connections)
            ACCEPT_THREAD.start()
            ACCEPT_THREAD.join()
            print('Done with client: ' + str(fromaddr))
        except ConnectionResetError:
            print('Program closing...')
            break

    SERVER.close()
