from tkinter import *
from tkinter import messagebox
import os

root = Tk()

root.title("Menu")

# root.geometry("287x175")
root.iconbitmap(
    r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\GL_icon.ico")


def HvsH():
    root.destroy()
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\gui10_rps_PvsP.py")


def HvsC():
    root.destroy()
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\gui9_rps_PvsC.py")


def Alert():
    messagebox.showinfo("Sorry", "This option is in beta version.")


root_Heading = Label(root, text="Rock, Paper, Scissor Game",
                     fg="white", bg="green", bd=3, relief=SUNKEN, font="bold")

root_Menu_Heading = Label(root, text="Menu", bg="yellow", bd=3, relief=RAISED)
root_Menu_Text = Label(root, text="Choose Game Mode !")

root_Human_Human = Button(root, text="Play Human/Human",
                          width=20, bd=1, relief=SOLID, command=HvsH)
root_Human_Computer = Button(
    root, text="Play Human/Computer", width=20, bd=1, relief=SOLID, command=HvsC)
root_Settings = Button(root, text="Settings", width=20,
                       bd=1, relief=SOLID, command=Alert)

root_credit = Label(root, text="A game by Aayan Yasin.",
                    font=["Bookman Old Style", 10])

root_Heading.grid(row=0, column=0)
root_Menu_Heading.grid(row=1, column=0)
root_Menu_Text.grid(row=2, column=0)
root_Human_Human.grid(row=4, column=0)
root_Human_Computer.grid(row=5, column=0)
root_Settings.grid(row=6, column=0)
root_credit.grid(row=7, column=0)

root.mainloop()
