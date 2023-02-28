from tkinter import *
from tkinter import colorchooser
import json, themeform as tf
# f = open('theme.json', encoding="utf-8")
# data = json.load(f)

root = Tk()
root.title("Генератор тем для Visiology")
root.geometry("500x200")

frame = Frame(root)
# frame.grid(sticky="W", column=0, row=0)
frame.pack(anchor=NW, side=LEFT)

titlecol = "#34A2FE"
fillcol = "#1E2735"
graphscol = "#FFA700"
lab = Label(frame, text="Заголовок", background=titlecol, fg="#FFFFFF", font=("Arial", 21, "bold"), width=13)
lab.pack()
# lab.grid(column=0, row=1)
lab2 = Label(frame, text="Текст", background=fillcol, fg="#FFFFFF", font=("Arial", 21, "bold"), width=13, height=5)
# lab.grid(column=0, row=2)
lab2.pack()


def colorbg():
    entry = entrybg.get()
    global titlecol
    if entry:
        if len(entry) > 6:
            if entry.startswith("#"):
                entry = entry[3:]
            else:
                entry = entry[2:]
        if not entry.startswith("#"): entry = f"#{entry}"
        titlecol = entry
        entrybg.delete(0, END)
    else:
        titlecol = colorchooser.askcolor()[1]
    lab.config(bg=titlecol)


def colorfg():
    lab.config(fg=colorchooser.askcolor()[1])


def colorbg2():
    entry = entrybg2.get()
    global fillcol
    if entry:
        if len(entry) > 6:
            if entry.startswith("#"):
                entry = entry[3:]
            else:
                entry = entry[2:]
        if not entry.startswith("#"): entry = f"#{entry}"
        fillcol = entry
        entrybg2.delete(0, END)
    else:
        fillcol = colorchooser.askcolor()[1]
    lab2.config(bg=fillcol)


def createtheme():
    tf.savetheme(tf.jsonload(), [titlecol, fillcol, graphscol], entrytheme.get())

frame2 = Frame(root)
# frame2.grid(sticky="N", column=1, row=0)
frame2.pack(anchor=NW)
butbg = Button(frame2, text="Цвет заголовка", command=colorbg).grid(sticky="W", column=0, row=0)
entrybg = Entry(frame2, width=10)
entrybg.grid(sticky="W", column=1, row=0)
# my_button2 = Button(frame2, text="Выбрать цвет текста", command=colorfg).grid(sticky="W", column=0, row=1)
butbg2 = Button(frame2, text="Цвет фона", command=colorbg2).grid(sticky="W", column=0, row=1)
entrybg2 = Entry(frame2, width=10)
entrybg2.grid(sticky="W", column=1, row=1)

entrytheme = Entry(root, width=40)
entrytheme.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
entrytheme.insert(0, "Название_темы")
buttheme = Button(root, text="Создать тему", command=createtheme).place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)


root.mainloop()
