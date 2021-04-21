import tkinter as tk
from tkinter import *
from threading import Thread, Event
from logic import *
import sys


# Funkcje aplikacji

def getAccouns():
    x = accounts.get("1.0", END)
    return x.split()


def startBot():
    bot = Thread(target=start, args=(
        pLogin.get(), pPassword.get(), getAccouns()))
    bot.start()


def writeConsole(text):
    console.insert(END, text)


# Wyglad okna
window = tk.Tk()
window.title("Instagram bot")
canvas = tk.Canvas(window, height=480, width=240, bg="#282828")
canvas.pack()
lLogin = Label(canvas, text="Login:", fg='#fff', bg="#282828")
lLogin.place(relx=0.1, rely=0.05)
pLogin = tk.Entry(canvas, width=30, bg="#E5E5E5")
pLogin.place(relx=0.1, rely=0.1)
lPassword = Label(canvas, text="Password:", fg='#fff', bg="#282828")
lPassword.place(relx=0.1, rely=0.15)
pPassword = tk.Entry(canvas, width=30, bg="#E5E5E5", show="*")
pPassword.place(relx=0.1, rely=0.2)

lAccounts = Label(
    canvas, text="Accounts:  -separated by a space", fg='#fff', bg="#282828")
lAccounts.place(relx=0.1, rely=0.40)
accounts = tk.Text(canvas, bg="#E5E5E5",
                   width=30, height=30, wrap=WORD)
accounts.place(relx=0.1, rely=0.45, relwidth=0.8, relheight=0.36)

startButton = tk.Button(canvas, text="Start", padx=10,
                        pady=5, fg="white", bg="#000000",  command=startBot)
startButton.place(relx=0.2, rely=0.86)
stopButton = tk.Button(canvas, text="Stop", padx=10,
                       pady=5, fg="white", bg="#000000")
stopButton.place(relx=0.55, rely=0.86)

window.mainloop()
