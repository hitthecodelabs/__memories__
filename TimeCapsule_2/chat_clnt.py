import socket
from threading import Thread
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
        client_socket.send(l)
        l = f.read(1024)


def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ)
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "ascii"))
    if msg == "salir":
        client_socket.close()
        top.quit()
    elif msg == "Enviar":
        send_datas()

def on_closing(event=None):
    my_msg.set("salir")
    send()

top = tkinter.Tk()
top.title("Chat")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()
my_msg.set("Usuario")
scrollbar = tkinter.Scrollbar(messages_frame)
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

# ----Now comes the sockets part----
# HOST = input('Enter host: ')
nombreEquipo = socket.gethostname()
HOST = socket.gethostbyname(nombreEquipo)
PORT = 33000

BUFSIZ = 1024
ADDR = ('localhost', 9999)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # Starts GUI execution.
# client_socket.close()
