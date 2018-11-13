import socket
from threading import Thread
import sys

def receiveMessage():
    try:
        while True:
            message = client.recv(2018).decode()
            if message != "/t":
                print(message)
    except:
        exit()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverIP = "192.168.1.57"
# serverIP = "192.168.43.234"
serverPortNumber = 666

try:
    client.connect((serverIP, serverPortNumber))
except:
    print("Couldn't connect to server")
    exit()

receiver = Thread(target=receiveMessage)
receiver.setDaemon = True
receiver.start()

alias = input(">>What's your name? ")
client.send("/a {}".format(alias).encode())

while True:
    try:
        messageToSend = input()
        client.send(messageToSend.encode())
        if messageToSend.split()[0] == '/l':
            print(">>You've logged out")
            break
    except Exception as e:
        print(e)
        break

print(">>Connection to server terminated")
client.close()