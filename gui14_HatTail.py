from tkinter import *
from tkinter import messagebox
import random as rd

root = Tk()

Hat_Tail = rd.choice(range(1, 6))
print(Hat_Tail)
Bat_Ball_Cchoice = ["Bat", "Ball"]
BAT_BALL_CHOICE_BY_COMP = rd.choice(Bat_Ball_Cchoice)
root_Play_Computer_Choice = [1, 2, 3, 4, 5, 6, 10]
balls_play = 0
Score = 0
LIVE = 1
scoreUpdates = 0

root.geometry("500x1000")

root.title("Hat/Tail Game")
root.iconbitmap(
    r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\GL_icon.ico")


def Name():
    if len(root_UserName_Entry.get()) == 0:
        messagebox.showerror("Sorry", "Name cannot be empty !")
    else:
        root_name_num.config(text=root_UserName_Entry.get())
        root_Hat.config(state=NORMAL)
        root_Tail.config(state=NORMAL)
        root_UserName_Entry.config(state=DISABLED)
        root_UserName_Button.config(state=DISABLED)


def TOSSdisabled():
    root_HT_1.config(state=DISABLED)
    root_HT_2.config(state=DISABLED)
    root_HT_3.config(state=DISABLED)
    root_HT_4.config(state=DISABLED)
    root_HT_5.config(state=DISABLED)
    root_HT_6.config(state=DISABLED)


def TOSSenabled():
    root_HT_1.config(state=NORMAL)
    root_HT_2.config(state=NORMAL)
    root_HT_3.config(state=NORMAL)
    root_HT_4.config(state=NORMAL)
    root_HT_5.config(state=NORMAL)
    root_HT_6.config(state=NORMAL)


def TossCalculate():
    global PHATTAILNO
    global BAT_BALL_CHOICE_BY_COMP
    if PHATTAILNO == Hat_Tail:  # Tail Winner P
        if root_Player_choice_num1.cget("text") == "Tail":
            root_Toss_Winner_num.config(text=root_UserName_Entry.get())
            root_Ball_btn.config(state=NORMAL)
            root_Bat_btn.config(state=NORMAL)
            root_Bat_Ball_Choice.config(text="Choice (P) : ")
        elif root_Computer_choice_num1.cget("text") == "Tail":
            root_Toss_Winner_num.config(text="Computer")
            root_Bat_Ball_Choice.config(text="Choice (C) : ")
            root_Bat_Ball_Choice_num.config(text=BAT_BALL_CHOICE_BY_COMP)
            root_Computer_Play_Choice.config(
                text="Computer choice ( {} ) :".format(BAT_BALL_CHOICE_BY_COMP))
            if BAT_BALL_CHOICE_BY_COMP == "Bat":
                root_Player_Play_Choice.config(text="Your choice ( Ball ) :")
                root_Bat_btn.config(relief=SOLID)
                root_Score_Play.config(text="Score ( C ) :")
                root_Balls_Play.config(text="Ball ( P )")
            else:
                root_Player_Play_Choice.config(text="Your choice ( Bat ) :")
                root_Ball_btn.config(relief=SOLID)
                root_Score_Play.config(text="Score ( P ) :")
                root_Balls_Play.config(text="Ball ( C )")
            root_Play_1.config(state=NORMAL)
            root_Play_2.config(state=NORMAL)
            root_Play_3.config(state=NORMAL)
            root_Play_4.config(state=NORMAL)
            root_Play_5.config(state=NORMAL)
            root_Play_6.config(state=NORMAL)
            root_Play_10.config(state=NORMAL)

    elif (PHATTAILNO+Hat_Tail) % 2 > 0:  # Hat Winner P
        if root_Player_choice_num1.cget("text") == "Hat":
            root_Toss_Winner_num.config(text=root_UserName_Entry.get())
            root_Ball_btn.config(state=NORMAL)
            root_Bat_btn.config(state=NORMAL)
            root_Bat_Ball_Choice.config(text="Choice (P) : ")
        elif root_Computer_choice_num1.cget("text") == "Hat":
            root_Toss_Winner_num.config(text="Computer")
            root_Bat_Ball_Choice.config(text="Choice (C) : ")
            root_Bat_Ball_Choice_num.config(text=BAT_BALL_CHOICE_BY_COMP)
            root_Play_1.config(state=NORMAL)
            root_Play_2.config(state=NORMAL)
            root_Play_3.config(state=NORMAL)
            root_Play_4.config(state=NORMAL)
            root_Play_5.config(state=NORMAL)
            root_Play_6.config(state=NORMAL)
            root_Play_10.config(state=NORMAL)
            root_Computer_Play_Choice.config(
                text="Computer choice ( {} ) :".format(BAT_BALL_CHOICE_BY_COMP))
            if BAT_BALL_CHOICE_BY_COMP == "Bat":
                root_Player_Play_Choice.config(text="Your choice ( Ball ) :")
                root_Bat_btn.config(relief=SOLID)
                root_Score_Play.config(text="Score ( C ) :")
                root_Balls_Play.config(text="Ball ( P )")
            else:
                root_Player_Play_Choice.config(text="Your choice ( Bat ) :")
                root_Ball_btn.config(relief=SOLID)
                root_Score_Play.config(text="Score ( P ) :")
                root_Balls_Play.config(text="Ball ( C )")

    elif (PHATTAILNO+Hat_Tail) % 2 == 0:  # Tail Winner P
        if root_Player_choice_num1.cget("text") == "Tail":
            root_Toss_Winner_num.config(text=root_UserName_Entry.get())
            root_Ball_btn.config(state=NORMAL)
            root_Bat_btn.config(state=NORMAL)
            root_Bat_Ball_Choice.config(text="Choice (P) : ")
        elif root_Computer_choice_num1.cget("text") == "Tail":
            root_Toss_Winner_num.config(text="Computer")
            root_Bat_Ball_Choice.config(text="Choice (C) : ")
            root_Bat_Ball_Choice_num.config(text=BAT_BALL_CHOICE_BY_COMP)
            root_Play_1.config(state=NORMAL)
            root_Play_2.config(state=NORMAL)
            root_Play_3.config(state=NORMAL)
            root_Play_4.config(state=NORMAL)
            root_Play_5.config(state=NORMAL)
            root_Play_6.config(state=NORMAL)
            root_Play_10.config(state=NORMAL)
            root_Computer_Play_Choice.config(
                text="Computer choice ( {} ) :".format(BAT_BALL_CHOICE_BY_COMP))
            if BAT_BALL_CHOICE_BY_COMP == "Bat":
                root_Player_Play_Choice.config(text="Your choice ( Ball ) :")
                root_Bat_btn.config(relief=SOLID)
                root_Score_Play.config(text="Score ( C ) :")
                root_Balls_Play.config(text="Ball ( P )")
            else:
                root_Player_Play_Choice.config(text="Your choice ( Bat ) :")
                root_Ball_btn.config(relief=SOLID)
                root_Score_Play.config(text="Score ( P ) :")
                root_Balls_Play.config(text="Ball ( C )")


def Pchoice1():
    global PHATTAILNO
    PHATTAILNO = 1
    root_Player_choice_num2.config(text="{}".format(PHATTAILNO))
    root_Computer_choice_num2.config(text="{}".format(Hat_Tail))
    root_HT_1.config(relief=SOLID)
    TOSSdisabled()
    TossCalculate()


def Pchoice2():
    global PHATTAILNO
    PHATTAILNO = 2
    root_Player_choice_num2.config(text="{}".format(PHATTAILNO))
    root_Computer_choice_num2.config(text="{}".format(Hat_Tail))
    root_HT_2.config(relief=SOLID)
    TOSSdisabled()
    TossCalculate()


def Pchoice3():
    global PHATTAILNO
    PHATTAILNO = 3
    root_Player_choice_num2.config(text="{}".format(PHATTAILNO))
    root_Computer_choice_num2.config(text="{}".format(Hat_Tail))
    root_HT_3.config(relief=SOLID)
    TOSSdisabled()
    TossCalculate()


def Pchoice4():
    global PHATTAILNO
    PHATTAILNO = 4
    root_Player_choice_num2.config(text="{}".format(PHATTAILNO))
    root_Computer_choice_num2.config(text="{}".format(Hat_Tail))
    root_HT_4.config(relief=SOLID)
    TOSSdisabled()
    TossCalculate()


def Pchoice5():
    global PHATTAILNO
    PHATTAILNO = 5
    root_Player_choice_num2.config(text="{}".format(PHATTAILNO))
    root_Computer_choice_num2.config(text="{}".format(Hat_Tail))
    root_HT_5.config(relief=SOLID)
    TOSSdisabled()
    TossCalculate()


def Pchoice6():
    global PHATTAILNO
    PHATTAILNO = 6
    root_Player_choice_num2.config(text="{}".format(PHATTAILNO))
    root_Computer_choice_num2.config(text="{}".format(Hat_Tail))
    root_HT_6.config(relief=SOLID)
    TOSSdisabled()
    TossCalculate()


def BAT_CHOICE():
    root_Bat_Ball_Choice_num.config(text="Bat")
    if root_Toss_Winner_num.cget("text") == root_UserName_Entry.get():
        root_Player_Play_Choice.config(text="Your choice ( Bat ) : ")
        root_Computer_Play_Choice.config(text="Computer choice ( Ball ) : ")
        root_Balls_Play.config(text="Balls ( C )")
        root_Score_Play.config(text="Score ( P )")
    root_Bat_btn.config(state=DISABLED)
    root_Ball_btn.config(state=DISABLED)
    root_Play_1.config(state=NORMAL)
    root_Play_2.config(state=NORMAL)
    root_Play_3.config(state=NORMAL)
    root_Play_4.config(state=NORMAL)
    root_Play_5.config(state=NORMAL)
    root_Play_6.config(state=NORMAL)
    root_Play_10.config(state=NORMAL)
    root_Bat_btn.config(relief=SOLID)


def BALL_CHOICE():
    root_Bat_Ball_Choice_num.config(text="Ball")
    if root_Toss_Winner_num.cget("text") == root_UserName_Entry.get():
        root_Player_Play_Choice.config(text="Your choice ( Ball ) : ")
        root_Computer_Play_Choice.config(text="Computer choice ( Bat ) : ")
        root_Balls_Play.config(text="Balls ( P )")
        root_Score_Play.config(text="Score ( C )")
    root_Bat_btn.config(state=DISABLED)
    root_Ball_btn.config(state=DISABLED)
    root_Play_1.config(state=NORMAL)
    root_Play_2.config(state=NORMAL)
    root_Play_3.config(state=NORMAL)
    root_Play_4.config(state=NORMAL)
    root_Play_5.config(state=NORMAL)
    root_Play_6.config(state=NORMAL)
    root_Play_10.config(state=NORMAL)
    root_Ball_btn.config(relief=SOLID)


def Hat():
    global PHAT
    global PTAIL
    global PHAT_PTAIL1
    global PHAT_PTAIL2
    PHAT = "Hat"
    PTAIL = "Tail"
    PHAT_PTAIL1 = PHAT
    PHAT_PTAIL2 = PTAIL
    root_Player_choice_num1.config(text="{}".format(PHAT))
    root_Computer_choice_num1.config(text="{}".format(PTAIL))
    root_Hat.config(state=DISABLED, relief=SOLID)
    root_Tail.config(state=DISABLED)
    TOSSenabled()


def Tail():
    global PTAIL
    global PHAT
    global PHAT_PTAIL1
    global PHAT_PTAIL2
    PTAIL = "Tail"
    PHAT = "Hat"
    PHAT_PTAIL1 = PTAIL
    PHAT_PTAIL2 = PHAT
    root_Player_choice_num1.config(text="{}".format(PTAIL))
    root_Computer_choice_num1.config(text="{}".format(PHAT))
    root_Hat.config(state=DISABLED)
    root_Tail.config(state=DISABLED, relief=SOLID)
    TOSSenabled()


def BUTTONSdisabled():
    root_Play_1.config(state=DISABLED)
    root_Play_2.config(state=DISABLED)
    root_Play_3.config(state=DISABLED)
    root_Play_4.config(state=DISABLED)
    root_Play_5.config(state=DISABLED)
    root_Play_6.config(state=DISABLED)
    root_Play_10.config(state=DISABLED)


def BUTTONSenabled():
    root_Play_1.config(state=NORMAL)
    root_Play_2.config(state=NORMAL)
    root_Play_3.config(state=NORMAL)
    root_Play_4.config(state=NORMAL)
    root_Play_5.config(state=NORMAL)
    root_Play_6.config(state=NORMAL)
    root_Play_10.config(state=NORMAL)


def turn1():
    global scoreUpdates
    global LIVE
    if root_Player_Play_Choice.cget("text") == "Your choice ( Bat ) : ":
        scoreUpdates = scoreUpdates + \
            int(root_Player_Play_Choice_num.cget("text"))
        root_Score_Play_num.config(text=scoreUpdates)
        if root_Player_Play_Choice_num.cget("text") == root_Computer_Play_Choice_num.cget("text") and root_Player_Play_Choice_num.cget("text") > 0 and root_Computer_Play_Choice_num.cget("text") > 0:
            root_Target_Play.config(text="Target (P): ")
            root_Target_Play_num.config(text=scoreUpdates)
            BUTTONSdisabled()
            scoreUpdates = 0
            root_Score_Play_num.config(text=scoreUpdates)
            root_Score_Play.config(text="Score ( C ) :")
            root_Player_Play_Choice.config(text="Your choice ( Ball ) : ")
            root_Computer_Play_Choice.config(text="Computer choice ( Bat ) : ")
            turn2()
            LIVE = LIVE + 1
            root.after(5000, BUTTONSenabled)
    elif root_Player_Play_Choice.cget("text") == "Your choice ( Ball ) : ":
        scoreUpdates = scoreUpdates + \
            int(root_Player_Play_Choice_num.cget("text"))
        root_Score_Play_num.config(text=scoreUpdates)
        if root_Player_Play_Choice_num.cget("text") == root_Computer_Play_Choice_num.cget("text") and root_Player_Play_Choice_num.cget("text") > 0 and root_Computer_Play_Choice_num.cget("text") > 0:
            root_Target_Play.config(text="Target (C): ")
            root_Target_Play_num.config(text=scoreUpdates)
            BUTTONSdisabled()
            scoreUpdates = 0
            root_Score_Play_num.config(text=scoreUpdates)
            root_Score_Play.config(text="Score ( P ) :")
            root_Player_Play_Choice.config(text="Your choice ( Bat ) : ")
            root_Computer_Play_Choice.config(
                text="Computer choice ( Ball ) : ")
            turn2()
            LIVE = LIVE + 1
            root.after(5000, BUTTONSenabled)


def turn2():
    global scoreUpdates
    print("Its running now")
    if root_Player_Play_Choice.cget("text") == "Your choice ( Ball ) : ":
        scoreUpdates = scoreUpdates + \
            int(root_Computer_Play_Choice_num.cget("text"))
        root_Score_Play_num.config(text=scoreUpdates)
        if root_Player_Play_Choice_num.cget("text") == root_Computer_Play_Choice_num.cget("text") and root_Player_Play_Choice_num.cget("text") > 0 and root_Computer_Play_Choice_num.cget("text") > 0:
            BUTTONSdisabled()
            root_WINNER_Play_num.config(text=root_UserName_Entry.get())
        elif root_Computer_Play_Choice_num.cget("text") > root_Target_Play_num.cget("text"):
            root_WINNER_Play_num.config(text="Computer")
            BUTTONSdisabled()
    elif root_Player_Play_Choice.cget("text") == "Your choice ( Bat ) : ":
        scoreUpdates = scoreUpdates + \
            int(root_Computer_Play_Choice_num.cget("text"))
        root_Score_Play_num.config(text=scoreUpdates)
        if root_Player_Play_Choice_num.cget("text") == root_Computer_Play_Choice_num.cget("text") and root_Player_Play_Choice_num.cget("text") > 0 and root_Computer_Play_Choice_num.cget("text") > 0:
            root_WINNER_Play_num.config(text="Computer")
            BUTTONSdisabled()
        elif root_Player_Play_Choice_num.cget("text") > root_Target_Play_num.cget("text"):
            root_WINNER_Play_num.config(text=root_UserName_Entry.get())
            BUTTONSdisabled()


def PlaySystem():
    if LIVE == 1:
        turn1()
    elif LIVE == 2:
        turn2()
    print(LIVE)


def Play1():
    global root_Play_Computer_Choice_btn
    global root_Play_Computer_Choice_btn
    root_Player_Play_Choice_num.config(text=1)
    root_Play_Computer_Choice_btn = rd.choice(root_Play_Computer_Choice)
    root_Computer_Play_Choice_num.config(text=root_Play_Computer_Choice_btn)
    PlaySystem()


def Play2():
    global root_Play_Computer_Choice_btn
    root_Player_Play_Choice_num.config(text=2)
    root_Computer_Play_Choice_num.config(
        text=rd.choice(root_Play_Computer_Choice))
    PlaySystem()


def Play3():
    global root_Play_Computer_Choice_btn
    root_Player_Play_Choice_num.config(text=3)
    root_Play_Computer_Choice_btn = rd.choice(root_Play_Computer_Choice)
    root_Computer_Play_Choice_num.config(text=root_Play_Computer_Choice_btn)
    PlaySystem()


def Play4():
    global root_Play_Computer_Choice_btn
    root_Player_Play_Choice_num.config(text=4)
    root_Play_Computer_Choice_btn = rd.choice(root_Play_Computer_Choice)
    root_Computer_Play_Choice_num.config(text=root_Play_Computer_Choice_btn)
    PlaySystem()


def Play5():
    global root_Play_Computer_Choice_btn
    root_Player_Play_Choice_num.config(text=5)
    root_Play_Computer_Choice_btn = rd.choice(root_Play_Computer_Choice)
    root_Computer_Play_Choice_num.config(text=root_Play_Computer_Choice_btn)
    PlaySystem()


def Play6():
    global root_Play_Computer_Choice_btn
    root_Player_Play_Choice_num.config(text=6)
    root_Play_Computer_Choice_btn = rd.choice(root_Play_Computer_Choice)
    root_Computer_Play_Choice_num.config(text=root_Play_Computer_Choice_btn)
    PlaySystem()


def Play10():
    global root_Play_Computer_Choice_btn
    root_Player_Play_Choice_num.config(text=10)
    root_Play_Computer_Choice_btn = rd.choice(root_Play_Computer_Choice)
    root_Computer_Play_Choice_num.config(text=root_Play_Computer_Choice_btn)
    PlaySystem()


root_Menu_Back = Button(root, text="<--", command="")

root_heading = Label(root, text="Hat/Tail", font=["Bookman Old Style", 20])
root_Info = Button(root, text="ⓘ", font=["times"], relief=FLAT)

root_UserName = Label(root, text="Username : ")
root_UserName_Entry = Entry(root)
root_UserName_Button = Button(root, text="Ok", command=Name)

root_name = Label(root, text="Player Name : ")
root_name_num = Label(root, text="Name")

root_heading_Toss = Label(root, text="Toss : ", font="times 13")

root_Hat = Button(root, text="HAT", bd=2, relief=RAISED,
                  state=DISABLED, command=Hat)
root_Tail = Button(root, text="TAIL", bd=2, relief=RAISED,
                   state=DISABLED, command=Tail)

root_HT_1 = Button(root, text=1, width=3, state=DISABLED, command=Pchoice1)
root_HT_2 = Button(root, text=2, width=3, state=DISABLED, command=Pchoice2)
root_HT_3 = Button(root, text=3, width=3, state=DISABLED, command=Pchoice3)
root_HT_4 = Button(root, text=4, width=3, state=DISABLED, command=Pchoice4)
root_HT_5 = Button(root, text=5, width=3, state=DISABLED, command=Pchoice5)
root_HT_6 = Button(root, text=6, width=3, state=DISABLED, command=Pchoice6)

root_Frame_Toss1 = Frame(root)
root_Player_choice = Label(root, text="Your Choice : ")
root_Player_choice_num1 = Label(root_Frame_Toss1, text="--")
root_Exclamation1 = Label(root_Frame_Toss1, text="/")
root_Player_choice_num2 = Label(root_Frame_Toss1, text="--")

root_Frame_Toss2 = Frame(root)
root_Computer_choice = Label(root, text="Computer Choice : ")
root_Computer_choice_num1 = Label(root_Frame_Toss2, text="--")
root_Exclamation2 = Label(root_Frame_Toss2, text="/")
root_Computer_choice_num2 = Label(root_Frame_Toss2, text="--")

root_Toss_Winner = Label(root, text="Toss Winner : ")
root_Toss_Winner_num = Label(root, text="--:--")

root_heading_Bat_Ball = Label(root, text="Choose : ", font="times 13")

root_Bat_btn = Button(root, text="Bat", bd=2, relief=RAISED,
                      state=DISABLED, width=5, command=BAT_CHOICE)
root_Ball_btn = Button(root, text="Ball", bd=2, relief=RAISED,
                       state=DISABLED, width=5, command=BALL_CHOICE)

root_Bat_Ball_Choice = Label(root, text="Choice (P/C) : ")
root_Bat_Ball_Choice_num = Label(root, text="--:--")

root_heading_Play = Label(root, text="Play : ", font="times 13")

root_Play_1 = Button(root, text=1, width=5, state=DISABLED, command=Play1)
root_Play_2 = Button(root, text=2, width=5, state=DISABLED, command=Play2)
root_Play_3 = Button(root, text=3, width=5, state=DISABLED, command=Play3)
root_Play_4 = Button(root, text=4, width=5, state=DISABLED, command=Play4)
root_Play_5 = Button(root, text=5, width=5, state=DISABLED, command=Play5)
root_Play_6 = Button(root, text=6, width=5, state=DISABLED, command=Play6)
root_Play_10 = Button(root, text=10, width=5, state=DISABLED, command=Play10)


root_Player_Play_Choice = Label(root, text="Your choice : ")
root_Computer_Play_Choice = Label(root, text="Computer choice : ")
root_Balls_Play = Label(root, text="Balls (P/C) : ")
root_Score_Play = Label(root, text="Score (P/C) : ")
root_Remarks_Play = Label(root, text="Remarks : ")
root_Target_Play = Label(root, text="Target (P/C): ")
root_WINNER_Play = Label(root, text="WINNER : ")

root_Player_Play_Choice_num = Label(root, text="--:--")
root_Computer_Play_Choice_num = Label(root, text="--:--")
root_Balls_Play_num = Label(root, text="--:--")
root_Score_Play_num = Label(root, text=0)
root_Remarks_Play_num = Label(root, text="--:--")
root_Target_Play_num = Label(root, text=0)
root_WINNER_Play_num = Label(root, text="--:--")

root_Menu_Back.place(x=1, y=1)
root_heading.place(x=100, y=1)
root_Info.place(x=215, y=9)
root_UserName.place(x=15, y=60)
root_UserName_Entry.place(x=100, y=62)
root_UserName_Button.place(x=230, y=58)
root_name.place(x=15, y=95)
root_name_num.place(x=140, y=95)
root_heading_Toss.place(x=15, y=125)
root_Hat.place(x=35, y=155)
root_Tail.place(x=140, y=155)
root_HT_1.place(x=35, y=190)
root_HT_2.place(x=90, y=190)
root_HT_3.place(x=140, y=190)
root_HT_4.place(x=35, y=220)
root_HT_5.place(x=90, y=220)
root_HT_6.place(x=140, y=220)
root_Player_choice.place(x=25, y=260)
root_Frame_Toss1.place(x=142, y=260)
root_Player_choice_num1.grid(row=0, column=0)
root_Exclamation1.grid(row=0, column=1)
root_Player_choice_num2.grid(row=0, column=2)
root_Computer_choice.place(x=25, y=285)
root_Frame_Toss2.place(x=142, y=285)
root_Computer_choice_num1.grid(row=0, column=0)
root_Exclamation2.grid(row=0, column=1)
root_Computer_choice_num2.grid(row=0, column=2)
root_Toss_Winner.place(x=25, y=310)
root_Toss_Winner_num.place(x=142, y=310)
root_heading_Bat_Ball.place(x=15, y=340)
root_Bat_btn.place(x=35, y=370)
root_Ball_btn.place(x=140, y=370)
root_Bat_Ball_Choice.place(x=25, y=410)
root_Bat_Ball_Choice_num.place(x=142, y=410)
root_heading_Play.place(x=15, y=440)
root_Play_1.place(x=35, y=470)
root_Play_2.place(x=90, y=470)
root_Play_3.place(x=140, y=470)
root_Play_4.place(x=35, y=500)
root_Play_5.place(x=90, y=500)
root_Play_6.place(x=140, y=500)
root_Play_10.place(x=90, y=530)
root_Player_Play_Choice.place(x=25, y=570)
root_Player_Play_Choice_num.place(x=165, y=570)
root_Computer_Play_Choice.place(x=25, y=595)
root_Computer_Play_Choice_num.place(x=165, y=595)
root_Balls_Play.place(x=25, y=620)
root_Balls_Play_num.place(x=165, y=620)
root_Score_Play.place(x=25, y=645)
root_Score_Play_num.place(x=165, y=645)
root_Remarks_Play.place(x=25, y=670)
root_Remarks_Play_num.place(x=165, y=670)
root_Target_Play.place(x=25, y=695)
root_Target_Play_num.place(x=165, y=695)
root_WINNER_Play.place(x=25, y=720)
root_WINNER_Play_num.place(x=165, y=720)

root.mainloop()
