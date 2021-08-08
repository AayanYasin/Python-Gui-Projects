from tkinter import *
from tkinter import messagebox
import random as rd
import time as t
import sys
import os

root = Tk()

root.geometry("325x630")
root.iconbitmap(
    r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\GL_icon.ico")

name = "Player"
betShow = None
balance = 200
Pchoice = None
FortuneNo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
RePaid = range(1, 100)
TIMe = 15


def Set_name():
    if os.path.isfile(r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\server1.py"):
        try:
            import server1
        except ModuleNotFoundError:
            pass
        root_UserName_Entry.insert(0, server1.Username)
        print("File exist")
    else:
        print("File do not exist")


def Name():
    global name
    name = root_UserName_Entry.get()
    if len(name) != 0:
        root_Name_Show_num.config(text=name)
        root_Bet_Entry.config(state=NORMAL)
        root_Bet_btn.config(state=NORMAL)
    else:
        messagebox.showerror("Sorry", "Name can not be empty.")


def Bet():
    global betShow
    global balance
    global root_AD_btn
    betShow = int(root_Bet_Entry.get())
    if balance >= betShow and betShow != 0:
        balance = balance-betShow
        root_Balance_Amount.config(text=balance)
        root_Bet_Show_num.config(text="$ {}".format(betShow))
        root_Start_Btn.config(state=NORMAL)
        root_Start_Btn.config(bg="lightgreen")
    else:
        messagebox.showerror("Sorry", "You do not have sufficient balance !")
        root_Bet_Entry.delete(0, END)
        root_Bet_Show_num.config(text="$")
    root_NA_num.config(text="--:--")
    root_Remarks_num.config(text="--:--")
    root_player_choice_num.config(text="--:--")
    root_Fortune_num.config(text="--:--")


def PlayStart():
    root_Start_Btn.config(state=DISABLED)
    root_Start_Btn.config(bg="gainsboro")
    root_Bet_Entry.config(state=DISABLED)
    root_Bet_btn.config(state=DISABLED)
    root_UserName_Entry.config(state=DISABLED)
    root_UserName_btn.config(state=DISABLED)
    root_Number_1.config(state=NORMAL)
    root_Number_2.config(state=NORMAL)
    root_Number_3.config(state=NORMAL)
    root_Number_4.config(state=NORMAL)
    root_Number_5.config(state=NORMAL)
    root_Number_6.config(state=NORMAL)
    root_Number_7.config(state=NORMAL)
    root_Number_8.config(state=NORMAL)
    root_Number_9.config(state=NORMAL)


def btn1():
    global b1
    global Pchoice
    b1 = 1
    Pchoice = b1
    root_Calculate_Btn.config(state=NORMAL)
    root_player_choice_num.config(text=Pchoice)


def btn2():
    global b2
    global Pchoice
    b2 = 2
    Pchoice = b2
    root_Calculate_Btn.config(state=NORMAL)
    root_player_choice_num.config(text=Pchoice)


def btn3():
    global b3
    global Pchoice
    b3 = 3
    Pchoice = b3
    root_Calculate_Btn.config(state=NORMAL)
    root_player_choice_num.config(text=Pchoice)


def btn4():
    global b4
    global Pchoice
    b4 = 4
    Pchoice = b4
    root_Calculate_Btn.config(state=NORMAL)
    root_player_choice_num.config(text=Pchoice)


def btn5():
    global b5
    global Pchoice
    b5 = 5
    Pchoice = b5
    root_Calculate_Btn.config(state=NORMAL)
    root_player_choice_num.config(text=Pchoice)


def btn6():
    global b6
    global Pchoice
    b6 = 6
    Pchoice = b6
    root_Calculate_Btn.config(state=NORMAL)
    root_player_choice_num.config(text=Pchoice)


def btn7():
    global b7
    global Pchoice
    b7 = 7
    Pchoice = b7
    root_Calculate_Btn.config(state=NORMAL)
    root_player_choice_num.config(text=Pchoice)


def btn8():
    global b8
    global Pchoice
    b8 = 8
    Pchoice = b8
    root_Calculate_Btn.config(state=NORMAL)
    root_player_choice_num.config(text=Pchoice)


def btn9():
    global b9
    global Pchoice
    b9 = 9
    Pchoice = b9
    root_Calculate_Btn.config(state=NORMAL)
    root_player_choice_num.config(text=Pchoice)


def Calculate():
    global fortune_Choice
    global balance
    root_Calculate_Btn.config(state=DISABLED)
    root_Number_1.config(state=DISABLED)
    root_Number_2.config(state=DISABLED)
    root_Number_3.config(state=DISABLED)
    root_Number_4.config(state=DISABLED)
    root_Number_5.config(state=DISABLED)
    root_Number_6.config(state=DISABLED)
    root_Number_7.config(state=DISABLED)
    root_Number_8.config(state=DISABLED)
    root_Number_9.config(state=DISABLED)
    root_Bet_Entry.config(state=NORMAL)
    root_Bet_btn.config(state=NORMAL)
    root_Bet_Entry.delete(0, END)
    fortune_Choice = rd.choice(FortuneNo)
    root_Fortune_num.config(text=fortune_Choice)
    if Pchoice == fortune_Choice:
        balance = balance + betShow*2
        root_Balance_Amount.config(text=balance)
        root_Remarks_num.config(text="Yahoo ! Correct.")
        root_NA_num.config(text="2X Bet = $ {} Left".format(balance))
    else:
        root_Remarks_num.config(text="Oops ! Incorrect.")
        root_NA_num.config(text="Bet Lost = $ {} Left".format(balance))
        if balance == 0:
            root_AD_show.config(state=NORMAL)
            root_AD_btn.config(state=NORMAL)


def AdButtonPack():
    global root_AD_btn
    root_Text_RePaid.destroy()
    root_AD_btn = Button(root, text="▶", width=5, state=DISABLED, command=Ad)
    root_AD_btn.place(x=190, y=535)


def AdRepay():
    global RePaidvar
    global balance
    global root_AD_Time
    global root_Text_RePaid
    root_AD_Time.destroy()
    RePaidvar = rd.choice(RePaid)
    root_Text_RePaid = Label(
        root, text="$ {} added to wallet !".format(RePaidvar))
    root_Text_RePaid.place(x=190, y=535)
    balance = RePaidvar
    root_Balance_Amount.config(text=balance)
    root_Text_RePaid.after(5000, AdButtonPack)


def TIMER1_15():
    global TIMe
    global root_AD_Time
    root_AD_Time.config(text="Wait {}s".format(TIMe))
    root_AD_Time.after(1000, TIMER1_15)
    TIMe -= 1
    if TIMe == 0:
        root_AD_Time.after(1000, AdRepay)
        TIMe = 15


def Ad():
    global RePaidvar
    global balance
    global root_AD_Time
    root_AD_btn.destroy()
    root_AD_Time = Label(root, text="Wait 15s !")
    root_AD_Time.place(x=190, y=535)
    TIMER1_15()


def Exit():
    sys.exit()


def Restart():
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\gui13_Casino.py")
    root.destroy()


def Exit_to_GL():
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\GamesLoby.py")
    root.destroy()


root_Menu_Back = Button(root, text="<--", command=Exit_to_GL)

root_Balance_Frame = Frame(root, bg="grey", bd=1, relief=SOLID)

root_Balance_Dollar_Icon_Showpiece = Label(root_Balance_Frame, text="$")
root_Balance_Amount = Label(root_Balance_Frame, text=balance)

root_Casino_Logo = Label(root, text="Casino", font=["Bookman Old Style", 20])

root_Name_Show = Label(root, text="Player : ")
root_Name_Show_num = Label(root, text="Name")

root_Bet_Show = Label(root, text="Bet : ")
root_Bet_Show_num = Label(root, text="$")

root_UserName = Label(root, text="Username : ")
root_UserName_Entry = Entry(root)
root_UserName_btn = Button(root, text="Ok", width=3, command=Name)

root_Bet = Label(root, text="Bet : ")
root_Bet_Entry = Entry(root, state=DISABLED)
root_Bet_btn = Button(root, text="Bet", state=DISABLED, width=3, command=Bet)

root_Start_Btn = Button(root, text="Play/Start", width=32,
                        state=DISABLED, bd=1, relief=RAISED, command=PlayStart)

root_Text = Label(root, text="Choose a number !")

root_Number_1 = Button(root, text=1, width=8, state=DISABLED, command=btn1)
root_Number_2 = Button(root, text=2, width=8, state=DISABLED, command=btn2)
root_Number_3 = Button(root, text=3, width=8, state=DISABLED, command=btn3)
root_Number_4 = Button(root, text=4, width=8, state=DISABLED, command=btn4)
root_Number_5 = Button(root, text=5, width=8, state=DISABLED, command=btn5)
root_Number_6 = Button(root, text=6, width=8, state=DISABLED, command=btn6)
root_Number_7 = Button(root, text=7, width=8, state=DISABLED, command=btn7)
root_Number_8 = Button(root, text=8, width=8, state=DISABLED, command=btn8)
root_Number_9 = Button(root, text=9, width=8, state=DISABLED, command=btn9)

root_Calculate_Btn = Button(root, text="Calculate", width=32,
                            state=DISABLED, bd=1, relief=RAISED, command=Calculate)

root_player_choice = Label(root, text="You Choosed : ")
root_player_choice_num = Label(root, text="--:--")

root_Fortune_show = Label(root, text="Fortune No. : ")
root_Fortune_num = Label(root, text="--:--")

root_Remarks_show = Label(root, text="Remarks : ")
root_Remarks_num = Label(root, text="--:--")

root_NA_show = Label(root, text="New Amount : ")
root_NA_num = Label(root, text="--:--")

root_AD_show = Label(root, text="Watch AD : ", state=DISABLED)
root_AD_btn = Button(root, text="▶", width=5, state=DISABLED, command=Ad)

root_Exit_Button = Button(root, text="Exit", bg="red",
                          fg="white", bd=2, relief=SOLID, width=6, command=Exit)
root_Restart_Button = Button(root, text="Restart", bg="red", fg="white",
                             bd=2, relief=SOLID, justify=LEFT, width=7, command=Restart)

root_Menu_Back.place(x=1, y=1)
root_Balance_Frame.place(x=280, y=1)
root_Balance_Dollar_Icon_Showpiece.grid(row=1)
root_Balance_Amount.grid(row=1, column=1)
root_Casino_Logo.place(x=100, y=40)
root_UserName.place(x=15, y=100)
root_UserName_Entry.place(x=100, y=102)
root_UserName_btn.place(x=230, y=99)
root_Bet.place(x=15, y=130)
root_Bet_Entry.place(x=100, y=132)
root_Bet_btn.place(x=230, y=130)
root_Name_Show.place(x=15, y=165)
root_Name_Show_num.place(x=140, y=165)
root_Bet_Show.place(x=15, y=190)
root_Bet_Show_num.place(x=145, y=190)
root_Start_Btn.place(x=23, y=220)
root_Text.place(x=85, y=255)
root_Number_1.place(x=25, y=288)
root_Number_2.place(x=105, y=288)
root_Number_3.place(x=185, y=288)
root_Number_4.place(x=25, y=318)
root_Number_5.place(x=105, y=318)
root_Number_6.place(x=185, y=318)
root_Number_7.place(x=25, y=348)
root_Number_8.place(x=105, y=348)
root_Number_9.place(x=185, y=348)
root_Calculate_Btn.place(x=23, y=385)
root_player_choice.place(x=15, y=430)
root_player_choice_num.place(x=200, y=430)
root_Fortune_show.place(x=15, y=455)
root_Fortune_num.place(x=200, y=455)
root_Remarks_show.place(x=15, y=480)
root_Remarks_num.place(x=200, y=480)
root_NA_show.place(x=15, y=505)
root_NA_num.place(x=200, y=505)
root_AD_show.place(x=15, y=535)
root_AD_btn.place(x=190, y=535)
root_Exit_Button.place(x=20, y=580)
root_Restart_Button.place(x=183, y=580)

Set_name()

root.mainloop()
