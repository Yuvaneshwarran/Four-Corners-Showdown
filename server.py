import socket
import ssl
from _thread import *
import pickle
from game import Game

server = "localhost"  # Change this to the appropriate IP address if needed
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Read the content of server.crt and server.key
# with open('server.crt', 'rb') as cert_file:
#     certificate = cert_file.read()

# with open('server.key', 'rb') as key_file:
#     private_key = key_file.read()

# Create an SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

# Set the certificate and private key
# context.load_cert_chain(certfile='server.crt', keyfile='server.key')

# Bind the socket with SSL context
s.bind((server, port))
s.listen(2)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0

def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))
    while True:
        try:
            data = conn.recv(4096).decode()
            if gameId in games:
                game = games[gameId]
                game.update()
                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)
                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break
    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    idCount += 1
    gameId = (idCount - 1) // 4
    if idCount % 4 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    elif idCount % 4 == 0:
        games[gameId].ready = True
    p = (idCount - 1) % 4
    start_new_thread(threaded_client, (conn, p, gameId))
