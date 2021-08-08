import os
from tkinter import *
import database as db

account = Tk()

account.title("Sign IN")
account.geometry("300x200")
account.iconbitmap(
    r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\GL_icon.ico")


def Delet():
    Result.config(text="")
    Result_text.config(text="")


def LogIn():
    Uname = a1.get()
    Uname1 = Uname.title()
    Upass2 = a2.get()
    path1 = r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\server1.py"
    try:
        u1 = db.Users.index(Uname1)
        p2 = db.Passwords[u1]
        if Upass2 == p2:
            with open(path1, "w") as server:
                server.write(f"\nUsername = '{Uname1}'\nPassword = '{Upass2}'")
            os.startfile(
                r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\GamesLoby.py")
            print("Done")
            account.destroy()
        elif Upass2 != p2:
            print("Incorrect Password")
            Result.config(text="Result :")
            Result_text.config(text="Incorrect Password")
            account.after(3000, Delet)
    except ValueError:
        print("Username does not exist !")
        Result.config(text="Result :")
        Result_text.config(text="Username does not exist !")
        account.after(3000, Delet)


def SHPass():
    if a2.cget("show") == "\u2022":
        a2.config(show="")
        rbps.config(text="Hide")
    elif a2.cget("show") == "":
        a2.config(show="\u2022")
        rbps.config(text="Show")


def Open_Server_LogIn():
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\gui_SignUp_User_Account.py")
    account.destroy()


def Open_GL():
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\GamesLoby.py")
    account.destroy()


def Open_DA():
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\gui_DeletMyAccount.py")
    account.destroy()


maindd = Menu(account)
dd = Menu(maindd, tearoff=0)
dd.add_command(label="Games Loby", command=Open_GL)
dd.add_command(label="Delete Account", command=Open_DA)
dd.add_separator()
dd.add_command(label="Exit", command=quit)
maindd.add_cascade(label="☰", menu=dd)

account.config(menu=maindd)
Label(account, text="Log In : ", font=[
      "Bookman Old Style", 15]).pack(anchor=W)
Label(account, text="Name : ").pack(anchor=W)
a1 = Entry(account)
a1.place(x=68, y=30)
Label(account, text="Password : ").pack(anchor=W)
a2 = Entry(account, show="\u2022")
a2.place(x=68, y=52)
rbps = Button(account, text="Show", bd=2, command=SHPass)
rbps.place(x=195, y=49)
Button(account, text="Sign Up ?", relief=FLAT,
       font="ariel 8 underline italic", command=Open_Server_LogIn).place(x=50, y=85)
Button(account, text="Log In", command=LogIn).place(x=5, y=80)
Result = Label(account, text="")
Result_text = Label(account, text="", font="tmes 8")
Result.place(x=4, y=118)
Result_text.place(x=50, y=119)

account.mainloop()

# from tkinter import *

# master = Tk()

# variable = StringVar(master)
# variable.set("one")  # default value

# w = OptionMenu(master, variable, "one", "two", "three")
# w.pack()

# mainloop()
