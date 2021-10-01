#!/usr/bin/python3

import socket
import threading
import socketserver
import tkinter
import datetime
from tkinter.constants import S

date = datetime.datetime.now()
date = date.strftime("%H:%M")

HostAddr = "127.0.0.1"
Port = 5566

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serveur.bind((HostAddr, Port))

serveur.listen(5)

ListClients = []

class ClientThread:

    def __init__(self, client, addr, port):
        
        self.client = client
        self.addr = addr
        self.port = port

        print ("<%s:%d> Connected.." %(self.addr, self.port))
        
        self.client.send(("Welcome to this chatroom !").encode("utf-8"))

    def recv(self):

        while True:

            try:

                print("tt")
            
                reception = self.client.recv(1024)
                reception = reception.decode("utf-8")

                if (reception):

                    print(reception)
                    print("test")

                    reception = "<%s> < %s //>" %(self.addr, date)

                    self.broadcast(reception)

                else:

                    print("test")

                    self.remove(self)

            except:

                print("tfft")


                continue

    def broadcast(self, message):

        for clients in ListClients:
            
            if (clients.client != self.client):
            
                try:
                    
                    message = message.encode("utf-8")

                    clients.client.send(message)

                except:

                    clients.client.close()

                    self.remove(clients)

    
    def remove(client):

        if (client in ListClients):

            ListClients.remove(client)

            if (len(ListClients) <= 0):
                
                serveur.close()


def main():

    while True:
        
        print("test1")

        (client, (addr, port)) = serveur.accept()

        print("test2")

        NewClient = ClientThread(client, addr, port)

        print("test3")

        ListClients.append(NewClient)

        print("test11")

        NewClient.recv()

        print("test12")

    serveur.close()    
main()
