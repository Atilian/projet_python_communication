#!/usr/bin/python3

import socket
import tkinter
import datetime

date = datetime.datetime.now()
Mydate = date.strftime("%H:%M")


class MySocket:

    def __init__(self, sock=None):
        if (sock == None):
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))
        print("\nConnexion...")

    def send_message(self, message):
        msg_enc = message.encode("utf-8")
        self.sock.send(msg_enc)


def recv(client):

    reception = client.sock.recv(1024)

    reception = reception.decode("utf-8")
        


def main():

    client = MySocket()
    client.connect("127.0.0.1", 5566)

    window = tkinter.Tk()

    window.title("Communication")

    window.minsize(480, 500)
    window.maxsize(480, 500)

    # ---------------------------------------------------- #

    listmsg = tkinter.Listbox(window, width=45)
    listmsg.place(x=20, y=20, height=400)
    # ---------------------------------------------------- #

    canva_send = tkinter.Canvas(window)
    canva_send.pack(side= tkinter.BOTTOM, pady=20)

    msgEntry = tkinter.Entry(canva_send, width=45)
    msgEntry.grid(column=0, row=0)

    sendButton = tkinter.Button(canva_send, text="ENTER", command=lambda: [listmsg.insert("end" ,Mydate + " //> " + msgEntry.get()), client.send_message(msgEntry.get()), msgEntry.delete(0, "end")])
    sendButton.grid(column=1, row=0)

    # ---------------------------------------------------- #

    #window.after(2000, recv(client))

    
    window.mainloop()


main()




