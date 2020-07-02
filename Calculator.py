from tkinter import *

window=Tk()
window.geometry("500x500")
window.title("CALCULATOR")
window.config()

def hello():
    print("button click")

butten1=Button(window,text="OK",command=hello)
butten1.grid(row=0,column=0)

window.mainloop()