import os
from tkinter import *
import database as db

account = Tk()

account.title("Sign UP")
account.geometry("300x200")
account.iconbitmap(
    r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\GL_icon.ico")

# F1 = Frame(account).grid(row=0, column=0)
# F2 = Frame(account).grid(row=1, column=0)

cb = IntVar()


def Delet():
    Result.config(text="")
    Result_text.config(text="")


def Store():
    Uname = str(a1.get())
    Uname1 = Uname.title()
    Upass2 = str(a2.get())
    Upass3 = str(a3.get())
    path1 = r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\database.py"
    # -- Checks if all fields are filled or not.
    if len(Upass2) != 0 and len(Upass3) != 0 and cb.get() == 1 and len(Uname1) != 0:
        # -- Checks if SetPassword match Confirm Password.
        if Upass2 == Upass3:
            # -- Check if Username already exist or not.
            if Uname1 in db.Users:
                print("Username already exist !")
                Result.config(text="Result :")
                Result_text.config(text="Username already exist !")
                account.after(3000, Delet)
            else:
                with open(path1, "a") as server:
                    server.write(
                        f"\nUsers.append('{Uname1}')\nPasswords.append('{Upass2}')")
                os.startfile(
                    r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\gui_Server_User_Account.py")
                print("Done")
                Result_text.config(text="Successfully Loged In")
                Result.config(text="Result :")
                account.after(3000, Delet)
                account.destroy()
        else:
            print("Confirm password does not match !")
            Result.config(text="Result :")
            Result_text.config(text="Confirm password does not match !")
            account.after(3000, Delet)
    else:
        print("Please Enter All Credentials !")
        Result_text.config(text="Please Enter All Credentials !")
        Result.config(text="Result :")
        account.after(3000, Delet)


def SHPass():
    if a2.cget("show") == "\u2022":
        a2.config(show="")
        a3.config(show="")
        rbps.config(text="Hide")
    elif a2.cget("show") == "":
        a2.config(show="\u2022")
        a3.config(show="\u2022")
        rbps.config(text="Show")


def Open_Server_SignUp():
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\gui_Server_User_Account.py")
    account.destroy()


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

Label(account, text="Sign Up : ", font=[
      "Bookman Old Style", 15]).pack(anchor=W)
Label(account, text="Name : ").pack(anchor=W)
a1 = Entry(account)
a1.place(x=68, y=30)
Label(account, text="Password : ").pack(anchor=W)
a2 = Entry(account, show="\u2022")
a2.place(x=68, y=52)
Label(account, text="Confirm : ").pack(anchor=W)
a3 = Entry(account, show="\u2022")
a3.place(x=68, y=74)
rbps = Button(account, text="Show", bd=2, command=SHPass)
rbps.place(x=195, y=71)
CB = Checkbutton(
    account, text="I agree to Terms and Conditions.", font="arial 8", variable=cb, onvalue=1, offvalue=0)
CB.place(x=1, y=101)
Button(account, text="Sign Up", command=Store).place(x=4, y=130)
Button(account, text="Log In ?", relief=FLAT,
       font="ariel 8 underline italic", command=Open_Server_SignUp).place(x=58, y=135)
Result = Label(account, text="")
Result_text = Label(account, text="", font="tmes 8")
Result.place(x=4, y=168)
Result_text.place(x=50, y=169)

account.mainloop()
