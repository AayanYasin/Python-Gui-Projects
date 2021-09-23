from tkinter import *
from tkinter import font
from tkinter import filedialog as fd
from tkinter import messagebox
import random as rd
import datetime as dt
import os
import keyword as kb
import webbrowser as wb

root = Tk()
try:
    root.iconbitmap("Notepad1.ico")
except Exception:
    pass
root.title("Untitled - Notepad - Aayan Yasin")
O1x = 1120
O2y = 550
root.geometry(f"{O1x}x{O2y}")
root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)
fontsmain = font.Font(family="areal", size=12)

Scroll = Scrollbar(root)
Scroll2 = Scrollbar(root, orient=HORIZONTAL)
Scroll.pack(side=RIGHT, fill=Y)

textarea = Text(root, font=fontsmain, yscrollcommand=Scroll.set,
                xscrollcommand=Scroll2.set, undo=True)
textarea.pack(expand=True, fill=BOTH)


def statusbarmain():
    global statusbar
    global statusbar_Content1
    statusbar = Frame(textarea)
    statusbar.pack(side=BOTTOM, fill=X)
    statusbar_Content1 = Label(
        statusbar, anchor=SW, width=18, text="Ln 1, col 1")
    statusbar_Content2 = Label(statusbar, anchor=SW, text="100%")
    statusbar_Content3 = Label(
        statusbar, anchor=SW, width=15, text="Windows (CRLF)")
    statusbar_Content4 = Label(statusbar, anchor=SW, width=13, text="UTF-8")
    statusbar_Content4.pack(side=RIGHT)
    Label(statusbar, anchor=SW, text="|", state=DISABLED).pack(side=RIGHT)
    statusbar_Content3.pack(side=RIGHT)
    Label(statusbar, anchor=SW, text="|", state=DISABLED).pack(side=RIGHT)
    statusbar_Content2.pack(side=RIGHT)
    Label(statusbar, anchor=SW, text="|", state=DISABLED).pack(side=RIGHT)
    statusbar_Content1.pack(side=RIGHT)
    Label(statusbar, anchor=SW, text="|", state=DISABLED).pack(side=RIGHT)


lines = 1
col = 1
first_time_forgive = 0


def Enter_line(*event):
    try:
        global lines
        global col
        col = 1
        lines += 1
        statusbar_Content1.config(text=f"Ln {lines}, col 1")
    except TclError:
        return


root.bind("<Return>", Enter_line)


def Row_Column(*event):
    try:
        global first_time_forgive
        global col
        statusbar_Content1.config(text=f"Ln {lines}, col {col}")
        col = col + 1
    except TclError:
        return


def Back_space(*event):
    try:
        global lines
        global col
        if col > 0:
            col = col - 1
        if col == 0 and lines > 1:
            lines -= 1
        statusbar_Content1.config(text=f"Ln {lines}, col {col}")
    except TclError:
        return


Scroll.config(command=textarea.yview)
Scroll2.config(command=textarea.xview)

cbm = IntVar(value=1)


def WordWrap():
    if cbm.get() == 0:
        textarea.config(wrap="none")
        Scroll2.pack(anchor=S, fill=X)
    elif cbm.get() == 1:
        textarea.config(wrap="word")
        Scroll2.pack_forget()
    # print(cbm.get())
    # pass


def Fonts():
    # fonts = font.Font(family=rd.choice(font.families()))
    fontsmain.config(family=rd.choice(font.families()))


def DFonts():
    fontsmain.config(family="areal")


def NEW_window(*event):
    os.startfile(
        r"C:\Users\Yasin\Documents\Aayan\Aayan Programming Projects\Python Gui Games\gui_notepad.py")


root.bind("<Control-Shift-N>", NEW_window)
root.bind("<Control-Shift-n>", NEW_window)


def New(*event):
    if root.title() == "Untitled - Notepad - Aayan Yasin":
        if textarea.get(1.0, END).split() == [] or textarea.get(1.0, END).split() == []:
            textarea.delete(1.0, END)
            root.title("Untitled - Notepad - Aayan Yasin")
        else:
            mb4 = messagebox.askyesnocancel(
                "Notepad - Aayan  Yasin", "Do you want to save Untitled.txt ?")
            if mb4:
                Save_File()
                textarea.delete(1.0, END)
                root.title("Untitled - Notepad - Aayan Yasin")
            elif mb4 is not None:
                textarea.delete(1.0, END)
                root.title("Untitled - Notepad - Aayan Yasin")
    else:
        if os.path.isfile(root.title()):
            f = open(root.title())
            f1 = f.read()
            if textarea.get(1.0, END).split() == f1.split():
                textarea.delete(1.0, END)
                root.title("Untitled - Notepad - Aayan Yasin")
            else:
                mb3 = messagebox.askyesnocancel(
                    "Notepad - Aayan  Yasin", f"Do you want to save changes to {os.path.basename(root.title())} ?")
                if mb3:
                    Save_File()
                    textarea.delete(1.0, END)
                    root.title("Untitled - Notepad - Aayan Yasin")
                elif mb3 is not None:
                    textarea.delete(1.0, END)
                    root.title("Untitled - Notepad - Aayan Yasin")


root.bind("<Control-N>", New)
root.bind("<Control-n>", New)


def date(*event):
    x = dt.datetime.now()
    date1 = x.strftime("%X ")
    date2 = x.strftime("%p ")
    date3_day = x.strftime("%d ")
    date3_month = x.strftime("%a ")
    date3_year = x.strftime("%y ")
    main_date = (date1 + date2 + date3_day +
                 "-" + date3_month + "-" + date3_year)
    textarea.insert(END, main_date)


root.bind("<F5>", date)


def Open_file(*event):
    global fileToOpen
    global CheckingFileEqual
    if root.title() == "Untitled - Notepad - Aayan Yasin":
        if textarea.get(1.0, END).split() == []:
            fileToOpen = fd.askopenfile(
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            try:
                root.title(fileToOpen.name)
            except AttributeError:
                pass
            if not fileToOpen:
                return
            with open(fileToOpen.name) as openfile:
                getfilelines = openfile.read()
                CheckingFileEqual = getfilelines.split()
                # print(CheckingFileEqual)
                textarea.delete(1.0, END)
                textarea.insert(1.0, getfilelines)
                openfile.close()
        else:
            mb4 = messagebox.askyesnocancel(
                "Notepad - Aayan  Yasin", "Do you want to save Untitled.txt ?")
            if mb4:
                Save_File()
                fileToOpen = fd.askopenfile(
                    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
                try:
                    root.title(fileToOpen.name)
                except AttributeError:
                    pass
                if not fileToOpen:
                    return
                with open(fileToOpen.name) as openfile:
                    getfilelines = openfile.read()
                    CheckingFileEqual = getfilelines.split()
                    # print(CheckingFileEqual)
                    textarea.delete(1.0, END)
                    textarea.insert(1.0, getfilelines)
                    openfile.close()
            elif mb4 is not None:
                fileToOpen = fd.askopenfile(
                    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
                try:
                    root.title(fileToOpen.name)
                except AttributeError:
                    pass
                if not fileToOpen:
                    return
                with open(fileToOpen.name) as openfile:
                    getfilelines = openfile.read()
                    CheckingFileEqual = getfilelines.split()
                    # print(CheckingFileEqual)
                    textarea.delete(1.0, END)
                    textarea.insert(1.0, getfilelines)
                    openfile.close()
    else:
        with open(root.title()) as read:
            s = read.read()
        if textarea.get(1.0, END).split() == s.split():
            fileToOpen = fd.askopenfile(
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            try:
                root.title(fileToOpen.name)
            except AttributeError:
                pass
            if not fileToOpen:
                return
            with open(fileToOpen.name) as openfile:
                getfilelines = openfile.read()
                CheckingFileEqual = getfilelines.split()
                # print(CheckingFileEqual)
                textarea.delete(1.0, END)
                textarea.insert(1.0, getfilelines)
                openfile.close()
        else:
            mb4 = messagebox.askyesnocancel(
                "Notepad - Aayan  Yasin", f"Do you want to save changes to {os.path.basename(root.title())} ?")
            if mb4:
                Save_File()
                fileToOpen = fd.askopenfile(
                    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
                try:
                    root.title(fileToOpen.name)
                except AttributeError:
                    pass
                if not fileToOpen:
                    return
                with open(fileToOpen.name) as openfile:
                    getfilelines = openfile.read()
                    CheckingFileEqual = getfilelines.split()
                    # print(CheckingFileEqual)
                    textarea.delete(1.0, END)
                    textarea.insert(1.0, getfilelines)
                    openfile.close()
            elif mb4 is not None:
                fileToOpen = fd.askopenfile(
                    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
                try:
                    root.title(fileToOpen.name)
                except AttributeError:
                    pass
                if not fileToOpen:
                    return
                with open(fileToOpen.name) as openfile:
                    getfilelines = openfile.read()
                    CheckingFileEqual = getfilelines.split()
                    # print(CheckingFileEqual)
                    textarea.delete(1.0, END)
                    textarea.insert(1.0, getfilelines)
                    openfile.close()


root.bind("<Control-o>", Open_file)
root.bind("<Control-O>", Open_file)


def Saveas_File(*event):
    global filetosave
    filetosave = fd.asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filetosave:
        return
    with open(filetosave, "w") as savefile:
        savefile.write(textarea.get(1.0, END))
    root.title(filetosave)


root.bind("<Control-Shift-s>", Saveas_File)
root.bind("<Control-Shift-S>", Saveas_File)


def Save_File(*event):
    try:
        if root.title() == fileToOpen.name:
            with open(root.title(), "w") as savefile:
                savefile.write(textarea.get(1.0, END))
    except NameError or AttributeError:
        Saveas_File()
        return


root.bind("<Control-s>", Save_File)
root.bind("<Control-S>", Save_File)


def Zoom_In(*event):
    global fontsmain
    if fontsmain.cget("size") == 50:
        return
    fontsmain.config(size=int(fontsmain.cget("size"))+2)


root.bind("<Control-Key-=>", Zoom_In)
root.bind("<Control-Key-plus>", Zoom_In)


def Zoom_Out(*event):
    global fontsmain
    fontsmain.config(size=int(fontsmain.cget("size"))-2)


root.bind("<Control-Key-minus>", Zoom_Out)


def Zoom_Default(*event):
    global fontsmain
    fontsmain.config(size=12)


def messageWindowforPagesetup():
    global O1x
    global O2y

    def ChangeXY():
        global O1x
        global O2y
        O1x = e1.get()
        O2y = e2.get()
        root.geometry(f"{O1x}x{O2y}")
        # print("Done")
    alert = Toplevel()
    alert.title("Change Orentation - Notepad")
    alert.geometry("350x100")
    Label(alert, text="X :").place(x=10, y=20)
    e1 = Entry(alert)
    e1.place(x=33, y=22)
    Label(alert, text="Y :").place(x=177, y=20)
    e2 = Entry(alert)
    e2.place(x=200, y=22)
    e1.insert(0, 1120)
    e2.insert(0, 550)
    B1 = Button(alert, text="Change", bd=1,
                relief=SOLID, width=8, command=ChangeXY)
    B1.place(x=148, y=60)
    alert.mainloop()


def StatusCheckButton():
    if cbs.get() == 1:
        statusbarmain()
    elif cbs.get() == 0:
        statusbar.destroy()


def cut():
    textarea.event_generate(("<<Cut>>"))


def copy():
    textarea.event_generate(("<<Copy>>"))


def paste():
    textarea.event_generate(("<<Paste>>"))


def Sall():
    textarea.event_generate(("<<SelectAll>>"))


def bold():
    global fontsman
    if b.get() == 1:
        fontsmain.config(weight="bold")
        print(1)
    elif b.get() == 0:
        fontsmain.config(weight="normal")


def italic():
    global fontsmainn
    if i.get() == 1:
        fontsmain.config(slant="italic")
        print(1)
    elif i.get() == 0:
        fontsmain.config(slant="roman")


def underline():
    global fontsmain
    if u.get() == 1:
        fontsmain.config(underline=True)
        print(1)
    elif u.get() == 0:
        fontsmain.config(underline=False)


def exit1():
    global filetosave
    # print(root.title())
    # print(os.path.isfile(root.title()))
    if os.path.isfile(root.title()):
        with open(root.title()) as exitlast:
            samenot = exitlast.read()
        a = textarea.get(0.1, END)
        if samenot.split() == textarea.get(1.0, END).split():
            # print(textarea.get(1.0, END).split())
            root.destroy()
        else:
            # print("error")
            mb1 = messagebox.askyesnocancel(
                "Notepad - Aayan  Yasin", f"Do you want to save changes to {os.path.basename(root.title())} ?")
            if mb1:
                Save_File()
                root.destroy()
            elif mb1 is not None:
                root.destroy()
    else:
        # print("No file exist !")
        # print(textarea.get(1.0, END).split())
        if textarea.get(1.0, END).split() == [] or textarea.get(1.0, END).split() == None:
            root.destroy()
        else:
            mb2 = messagebox.askyesnocancel(
                "Notepad - Aayan  Yasin", "Do you want to save Untitled.txt ?")
            if mb2:
                Save_File()
            elif mb2 is not None:
                root.destroy()


root.protocol("WM_DELETE_WINDOW", exit1)


root.bind("<Control-0>", Zoom_Default)

menu = Menu(root)
item1 = Menu(menu, tearoff=0)
item1.add_command(label="New", command=New,
                  accelerator="Ctrl+N")
item1.add_command(label="New Window", command=NEW_window,
                  accelerator="Ctrl+Shift+N")
item1.add_command(label="Open...", command=Open_file, accelerator="Ctrl+O")
item1.add_command(label="Save", command=Save_File, accelerator="Ctrl+S")
item1.add_command(label="Save As...", command=Saveas_File,
                  accelerator="Ctrl+Shift+S")
item1.add_separator()
item1.add_command(label="Page Setup...", command=messageWindowforPagesetup)
item1.add_command(label="Print....", command="", accelerator="Ctrl+P")
item1.add_separator()
item1.add_command(label="Exit", command=exit1)
menu.add_cascade(label="File", menu=item1)

item2 = Menu(menu, tearoff=0)
item2.add_command(label="Undo", command=textarea.edit_undo,
                  accelerator="Ctrl+Z")
item2.add_command(label="Redo", command=textarea.edit_redo,
                  accelerator="Ctrl+Y")
item2.add_separator()
item2.add_command(label="Cut", command=cut, accelerator="Ctrl+X")
item2.add_command(label="Copy", command=copy, accelerator="Ctrl+C")
item2.add_command(label="Paste", command=paste, accelerator="Ctrl+V")
item2.add_command(label="Delete", command="", accelerator="Del")
item2.add_separator()
item2.add_command(label="Find", command="", accelerator="Ctrl+F")
item2.add_command(label="Replace", command="", accelerator="Ctrl+H")
item2.add_separator()
item2.add_command(label="Select All", command=Sall, accelerator="Ctrl+A")
item2.add_command(label="Time/Date", command=date, accelerator="F5")
menu.add_cascade(label="Edit", menu=item2)

item3 = Menu(menu, tearoff=0)
item3.add_checkbutton(label="Word Wrap", command=WordWrap,
                      variable=cbm, onvalue=1, offvalue=0)
item3.add_command(label="Random Font", command=Fonts)
item3.add_command(label="Default Font", command=DFonts)
menu.add_cascade(label="Format", menu=item3)
item3.add_separator()
# item3.add_command(label="Format Text")
item3menu = Menu(item3, tearoff=0)
item3.add_cascade(label="Format Text", menu=item3menu)
b = IntVar(value=0)
i = IntVar(value=0)
u = IntVar(value=0)
item3menu.add_checkbutton(label="Bold", command=bold,
                          variable=b, onvalue=1, offvalue=0)
item3menu.add_checkbutton(label="Italic", command=italic,
                          variable=i, onvalue=1, offvalue=0)
item3menu.add_checkbutton(
    label="Underline", command=underline, variable=u, onvalue=1, offvalue=0)

cbs = IntVar(value=1)

item4 = Menu(menu, tearoff=0)
item4menu = Menu(item4, tearoff=0)
item4.add_cascade(label="Zoom", menu=item4menu)
item4menu.add_command(label="Zoom In", command=Zoom_In,
                      accelerator="Ctrl+Plus")
item4menu.add_command(label="Zoom Out", command=Zoom_Out,
                      accelerator="Ctrl+Minus")
item4menu.add_command(label="Restore Default Zoom",
                      command=Zoom_Default, accelerator="Ctrl+0")
item4.add_checkbutton(label="Status Bar", command=StatusCheckButton,
                      variable=cbs, onvalue=1, offvalue=0)
menu.add_cascade(label="View", menu=item4)

item5 = Menu(menu, tearoff=0)
item5.add_command(label="View Help", command=lambda: wb.open_new_tab(
    "https://support.microsoft.com/en-us/windows/help-in-notepad-4d68c388-2ff2-0e7f-b706-35fb2ab88a8c"))
item5.add_command(label="Send Feedback", command=lambda: wb.open_new_tab(
    "https://playwithaayan.000webhostapp.com/contact.html"))
item5.add_separator()
item5.add_command(label="About Aayan Yasin", command=lambda: wb.open_new_tab(
    "https://playwithaayan.000webhostapp.com/"))
menu.add_cascade(label="Help", menu=item5)

root.config(menu=menu)
StatusCheckButton()

Row_Column()
# Keyboard keys - Alphabetic & Numbers - Symbols Only.
root.bind("1", Row_Column)
root.bind("2", Row_Column)
root.bind("3", Row_Column)
root.bind("4", Row_Column)
root.bind("5", Row_Column)
root.bind("6", Row_Column)
root.bind("7", Row_Column)
root.bind("8", Row_Column)
root.bind("9", Row_Column)
root.bind("0", Row_Column)
root.bind("q", Row_Column)
root.bind("w", Row_Column)
root.bind("e", Row_Column)
root.bind("r", Row_Column)
root.bind("t", Row_Column)
root.bind("y", Row_Column)
root.bind("u", Row_Column)
root.bind("i", Row_Column)
root.bind("o", Row_Column)
root.bind("p", Row_Column)
root.bind("a", Row_Column)
root.bind("s", Row_Column)
root.bind("d", Row_Column)
root.bind("f", Row_Column)
root.bind("g", Row_Column)
root.bind("h", Row_Column)
root.bind("h", Row_Column)
root.bind("j", Row_Column)
root.bind("k", Row_Column)
root.bind("l", Row_Column)
root.bind("z", Row_Column)
root.bind("x", Row_Column)
root.bind("c", Row_Column)
root.bind("v", Row_Column)
root.bind("b", Row_Column)
root.bind("n", Row_Column)
root.bind("m", Row_Column)
root.bind("_", Row_Column)
root.bind("-", Row_Column)
root.bind("+", Row_Column)
root.bind("=", Row_Column)
root.bind("\\", Row_Column)
root.bind("|", Row_Column)
root.bind("}", Row_Column)
root.bind("{", Row_Column)
root.bind("]", Row_Column)
root.bind("[", Row_Column)
root.bind("\"", Row_Column)
root.bind("'", Row_Column)
root.bind(";", Row_Column)
root.bind(":", Row_Column)
root.bind("/", Row_Column)
root.bind("?", Row_Column)
root.bind(">", Row_Column)
root.bind(".", Row_Column)
# root.bind("<", Row_Column)
root.bind(")", Row_Column)
root.bind("(", Row_Column)
root.bind("*", Row_Column)
root.bind("&", Row_Column)
root.bind("^", Row_Column)
root.bind("%", Row_Column)
root.bind("$", Row_Column)
root.bind("#", Row_Column)
root.bind("@", Row_Column)
root.bind("!", Row_Column)
root.bind("~", Row_Column)
root.bind("`", Row_Column)

Back_space()
root.bind("<BackSpace>", Back_space)

root.mainloop()
