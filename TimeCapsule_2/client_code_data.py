import socket
#import sys
#import chardet

s = socket.socket()
s.connect(("localhost",9999))

import tkinter
from tkinter import filedialog


def send_datas():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Open file",
                                          filetypes=(("Text Files", "*.txt"),
                                                     ("All files", "*.*")))

    form = tkinter.Tk()
    form.title("Python Menus")
    nombre = filename.split("/")[-1]
    f = open(nombre, "rb")
    l = f.read(1024)
    while l:
        s.send(l)
        l = f.read(1024)

send_datas()
s.close()

"""
filename = filedialog.askopenfilename(initialdir="/",
                                          title="Open file",
                                          filetypes=(("Text Files", "*.txt"),
                                                     ("All files", "*.*")))
#form = tkinter.Tk()
#form.title("Python Menus")
nombre = filename.split("/")[-1]
print(nombre)
#vaina = chardet.detect(open(nombre, 'rb').read())['encoding']
#print(vaina)
"""