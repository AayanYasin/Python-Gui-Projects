from tkinter import *
import random as rd
import time as t
import os
import sys


root = Tk()

User_Name1 = "Player 1"
User_Name2 = "Player 2"
RPS1 = 0
RPS2 = 0
score = None
ButtonClickedp1 = None
ButtonClickedp2 = None

root.title("Rock, Paper, Scissors Game")

root.geometry("320x540")
root.minsize(320, 540)
root.iconbitmap(
    r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\GL_icon.ico")


def Set_name():
    if os.path.isfile(r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\server1.py"):
        try:
            import server1
        except ModuleNotFoundError:
            pass
        root_Name_Entry1.insert(0, server1.Username)
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
    print("User set score limit to {}".format(score1))


def TName1():
    global User_Name1
    User_Name1 = root_Name_Entry1.get()
    # root_Winner1.config(text=User_Name1)
    root_Set_Name_Str1.config(text=User_Name1)
    root_Player1_text.config(text=User_Name1)
    root_Name_Entry1.config(state=DISABLED)
    root_Name_button1.config(state=DISABLED)
    print("Player 1 named him/herself as {}".format(User_Name1))


def TName2():
    global User_Name2
    User_Name2 = root_Name_Entry2.get()
    # root_Winner1.config(text=User_Name2)
    root_Set_Name_Str2.config(text=User_Name2)
    root_Player2_text.config(text=User_Name2)
    root_Name_Entry2.config(state=DISABLED)
    root_Name_button2.config(state=DISABLED)
    print("Player 2 named him/herself as {}".format(User_Name2))


def DisableButtonp1():
    root_rock1.config(state=DISABLED)
    root_paper2.config(state=DISABLED)
    root_scissor3.config(state=DISABLED)
    root_rock4.config(state=NORMAL)
    root_paper5.config(state=NORMAL)
    root_scissor6.config(state=NORMAL)


def DisableButtonp2():
    root_rock4.config(state=DISABLED)
    root_paper5.config(state=DISABLED)
    root_scissor6.config(state=DISABLED)
    root_rock1.config(state=NORMAL)
    root_paper2.config(state=NORMAL)
    root_scissor3.config(state=NORMAL)


def click1():
    global p1r
    global ButtonClickedp1
    p1r = "rock"
    ButtonClickedp1 = p1r
    DisableButtonp1()
    root_Player1_text.config(fg="black")
    root_Player2_text.config(fg="green")
    root_player1ChoiceAnswer.config(text="--:--")
    root_player2ChoiceAnswer.config(text="--:--")
    print(ButtonClickedp1)


def click2():
    global p1p
    global ButtonClickedp1
    p1p = "paper"
    ButtonClickedp1 = p1p
    DisableButtonp1()
    root_Player1_text.config(fg="black")
    root_Player2_text.config(fg="green")
    root_player1ChoiceAnswer.config(text="--:--")
    root_player2ChoiceAnswer.config(text="--:--")
    print(ButtonClickedp1)


def click3():
    global p1s
    global ButtonClickedp1
    p1s = "scissor"
    ButtonClickedp1 = p1s
    DisableButtonp1()
    root_Player1_text.config(fg="black")
    root_Player2_text.config(fg="green")
    root_player1ChoiceAnswer.config(text="--:--")
    root_player2ChoiceAnswer.config(text="--:--")
    print(ButtonClickedp1)


def click4():
    global p2r
    global ButtonClickedp2
    p2r = "rock"
    ButtonClickedp2 = p2r
    root_rock4.config(state=DISABLED)
    root_paper5.config(state=DISABLED)
    root_scissor6.config(state=DISABLED)
    root_Player2_text.config(fg="black")
    root_Calculate_Answer.config(state=NORMAL)
    root_Calculate_Answer.config(fg="green")
    print(ButtonClickedp2)


def click5():
    global p2p
    global ButtonClickedp2
    p2p = "paper"
    ButtonClickedp2 = p2p
    root_rock4.config(state=DISABLED)
    root_paper5.config(state=DISABLED)
    root_scissor6.config(state=DISABLED)
    root_Player2_text.config(fg="black")
    root_Calculate_Answer.config(state=NORMAL)
    root_Calculate_Answer.config(fg="green")
    print(ButtonClickedp2)


def click6():
    global p2s
    global ButtonClickedp2
    p2s = "scissor"
    ButtonClickedp2 = p2s
    root_rock4.config(state=DISABLED)
    root_paper5.config(state=DISABLED)
    root_scissor6.config(state=DISABLED)
    root_Player2_text.config(fg="black")
    root_Calculate_Answer.config(state=NORMAL)
    root_Calculate_Answer.config(fg="green")
    print(ButtonClickedp2)


def CalculateResult():
    global RPS1
    global RPS2
    root_player1ChoiceAnswer.config(text=ButtonClickedp1)
    root_player2ChoiceAnswer.config(text=ButtonClickedp2)
    if ButtonClickedp1 == ButtonClickedp2:
        root_Winner1.config(text="Tied")
        root_Winner1.config(fg="black")
    elif ButtonClickedp1 == "rock" and ButtonClickedp2 == "scissor" or ButtonClickedp1 == "scissor" and ButtonClickedp2 == "paper" or ButtonClickedp1 == "paper" and ButtonClickedp2 == "rock":
        root_Winner1.config(text=User_Name1)
        root_Winner1.config(fg="green")
        RPS1 += 1
        root_Score_Player1_Num.config(text=RPS1)
    elif ButtonClickedp2 == "rock" and ButtonClickedp1 == "scissor" or ButtonClickedp2 == "scissor" and ButtonClickedp1 == "paper" or ButtonClickedp2 == "paper" and ButtonClickedp1 == "rock":
        root_Winner1.config(text=User_Name2)
        root_Winner1.config(fg="green")
        RPS2 += 1
        root_Score_Player2_Num.config(text=RPS2)
    DisableButtonp2()
    remarks()
    finish123()
    root_Calculate_Answer.config(fg="black")
    root_Calculate_Answer.config(state=DISABLED)


def restart():
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\gui10_rps_PvsP.py")
    root.destroy()


def exitgame():
    # WE can use both of these to close this program
    # root.destroy() # This can also be used
    sys.exit()  # I will use this for now


def BackMenu2():
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\gui11_rps_Menu.py")
    root.destroy()


def remarks():
    global score1
    if RPS1 == RPS2 and RPS1 > 0 and RPS2 > 0:
        root_Remarks_Answer.config(text="You both have same score.")
    elif RPS1 > RPS2:
        root_Remarks_Answer.config(
            text="Yahoo! {} is leading.".format(User_Name1))
    elif RPS2 > RPS1:
        root_Remarks_Answer.config(
            text="Yahoo! {} is leading.".format(User_Name2))
    elif RPS1 == score1 or RPS2 == score1:
        root_Remarks_Answer.config(
            text="Game ended ! Press restart button to play again.")


def disabled():
    root_rock1.config(state=DISABLED)
    root_paper2.config(state=DISABLED)
    root_scissor3.config(state=DISABLED)
    root_rock4.config(state=DISABLED)
    root_paper5.config(state=DISABLED)
    root_scissor6.config(state=DISABLED)
    root_Name_Entry1.config(state=DISABLED)
    root_Name_button1.config(state=DISABLED)
    root_Name_Entry2.config(state=DISABLED)
    root_Name_button2.config(state=DISABLED)
    root_Score_Set_Button.config(state=DISABLED)
    root_Score_Set_Entry.config(state=DISABLED)
    root_Calculate_Answer.config(state=DISABLED)


def finish123():
    global score1
    if RPS1 == score1:
        root_Final_Winner_Num.config(text=User_Name1)
        root_Remarks_Answer.config(text="Game ended !")
        root_Final_Winner_Num.config(
            fg="black", bg="lightgreen", bd=1, relief=SUNKEN, padx=3, pady=2)
        disabled()
    elif RPS2 == score1:
        root_Final_Winner_Num.config(text=User_Name2)
        root_Remarks_Answer.config(text="Game ended !")
        root_Final_Winner_Num.config(
            fg="black", bg="lightgreen", bd=1, relief=SUNKEN, padx=3, pady=2)
        disabled()


root_Heading = Label(root, text="Rock, Paper, Scissor Game",
                     fg="white", bg="green", bd=3, relief=SUNKEN, font="bold")

root_Exit_Back_Arrow2 = Button(
    root, text="<--", anchor=CENTER, bd=2, relief=RIDGE, command=BackMenu2)

root_Name1 = Label(root, text="User Name 1 : ")
root_Name_Entry1 = Entry(root)
root_Name_button1 = Button(root, text="OK", command=TName1)

root_Name2 = Label(root, text="User Name 2 : ")
root_Name_Entry2 = Entry(root)
root_Name_button2 = Button(root, text="OK", command=TName2)

root_Score_Set = Label(root, text="Set Score Limit : ")
root_Score_Set_Entry = Entry(root)
root_Score_Set_Button = Button(root, text="Set", command=ScoreSet)

root_Set_Name1 = Label(root, text="User Name 1 : ")
root_Set_Name_Str1 = Label(root, text="Name")

root_Set_Name2 = Label(root, text="User Name 2 : ")
root_Set_Name_Str2 = Label(root, text="Name")

root_SLimit = Label(root, text="Score Limit : ")
root_SLimit_Num = Label(root, text="Score")

root_Player1_text = Label(root, text="Player 1", fg="green")
root_Player2_text = Label(root, text="Player 2")

root_rock1 = Button(root, text="Rock", bg="pink", command=click1)
root_paper2 = Button(root, text="Paper", bg="yellow", command=click2)
root_scissor3 = Button(root, text="Scissor", bg="silver", command=click3)

root_rock4 = Button(root, text="Rock", bg="pink",
                    state=DISABLED, command=click4)
root_paper5 = Button(root, text="Paper", bg="yellow",
                     state=DISABLED, command=click5)
root_scissor6 = Button(root, text="Scissor", bg="silver",
                       state=DISABLED, command=click6)

root_playerChoice = Label(root, text="Choosed : ")
root_ComputerChoice = Label(root, text="Choosed : ")

root_player1ChoiceAnswer = Label(root, text="--:--")
root_player2ChoiceAnswer = Label(root, text="--:--")

root_Calculate_Answer = Button(root, text="Calculate", width=28, bd=3, relief=RIDGE,
                               bg="yellow", anchor=CENTER, state=DISABLED, command=CalculateResult)

root_Winner = Label(root, text="Win : ")
root_Winner1 = Label(root, text="--:--", fg="black")

root_Score_Player1 = Label(root, text="Player 1 Score : ")
root_Score_Player1_Num = Label(root, text=RPS1)
root_Score_Player2 = Label(root, text="Player 2 Score : ")
root_Score_Player2_Num = Label(root, text=RPS2)

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

root_Exit_Back_Arrow2.place(x=1, y=1)
root_Heading.grid(row=0, column=0, columnspan=3)
root_Name1.grid(row=1, column=0)
root_Name_Entry1.grid(row=1, column=1)
root_Name_button1.grid(row=1, column=2)
root_Name2.grid(row=2, column=0)
root_Name_Entry2.grid(row=2, column=1)
root_Name_button2.grid(row=2, column=2)
root_Score_Set.grid(row=3, column=0)
root_Score_Set_Entry.grid(row=3, column=1)
root_Score_Set_Button.grid(row=3, column=2)
root_Set_Name1.grid(row=4, column=0)
root_Set_Name_Str1.grid(row=4, column=1)
root_Set_Name2.grid(row=5, column=0)
root_Set_Name_Str2.grid(row=5, column=1)
root_SLimit.grid(row=6, column=0)
root_SLimit_Num.grid(row=6, column=1)
root_Player1_text.grid(row=7, column=0)
root_Player2_text.grid(row=7, column=1)
root_rock1.grid(row=8, column=0)
root_rock4.grid(row=8, column=1)
root_paper2.grid(row=9, column=0)
root_paper5.grid(row=9, column=1)
root_scissor3.grid(row=10, column=0)
root_scissor6.grid(row=10, column=1)
root_playerChoice.grid(row=11, column=0)
root_ComputerChoice.grid(row=11, column=1)
root_player1ChoiceAnswer.grid(row=12, column=0)
root_player2ChoiceAnswer.grid(row=12, column=1)
root_Calculate_Answer.grid(row=13, columnspan=2)
root_Winner.grid(row=14, column=0)
root_Winner1.grid(row=14, column=1)
root_Remarks.grid(row=15, column=0)
root_Remarks_Answer.grid(row=15, column=1)
root_Score_Player1.grid(row=16, column=0)
root_Score_Player1_Num.grid(row=16, column=1)
root_Score_Player2.grid(row=17, column=0)
root_Score_Player2_Num.grid(row=17, column=1)
root_Final_Winner.grid(row=18, column=0)
root_Final_Winner_Num.grid(row=18, column=1)
root_Exit_Button.grid(row=19, columnspan=1)
root_Restart_Button.grid(row=19, column=1)
root_Author1.grid(row=20, column=0)
root_Author2.grid(row=21, column=0)
root_Author3.grid(row=22, column=0)

Set_name()

root.mainloop()
