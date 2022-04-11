from tkinter import *
from tkinter import ttk


def frame_sentence():
    name = name_me.get()

    disp_tf.insert(0, f'{name}')


ws = Tk()
ws.title('Midterms in OOP')
ws.geometry('400x300')

name_me = Entry(ws)

name_lbl = Label(ws, text='Name', fg='red').place(x=265, y=65)

name_lbl.pack()
name_me.pack()

btn = Button(ws, text='Frame Sentence', relief=SOLID, command=frame_sentence).place(x=70, y=60)
btn.pack(pady=10)

disp_tf = Entry(ws, width=11, font=('Arial', 14).place(x=265, y=154))
disp_tf.pack(pady=5)

ws.mainloop()
