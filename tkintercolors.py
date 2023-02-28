from tkinter import *
from tkinter import colorchooser
import json
f = open('theme.json', encoding="utf-8")
data = json.load(f)

root = Tk()
root.title("Генератор тем для Visiology")
root.geometry("500x200")

frame = Frame(root)
# frame.grid(sticky="W", column=0, row=0)
frame.pack(anchor=NW, side=LEFT)

style = ["#34A2FE", "#1E2735"]
lab = Label(frame, text="Заголовок", background="#34A2FE", fg="#FFFFFF", font=("Arial", 21, "bold"), width=13)
lab.pack()
# lab.grid(column=0, row=1)
lab2 = Label(frame, text="Текст", background="#1E2735", fg="#FFFFFF", font=("Arial", 21, "bold"), width=13, height=5)
# lab.grid(column=0, row=2)
lab2.pack()


def colorbg():
    lab.config(bg=colorchooser.askcolor()[1])
    # my_label = tk.Label(root, text=my_color).pack(pady=10)
    # my_label2 = tk.Label(root, text="You picked a color!", font=("Helvetica", 32), bg=my_color).pack()
    # lab.config(bg=my_color)

def colorfg():
    lab.config(fg=colorchooser.askcolor()[1])

def colorbg2():
    lab2.config(bg=colorchooser.askcolor()[1])


frame2 = Frame(root)
# frame2.grid(sticky="N", column=1, row=0)
frame2.pack(anchor=NW)
my_button = Button(frame2, text="Цвет заголовка", command=colorbg).grid(sticky="W", column=0, row=0)
# my_button2 = Button(frame2, text="Выбрать цвет текста", command=colorfg).grid(sticky="W", column=0, row=1)
my_button3 = Button(frame2, text="Цвет фона", command=colorbg2).grid(sticky="W", column=0, row=1)
my_button4 = Button(root, text="Создать тему", command=colorbg2).place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)


root.mainloop()