from tkinter import *

window=Tk()
#window.geometry("500x500")
window.title("CALCULATOR")


def zero():
    print("button 0 click")
def one():
    print("button 1 click")
def two():
    print("button 2 click")
def three():
    print("button 3 click")
def four():
    print("button 4 click")
def five():
    print("button 5 click")
def six():
    print("button 6 click")
def seven():
    print("button 7 click")
def eight():
    print("button 8 click")
def nine():
    print("button 9 click")
def add():
    print("button + click")
def sub():
    print("button - click")
def div():
    print("button / click")
def mul():
    print("button x click")
def equal():
    print("button = click")
def decimal():
    print("button . click")




button7=Button(window,text="7",command=seven)
button7.grid(row=0,column=0)
button8=Button(window,text="8",command=eight)
button8.grid(row=0,column=1)
button9=Button(window,text="9",command=nine)
button9.grid(row=0,column=2)
button_div=Button(window,text="/",command=div)
button_div.grid(row=0,column=3)

button4=Button(window,text="4",command=four)
button4.grid(row=1,column=0)
button5=Button(window,text="5",command=five)
button5.grid(row=1,column=1)
button6=Button(window,text="6",command=six)
button6.grid(row=1,column=2)
button_mul=Button(window,text="X",command=mul)
button_mul.grid(row=1,column=3)

button1=Button(window,text="1",command=one)
button1.grid(row=2,column=0)
button2=Button(window,text="2",command=two)
button2.grid(row=2,column=1)
button3=Button(window,text="3",command=three)
button3.grid(row=2,column=2)
button_sub=Button(window,text="-",command=sub)
button_sub.grid(row=2,column=3)

button_dec=Button(window,text=".",command=decimal)
button_dec.grid(row=3,column=0)
button0=Button(window,text="0",command=zero)
button0.grid(row=3,column=1)
button_eql=Button(window,text="=",command=equal)
button_eql.grid(row=3,column=2)
button_add=Button(window,text="+",command=add)
button_add.grid(row=3,column=3)





window.mainloop()