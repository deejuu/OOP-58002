from tkinter import *
from tkinter import ttk
window = Tk()

def Myname():
    txtfld['text'] = 'NAME'


window.geometry("500x250+10+20")
window.title("Midterm in OOP")


label = Label(window, text = "Enter your fullname:", fg = "red")
label.place(x=60, y=70)

button = Button(window, text = "Click to display your Fullname", fg = "red", command=Myname)
button.place (x=60, y=145)

txtfld = Entry(window, textvariable = 'NAME', bd = 5)
txtfld.place(x=265, y=65)

txtfld = Entry(window, text = 'FULLNAME', bd = 5)
txtfld.place(x=265, y=145)

window.mainloop()
