from os import startfile
from tkinter import *
import random as rd
import os
import sys

root = Tk()

root.title("Hangman Game")
root.geometry("560x386")
root.iconbitmap(
    r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\GL_icon.ico")

correct = 0
Incorrect = 0
buttonDisaled = 5
lives = 15

Animal = ["Lion", "Snake", "Elephant", "Mouse", "Monkey", "Giraffe", "Dog"]
Country = ["Pakistan", "China", "India",
           "Palestine", "Saudi Arab", "Bangladesh"]
Food = ["Burger", "Pizza", "Sandwitch",
        "Rice", "Biryani", "Pulao", "Spaghetti"]

Hint = {"Lion": "A wild animal, never leaves its prey and hunts it slowly slowly...",
        "Snake": "A wild Lizard, having no legs, bite creatures to death...",
        "Elephant": "A largest living land mammal, calm and herbivorous...",
        "Mouse": "A small animal, Sneak's into the house and bites everything on its way, Smelly...",
        "Monkey": "A naughty animal, little bit human, more like a tarzan...",
        "Giraffe": " A calm herbivorous animal with long neck...",
        "Dog": "A Loyal Friend, never forgets his home...",
        "Pakistan": "An Islamic country with very old & beautiful tradations...",
        "China": "Super Power Country with worlds largest population...",
        "India": "A Hindu Country, Having 2nd largest population in the world...",
        "Palestine": "A muslim Country in Western Asia captured by other terrorist state...",
        "Saudi Arab": "An Arab Muslim Country, haveing strict privacy laws, Known for its oil...",
        "Bangladesh": "A small muslim country seperated from another muslim country from hindu country...",
        "Burger": "Fast Food, Big pillows with Crispy and Crunchy cock between them...",
        "Pizza": "Fast Food, Geometrically Triangle...",
        "Sandwitch": "Build by the combination of Scary witch eating Sand from SeaView...",
        "Rice": "Takes two months to grow and eaten hundreds at a time...",
        "Biryani": "Desi food, Rice and Spice, ofc tasty...",
        "Pulao": "Desi Food but simple rice and lovely taste, added potatos sometimes...",
        "Spaghetti": "Chinese dish, type of very long ropes, Tangle like..."}


def update():
    global correct
    global Incorrect
    global Random_Word1
    global Random_Word2
    global Main_Word
    global word
    global buttonDisaled
    global lives
    Random_Word1 = "Animal", "Country", "Food"
    Random_Word2 = rd.choice(Random_Word1)
    Typeword.config(text=Random_Word2)
    if Random_Word2 == "Animal":
        word = Animal
    elif Random_Word2 == "Country":
        word = Country
    elif Random_Word2 == "Food":
        word = Food
    Main_Word = rd.choice(word)
    # print(Main_Word)
    # answer.insert(0, Main_Word)
    Hint_Text.config(text=Hint[Main_Word])


def begin():
    ButtonAns.config(state=NORMAL)
    again.config(state=NORMAL)
    answer.config(state=NORMAL)
    begin_text.destroy()
    Typeword.place(x=297, y=50)
    update()
    Start_Button.destroy()


def typeofword():
    global Random_Word1
    global Random_Word2
    global Main_Word
    global word
    global buttonDisaled
    Random_Word1 = "Animal", "Country", "Food"
    Random_Word2 = rd.choice(Random_Word1)
    Typeword.config(text=Random_Word2)
    if Random_Word2 == "Animal":
        word = Animal
    elif Random_Word2 == "Country":
        word = Country
    elif Random_Word2 == "Food":
        word = Food
    try:
        Main_Word = rd.choice(word)
        # print(Main_Word)
        Hint_Text.config(text=Hint[Main_Word])
    except IndexError:
        pass
    if buttonDisaled > -1:
        BL.config(text=buttonDisaled)
    buttonDisaled = buttonDisaled - 1
    if buttonDisaled < 0:
        again.config(state=DISABLED)
    # answer.insert(0, Main_Word)


def chooseAgain():
    global Random_Word2
    typeofword()
    Typeword.config(text=Random_Word2)


def PlaySystem(*event):
    global correct
    global Incorrect
    global Random_Word1
    global Random_Word2
    global Main_Word
    global word
    global buttonDisaled
    global lives
    User_Ans = answer.get().capitalize()
    if User_Ans == Main_Word:
        A1.config(text=Main_Word)
        print("Winner !")
        correct = correct + 1
        A4.config(text=correct)
        A2.config(text="Yahoo ! Correct.")
        try:
            update()
            word.remove(Main_Word)
        except IndexError:
            # if len(Animal) == 0 and len(Food) == 0 and len(Country):
            if not Animal and not Food and not Country:
                answer.delete(0, END)
                ButtonAns.config(state=DISABLED)
                again.config(state=DISABLED)
                hint_dummy.destroy()
                Hint_Text.destroy()
                answer.config(state=DISABLED)
                Label(text="Finished", font="ariel 15").place(x=250, y=85)
                if int(A4.cget("text")) > int(A5.cget("text")):
                    A6.config(text="You Win :)")
                else:
                    A6.config(text="You Lost :(")
            else:
                pass
    elif len(User_Ans) == 0:
        pass
    elif User_Ans != Main_Word:
        print("Wrong !")
        A1.config(text=Main_Word)
        A2.config(text="Oops ! Incorrect.")
        Incorrect = Incorrect + 1
        A5.config(text=Incorrect)
        lives = lives - 1
        A3.config(text=lives)
        # word.remove(Main_Word)
        update()
        if A3.cget("text") == 0:
            answer.delete(0, END)
            ButtonAns.config(state=DISABLED)
            again.config(state=DISABLED)
            hint_dummy.destroy()
            Hint_Text.destroy()
            answer.config(state=DISABLED)
            Label(text="Finished", font="ariel 15").place(x=250, y=85)
            if int(A4.cget("text")) > int(A5.cget("text")):
                A6.config(text="You Win :)")
            else:
                A6.config(text="You Lost :(")
    answer.delete(0, END)


root.bind('<Return>', PlaySystem)


def Exit():
    sys.exit()


def Restart():
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\gui15_Hangman.py")
    root.destroy()


def Exit_to_GL():
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\GamesLoby.py")
    root.destroy()


Label(root, text="Hang Man", font=[
      "Bookman Old Style", 20]).place(x=205, y=0)

Button(root, text="<--", command=Exit_to_GL).place(x=0, y=0)
Label(root, text="Your word is :", font="ariel 10").place(x=200, y=50)
Typeword = Label(root, text=None, font="ariel 10")
# Typeword.place(x=297, y=50)
again = Button(root, text="⟲", bd=1, relief=SOLID, state=DISABLED,
               command=typeofword)
again.place(x=360, y=50)
BL = Label(root, text=5)
BL.place(x=390, y=51)
hint_dummy = Label(root, text="Hint :-")
hint_dummy.place(x=50, y=87)
begin_text = Label(text="Press start button to begin the game...")
begin_text.place(x=103, y=87)
Hint_Text = Label(root, text="")
Hint_Text.place(x=100, y=87)
Label(root, text="Answer :-").place(x=160, y=125)
answer = Entry(root, state=DISABLED)
answer.place(x=230, y=127)
ButtonAns = Button(root, text="Submit", state=DISABLED, command=PlaySystem)
ButtonAns.place(x=366, y=123)
Label(root, text="Correct Word :").place(x=160, y=177)
A1 = Label(root, text="--:--")
A1.place(x=342, y=177)
Label(root, text="Remarks :").place(x=160, y=204)
A2 = Label(root, text="--:--")
A2.place(x=342, y=204)
Label(root, text="Lives :").place(x=160, y=231)
A3 = Label(root, text="15")
A3.place(x=342, y=231)
Label(root, text="Correct's :").place(x=160, y=258)
A4 = Label(root, text="0")
A4.place(x=342, y=258)
Label(root, text="Incorrect's :").place(x=160, y=285)
A5 = Label(root, text="0")
A5.place(x=342, y=285)
Label(root, text="Result :").place(x=160, y=312)
A6 = Label(root, text="--:--")
A6.place(x=342, y=312)
Start_Button = Button(root, text="Start", width=5,
                      command=begin)
Start_Button.place(x=297, y=49)
root_Exit_Button = Button(root, text="Exit", bg="red",
                          fg="white", bd=2, relief=SOLID, width=6, command=Exit)
root_Restart_Button = Button(root, text="Restart", bg="red", fg="white",
                             bd=2, relief=SOLID, justify=LEFT, width=7, command=Restart)
root_Exit_Button.place(x=160, y=345)
root_Restart_Button.place(x=328, y=345)

root.mainloop()
