from tkinter import *
import os
import time as t
import sys
import random as rd

root = Tk()

Words = ["Brown", "Black", "Blue", "Peach",
         "Grey", "Maroon", "Magenta", "Cyan"]
Colors = ["red", "green", "yellow", "orange", "purple", "pink"]

correct = 0
incorrect = 0
timerNUM = 60
TIMERNUMBER = 1000

root.geometry("290x270")
root.minsize(290, 270)
root.iconbitmap(
    r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\GL_icon.ico")


def Timer():
    global timerNUM
    global TIMERNUMBER
    global correct
    global incorrect
    root_time_num.config(text="{}s".format(timerNUM))
    root_time_num.after(TIMERNUMBER, Timer)
    timerNUM -= 1
    if root_time_num.cget("text") == "{}s".format(0):
        root_Entry_Ans.config(state=DISABLED)
        root_Entry_Ans_Button.config(state=DISABLED)
        root_Text.config(text="ENDED", fg="black")
        TIMERNUMBER = 0
        if correct == 0:
            root_Score_Text_num.config(text=0)
        elif incorrect == 0:
            root_Score_Text_num.config(text=correct*10)
        elif correct > incorrect:
            root_Score_Text_num.config(text=(correct/incorrect)*10)
        elif incorrect > correct:
            root_Score_Text_num.config(text=(incorrect/correct)*10)
        elif correct == incorrect and correct != 0 and incorrect != 0:
            root_Score_Text_num.config(
                text=(correct*incorrect)/(correct+incorrect))


def color():
    global word
    global color
    global correct
    global incorrect
    if root_Entry_Ans_Button.cget("text") == "Start":
        root_Entry_Ans.config(state=NORMAL)
        root_Entry_Ans_Button.config(text="Submit", relief=RAISED)
        word = rd.choice(Words)
        color = rd.choice(Colors)
        root_Text.config(text=word)
        root_Text.config(fg=color)
        Timer()
    else:
        ans = root_Entry_Ans.get()
        if ans == color:
            print("Yahoo ! Correct")
            word = rd.choice(Words)
            color = rd.choice(Colors)
            root_Text.config(text=word)
            root_Text.config(fg=color)
            root_Remarks_num.config(text="Yahoo ! Correct.")
            correct += 1
            root_Correct_num.config(text=correct)
        elif len(ans) == 0:
            pass
        else:
            print("Oops ! Incorrect")
            root_Remarks_num.config(text="Oops ! Incorrect.")
            incorrect += 1
            root_Incorrect_num.config(text=incorrect)
        root_Entry_Ans.delete(0, END)


def Exit():
    sys.exit()


def Restart():
    root.destroy()
    os.startfile("gui12.py")


def exit_to_menu():
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\GamesLoby.py")
    root.destroy()


root_Menu_Btn = Button(root, text="<--", command=exit_to_menu)

root_heading = Label(root, text="Color Guessing Game")

root_Text = Label(root, text="START", font=10)

root_head = Label(root, text="Enter color name and not the name of the text.")

root_time = Label(root, text="Time left : ")
root_time_num = Label(root, text="60s")

root_Entry_Ans = Entry(root, state=DISABLED)
root_Entry_Ans_Button = Button(
    root, text="Start", relief=SOLID, bd=1, command=color)

root_Remarks = Label(root, text="Remarks : ")
root_Remarks_num = Label(root, text="--:--")

root_Correct = Label(root, text="Correct : ")
root_Correct_num = Label(root, text="--:--")

root_Incorrect = Label(root, text="Incorrect : ")
root_Incorrect_num = Label(root, text="--:--")

root_Score_Text = Label(root, text="Score : ")
root_Score_Text_num = Label(root, text="--:--")

root_Exit = Button(root, text="Exit", bg="red", fg="white",
                   bd=2, relief=SOLID, width=6, command=Exit)
root_Restart = Button(root, text="Restart", bg="red",
                      fg="white", bd=2, relief=SOLID, width=7, command=Restart)

root_Menu_Btn.place(x=1, y=1)
root_heading.place(x=85)
root_Text.place(x=124, y=25)
root_head.place(x=25, y=49)
root_time.place(x=90, y=75)
root_time_num.place(x=155, y=76)
root_Entry_Ans.place(x=60, y=98)
root_Entry_Ans_Button.place(x=195, y=95)
root_Remarks.place(x=50, y=135)
root_Remarks_num.place(x=190, y=135)
root_Correct.place(x=50, y=155)
root_Correct_num.place(x=190, y=155)
root_Incorrect.place(x=50, y=175)
root_Incorrect_num.place(x=190, y=175)
root_Score_Text.place(x=50, y=195)
root_Score_Text_num.place(x=190, y=195)
root_Exit.place(x=45, y=230)
root_Restart.place(x=175, y=230)
# root_Start.pack()

root.mainloop()
