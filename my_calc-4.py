from Tkinter import *
from math import *
root=Tk()
root.title('CALCULATOR')
root.geometry('400x450')
e=Entry(root, width=18, font='Arial 30 bold', bd=5,bg='gray', relief='sunken',justify='right')
e.grid(row=0, column=0, columnspan=4)
def add_entry(x):
    e.insert(28, x)
def result(y):
    e.delete(0, END)
    e.insert(28, y)
def clear():
    e.delete(0, END)
def back():
    e.delete(0,1)
Button(root, text='7', width=3, height=3, command=lambda: add_entry('7')).grid(row=1,column=0, sticky=E+W+N+S)
Button(root, text='8', width=3, height=3, command=lambda: add_entry('8')).grid(row=1,column=1, sticky=E+W+N+S)
Button(root, text='9', width=3, height=3, command=lambda: add_entry('9')).grid(row=1,column=2, sticky=E+W+N+S)
Button(root, text='+', width=3, height=3, command=lambda: add_entry('+')).grid(row=1,column=3, sticky=E+W+N+S)

Button(root, text='4', width=3, height=3, command=lambda: add_entry('4')).grid(row=2,column=0, sticky=E+W+N+S)
Button(root, text='5', width=3, height=3, command=lambda: add_entry('5')).grid(row=2,column=1, sticky=E+W+N+S)
Button(root, text='6', width=3, height=3, command=lambda: add_entry('6')).grid(row=2,column=2, sticky=E+W+N+S)
Button(root, text='-', width=3, height=3, command=lambda: add_entry('-')).grid(row=2,column=3, sticky=E+W+N+S)

Button(root, text='1', width=3, height=3, command=lambda: add_entry('1')).grid(row=3,column=0, sticky=E+W+N+S)
Button(root, text='2', width=3, height=3, command=lambda: add_entry('2')).grid(row=3,column=1, sticky=E+W+N+S)
Button(root, text='3', width=3, height=3, command=lambda: add_entry('3')).grid(row=3,column=2, sticky=E+W+N+S)
Button(root, text='*', width=3, height=3, command=lambda: add_entry('*')).grid(row=3,column=3, sticky=E+W+N+S)

Button(root, text='0', width=3, height=3, command=lambda: add_entry('0')).grid(row=4,column=0, sticky=E+W+N+S)
Button(root,text=',',  width=3,height=3,command=lambda:add_entry(',')).grid(row=4,column=1,sticky=E+W+N+S)
Button(root, text='.', width=3, height=3, command=lambda: add_entry('.')).grid(row=4,column=2, sticky=E+W+N+S)
Button(root, text='/', width=3, height=3, command=lambda: add_entry('/')).grid(row=4,column=3, sticky=E+W+N+S)

Button(root,text='PI', width=3,height=3,command=lambda:add_entry('pi')).grid(row=5,column=0, sticky=E+W+N+S)
Button(root,text='COS',width=3,height=3,command=lambda:add_entry('cos(')).grid(row=5,column=1,sticky=E+W+N+S)
Button(root,text='SIN',width=3,height=3,command=lambda:add_entry('sin(')).grid(row=5,column=2,sticky=E+W+N+S)
Button(root,text='TAN',width=3,height=3,command=lambda:add_entry('tan(')).grid(row=5,column=3,sticky=E+W+N+S)

Button(root,text='LOG',width=3,height=3,command=lambda:add_entry('log(')).grid(row=6,column=0,sticky=E+W+N+S)
Button(root,text='SQRT',width=3,height=3,command=lambda:add_entry('sqrt(')).grid(row=6,column=1,sticky=E+W+N+S)
Button(root, text='<-', width=3, height=3, command=lambda: back()).grid(row=6,column=2, sticky=E+W+N+S)
Button(root, text='C', width=3, height=3, command=lambda: clear()).grid(row=6,column=3, sticky=E+W+N+S)

Button(root, text='=', width=3, height=3, command=lambda: result(eval(e.get()))).grid(row=7,column=0, sticky=E+W+N+S)
Button(root, text='POWER', width=3, height=3, command=lambda: add_entry('**')).grid(row=7,column=1, sticky=E+W+N+S)
Button(root, text='(', width=3, height=3, command=lambda: add_entry('(')).grid(row=7,column=2, sticky=E+W+N+S)
Button(root, text=')', width=3, height=3, command=lambda: add_entry(')')).grid(row=7,column=3, sticky=E+W+N+S)
root.mainloop()
