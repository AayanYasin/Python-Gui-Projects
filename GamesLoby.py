import os
from tkinter import *
from tkinter import messagebox

root = Tk()

root.iconbitmap(
    r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\GL_icon.ico")
root.title("Game Loby \\ Aayan Yasin")

root.geometry("700x450")
root.minsize(700, 450)

Label(root, text="Games Loby :)", font=[
      "Bookman Old Style", 20]).place(x=254, y=0)

Label(root, text="Play with love !").place(x=310, y=45)


def Log_in():
    if os.path.isfile(r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\server1.py"):
        try:
            import server1
        except ModuleNotFoundError:
            pass
        print("File exist")
        root_User_name_login3.destroy()
        root_User_name_login1.grid(row=0, column=0)
        root_User_name_login2.grid(row=0, column=1)
        root_User_name_login2.config(text=server1.Username)
        root_Logout.place(x=640, y=0)
    else:
        print("File not exist")
        root_Help.place(x=640, y=0)


def sa():
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\gui_Server_User_Account.py")
    root.destroy()


def Log_out():
    os.remove(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\server1.py")
    print("File deleted Successfully...!")
    print("Log Out Successfully...!")
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\GamesLoby.py")
    root.destroy()


def helpUs():
    messagebox.showinfo("Help", "You are in games loby. Here you can play different games in Python Gui made by Aayan Yasin. For now here are 6 games, more will be added soon. You can log in so games would know your name automaticly and set it without bothering you to write again and again. Happy Playing :)")


UserF = Frame(root, bd=2, relief=SOLID)
root_User_name_login1 = Label(UserF, text="User : ")
root_User_name_login3 = Button(
    UserF, text="Log In", width=6, relief=FLAT, command=sa)
root_User_name_login2 = Label(UserF, text="Unknown")
root_Logout = Button(root, text="LOG OUT", bd=1, width=7,
                     relief=SOLID, command=Log_out)
root_Help = Button(root, text="Help", bd=1, width=7,
                   relief=SOLID, command=helpUs)
UserF.place(x=0, y=0)
root_User_name_login3.grid(row=0, column=1)


def Open_rps():
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\gui11_rps_Menu.py")
    root.destroy()


def Open_CGame():
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\gui12_ColorGame.py")
    root.destroy()


def Open_Casino():
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\gui13_Casino.py")
    root.destroy()


def Open_Hangman():
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\gui15_Hangman.py")
    root.destroy()


def Open_SWG():
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\gui18_SWG_menu.py")
    root.destroy()


def Open_Beta():
    messagebox.showwarning(
        "Comming Soon", "This app is under development and will be published soon, untill then feel free to play other games.")


icon1 = PhotoImage(
    file=r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\gameicon.png")
icon2 = PhotoImage(
    file=r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\cominsoon.png")
Button(root, image=icon1, width=53, height=66,
       command=Open_rps).place(x=170, y=83)

Label(root, text="Rock, paper, scissor").place(x=145, y=165)

Button(root, image=icon1, width=53, height=66,
       command=Open_CGame).place(x=320, y=83)

Label(root, text="Color Guessing Game").place(x=290, y=165)

Button(root, image=icon1, width=53, height=66,
       command=Open_Casino).place(x=470, y=83)

Label(root, text="Casino Number Guess").place(x=440, y=165)

Button(root, image=icon1, width=53, height=66,
       command=Open_Hangman).place(x=170, y=200)

Label(root, text="Hangman Game").place(x=153, y=284)

Button(root, image=icon1, width=53, height=66,
       command=Open_SWG).place(x=320, y=200)

Label(root, text="Snake, Water, Gun").place(x=300, y=284)

Button(root, image=icon1, width=53, height=66).place(x=470, y=200)

# Label(root, text="").pack()

Button(root, image=icon2, width=53, height=66,
       command=Open_Beta).place(x=170, y=320)

Label(root, text="Coming Soon").place(x=160, y=410)

Button(root, image=icon2, width=53, height=66,
       command=Open_Beta).place(x=320, y=320)

Label(root, text="Coming Soon").place(x=311, y=410)

Button(root, image=icon2, width=53, height=66,
       command=Open_Beta).place(x=470, y=320)

Label(root, text="Coming Soon").place(x=462, y=410)


# root.pack()
Log_in()
root.mainloop()
