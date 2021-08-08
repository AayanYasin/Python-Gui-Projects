from tkinter import *
import random as rd
import time as t
import os
import sys


root = Tk()

ComputersrpcChoice = ["Snake", "Gun", "Water"]
User_Name = "Player"
RPS = 0
RCS = 0
score = None
width = 6,
root.title("Snake, Water, Gun Game")
root.iconbitmap(
    r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\GL_icon.ico")

root.geometry("330x440")
root.minsize(320, 440)
root.iconbitmap(
    r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\GL_icon.ico")


def Set_name():
    if os.path.isfile(r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\server1.py"):
        try:
            import server1
        except ModuleNotFoundError:
            pass
        root_Name_Entry.insert(0, server1.Username)
        print("File exist")
    else:
        print("File do not exist")


def ScoreSet():
    global score
    global score1
    score = root_Score_Set_Entry.get()
    score1 = int(score)
    root_SLimit_Num.config(text=score1)
    root_Score_Set_Entry.config(state=DISABLED)
    root_Score_Set_Button.config(state=DISABLED)
    print(score1)


def TName():
    global User_Name
    User_Name = root_Name_Entry.get()
    # root_Winner1.config(text=User_Name)
    root_Set_Name_Str.config(text=User_Name)
    root_Name_Entry.config(state=DISABLED)
    root_Name_button.config(state=DISABLED)
    print("Player named him/herself as {}".format(User_Name))


def PCR():
    global RPS
    global RCS
    root_playerChoiceAnswer.config(text="Snake")
    CC1 = rd.choice(ComputersrpcChoice)
    root_ComputerChoiceAnswer.config(text=CC1)
    print("Player Choosed : Snake")
    print("Computer choosed : ", CC1)
    if CC1 == "Snake":
        root_Winner1.config(text="Tie")
        root_Winner1.config(fg="black")
        # print("Game Tied")
    elif CC1 == "Water":
        root_Winner1.config(text=User_Name)
        root_Winner1.config(fg="green")
        # print("Player Won")
        RPS += 1
        root_Score_Player_Num.config(text=RPS)
    elif CC1 == "Gun":
        root_Winner1.config(text="Computer")
        root_Winner1.config(fg="red")
        # print("Computer Won")
        RCS += 1
        root_Score_Computer_Num.config(text=RCS)
    remarks()
    finish123()


def PCP():
    global RPS
    global RCS
    root_playerChoiceAnswer.config(text="Gun")
    CC2 = rd.choice(ComputersrpcChoice)
    root_ComputerChoiceAnswer.config(text=CC2)
    print("Computer choosed : ", CC2)
    print("Player Choosed : Gun")
    if CC2 == "Gun":
        root_Winner1.config(text="Tie")
        root_Winner1.config(fg="black")
        # print("Game Tied")
    elif CC2 == "Snake":
        root_Winner1.config(text=User_Name)
        root_Winner1.config(fg="green")
        # print("Player Won")
        RPS += 1
        root_Score_Player_Num.config(text=RPS)
    elif CC2 == "Water":
        root_Winner1.config(text="Computer")
        root_Winner1.config(fg="red")
        # print("Computer Won")
        RCS += 1
        root_Score_Computer_Num.config(text=RCS)
    remarks()
    finish123()


def PCS():
    global RPS
    global RCS
    root_playerChoiceAnswer.config(text="Water")
    CC3 = rd.choice(ComputersrpcChoice)
    root_ComputerChoiceAnswer.config(text=CC3)
    print("Player Choosed : Water")
    print("Computer choosed : ", CC3)
    if CC3 == "Water":
        root_Winner1.config(text="Tie")
        root_Winner1.config(fg="black")
        # print("Game Tied")
    elif CC3 == "Gun":
        root_Winner1.config(text=User_Name)
        root_Winner1.config(fg="green")
        # print("Player Won")
        RPS += 1
        root_Score_Player_Num.config(text=RPS)
    elif CC3 == "Snake":
        root_Winner1.config(text="Computer")
        root_Winner1.config(fg="red")
        # print("Computer Won")
        RCS += 1
        root_Score_Computer_Num.config(text=RCS)
    remarks()
    finish123()


def restart():
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\gui17_SWG_PvsC.py")
    root.destroy()


def exitgame():
    # WE can use both of these to close this program
    # root.destroy() # This can also be used
    sys.exit()  # I will use this for now


def BackMenu1():
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\gui18_SWG_Menu.py")
    root.destroy()


def remarks():
    if RPS == RCS and RPS > 0 and RCS > 0:
        root_Remarks_Answer.config(text="You both have same score.")
    elif RPS > RCS:
        root_Remarks_Answer.config(text="Yahoo! You are leading.")
    elif RCS > RPS:
        root_Remarks_Answer.config(text="Oops! Computer is leading.")


def disabled():
    root_rock.config(state=DISABLED)
    root_Gun.config(state=DISABLED)
    root_scissor.config(state=DISABLED)
    root_Name_Entry.config(state=DISABLED)
    root_Name_button.config(state=DISABLED)
    root_Score_Set_Button.config(state=DISABLED)
    root_Score_Set_Entry.config(state=DISABLED)


def finish123():
    global score1
    if RPS == score1:
        root_Final_Winner_Num.config(text=User_Name)
        root_Remarks_Answer.config(text="Game ended !")
        root_Final_Winner_Num.config(
            fg="black", bg="lightgreen", bd=1, relief=SUNKEN, padx=3, pady=2)
        disabled()
    elif RCS == score1:
        root_Final_Winner_Num.config(text="Computer")
        root_Remarks_Answer.config(text="Game ended !")
        root_Final_Winner_Num.config(
            fg="black", bg="orangered", bd=1, relief=SUNKEN, padx=3, pady=2)
        disabled()


root_Heading = Label(root, text="Snake, Gun, Water Game",
                     fg="white", bg="green", bd=3, relief=SUNKEN, font="bold")

root_Exit_Back_Arrow1 = Button(
    root, text="<--", anchor=CENTER, bd=2, relief=RIDGE, command=BackMenu1)

root_Name = Label(root, text="User Name : ")
root_Name_Entry = Entry(root)
root_Name_button = Button(root, text="OK", command=TName)

root_Score_Set = Label(root, text="Set Score Limit : ")
root_Score_Set_Entry = Entry(root)
root_Score_Set_Button = Button(root, text="Set", command=ScoreSet)

root_Set_Name = Label(root, text="User Name : ")
root_Set_Name_Str = Label(root, text="Name")

root_SLimit = Label(root, text="Score Limit : ")
root_SLimit_Num = Label(root, text="Score")

root_rock = Button(root, text="Snake", bg="pink", width=6, command=PCR)
root_Gun = Button(root, text="Gun", bg="yellow", width=6, command=PCP)
root_scissor = Button(root, text="Water", bg="silver", width=6, command=PCS)

root_arrow1 = Label(root, text="<--")
root_arrow2 = Label(root, text="<--")
root_arrow3 = Label(root, text="<--")

root_playerChoice = Label(root, text="You choosed : ")
root_ComputerChoice = Label(root, text="Computer choosed : ")

root_playerChoiceAnswer = Label(root, text="--:--")
root_ComputerChoiceAnswer = Label(root, text="--:--")

root_Winner = Label(root, text="Winner : ")
root_Winner1 = Label(root, text="--:--", fg="black")

root_Score_Player = Label(root, text="Player Score : ")
root_Score_Player_Num = Label(root, text=RPS)
root_Score_Computer = Label(root, text="Computer Score : ")
root_Score_Computer_Num = Label(root, text=RCS)

root_Remarks = Label(root, text="Remarks : ")
root_Remarks_Answer = Label(root, text="--:--")

root_Exit_Button = Button(root, text="Exit", bg="red",
                          fg="white", bd=2, relief=SOLID, width=6, command=exitgame)
root_Restart_Button = Button(root, text="Restart", bg="red", fg="white",
                             bd=2, relief=SOLID, justify=LEFT, width=7, command=restart)

root_Final_Winner = Label(root, text="WINNER : ")
root_Final_Winner_Num = Label(root, text="?")

root_Author1 = Label(root, text="Made by Aayan Yasin", font="ariel 10 italic")
root_Author2 = Label(root, text="Reuse not allowed      ",
                     font="ariel 10 italic")
root_Author3 = Label(root, text="Copyright not allowed  ",
                     font="ariel 10 italic")

root_Exit_Back_Arrow1.place(x=1, y=1)
root_Heading.grid(row=0, column=0, columnspan=3)
root_Name.grid(row=1, column=0)
root_Name_Entry.grid(row=1, column=1)
root_Name_button.grid(row=1, column=2)
root_Score_Set.grid(row=2, column=0)
root_Score_Set_Entry.grid(row=2, column=1)
root_Score_Set_Button.grid(row=2, column=2)
root_Set_Name.grid(row=3, column=0)
root_Set_Name_Str.grid(row=3, column=1)
root_SLimit.grid(row=4, column=0)
root_SLimit_Num.grid(row=4, column=1)
root_rock.grid(row=5, column=0)
root_arrow1.grid(row=5, column=1)
root_Gun.grid(row=6, column=0)
root_arrow2.grid(row=6, column=1)
root_scissor.grid(row=7, column=0)
root_arrow3.grid(row=7, column=1)
root_playerChoice.grid(row=8, column=0)
root_playerChoiceAnswer.grid(row=8, column=1)
root_ComputerChoice.grid(row=9, column=0)
root_ComputerChoiceAnswer.grid(row=9, column=1)
root_Winner.grid(row=10, column=0)
root_Winner1.grid(row=10, column=1)
root_Remarks.grid(row=11, column=0)
root_Remarks_Answer.grid(row=11, column=1)
root_Score_Player.grid(row=12, column=0)
root_Score_Player_Num.grid(row=12, column=1)
root_Score_Computer.grid(row=13, column=0)
root_Score_Computer_Num.grid(row=13, column=1)
root_Final_Winner.grid(row=14, column=0)
root_Final_Winner_Num.grid(row=14, column=1)
root_Exit_Button.grid(row=15, columnspan=1)
root_Restart_Button.grid(row=15, column=1)
root_Author1.grid(row=16, column=0)
root_Author2.grid(row=17, column=0)
root_Author3.grid(row=18, column=0)

Set_name()

root.mainloop()
