from tkinter import *
import tkinter as tk

lista=["vaishu",'public', 'actions','ganesh','ganesh vaishu', 'additional', 'also', 'an', 'and', 'angle', 'are', 'as', 'be', 'bind', 'bracket', 'brackets',
         'button', 'can', 'cases', 'configure', 'course', 'detail', 'enter', 'event', 'events', 'example', 'field',
         'fields', 'for', 'give', 'important', 'in', 'information', 'is', 'it', 'just', 'key', 'keyboard', 'kind',
         'leave', 'left', 'like', 'manager', 'many', 'match', 'modifier', 'most', 'of', 'or', 'others', 'out', 'part',
         'simplify', 'space', 'specifier', 'specifies', 'string;', 'that', 'the', 'there', 'to', 'type', 'unless',
         'use', 'used', 'user', 'various', 'ways', 'we', 'window', 'wish', 'you','static'
         ,'void','main','protected']
ls=[]
ls1=[]
global flag
flag=False
def sug(event):
    print("sug")
    t1.config(state=NORMAL)
    global flag
    global text
    aa=float(t.index(INSERT))
    a = str(t.get(float(int(aa-0.1)), END))
    print(a)
    t1.delete(0.0,END)
    if a.__contains__(" "):
        a = str(t.get(float(int(aa - 0.1)), END))
        i=0
        b1=""
        b2=""
        ls=a.split(" ")
        a1=ls[ls.__len__()-1]
        a1=a1.rstrip()
        ls1=a1.split("\n")
        a2=ls1[0]
        text=a2
        t1.delete(0.0, END)
        while (i < lista.__len__() - 1):
            b = str(lista[i])

            if b.__len__() > 1 and a2.__len__()== 2:
                b1 = b[0] + b[1]
            if b.__len__() > 2 and a2.__len__()== 3:
                b2 = b[0] + b[1] + b[2]

            if a2.__contains__(b[0]) and a2.__len__()==1:
                t1.insert(0.0, lista[i] + "\n")
            if a2.__contains__(b1) and a2.__len__() == 2:
                t1.insert(0.0, lista[i] + "\n")
            if a2.__contains__(b2) and a2.__len__() == 3:
                t1.insert(0.0, lista[i] + "\n")


            i = i + 1
        a=""

    else:
        b1=""
        b2=""
        t1.delete(0.0,END)
        if flag==True:
            a = str(t.get(aa - 0.1, END))
        else:
            a = str(t.get(float(int(aa - 0.1)), END))
        i=0
        text=a
        while (i < lista.__len__() - 1):
            b = str(lista[i])
            if b.__len__()>1 and a.__len__()-1==2:
                b1=b[0]+b[1]
            if b.__len__()>2 and a.__len__()-1==3:
                b2=b[0]+b[1]+b[2]

            if a.__contains__(b[0]) and a.__len__()-1==1:
                t1.insert(0.0, lista[i] + "\n")

            if a.__contains__(b1) and a.__len__()-1==2:
                t1.insert(0.0, lista[i] + "\n")

            if a.__contains__(b2) and a.__len__()-1==3:
                t1.insert(0.0, lista[i] + "\n")

            i = i + 1

        if a.__contains__(" ") or a.__len__()==1:
            t1.delete(0.0, END)
        a=""
        flag=False
        t1.config(state=DISABLED)

def dell(event):
    print("dell")
    t1.config(state=NORMAL)
    t1.delete(0.0,END)
    global flag
    flag = True
    t1.config(state=DISABLED)

def copy(event):
    print("copy")
    i=0
    ind=float(t.index(INSERT))
    a=t1.get(float(t1.index(INSERT)),END)
    ls=a.split("\n")
    b=str(t1.get(0.0,END))
    ls1=b.split("\n")
    while(True):
        if ls[1]==ls1[i]:
            break
        i=i+1
    c=ls1[i-1]
    c1=""
    ind2=0.0
    ii=str(ind)
    if str(t.get(float(int(ind - 0.1)), END)).__contains__(" "):
        if ii.__len__()==3:
            if text.__len__() == 1:
                c1 = c[0]
                ind2 = ind - 0.1
            if text.__len__() == 2:
                c1 = c[0] + c[1]
                ind2 = ind - 0.2
            if text.__len__() == 3:
                c1 = c[0] + c[1] + c[2]
                ind2 = ind - 0.3
        else:
            if text.__len__() == 1:
                c1 = c[0]
                ind2 = ind - 0.01
            if text.__len__() == 2:
                c1 = c[0] + c[1]
                ind2 = ind - 0.02
            if text.__len__() == 3:
                c1 = c[0] + c[1] + c[2]
                ind2 = ind - 0.03


    else:
        if ii.__len__()==3:
            if text.__len__() - 1 == 1:
                c1 = c[0]
                ind2 = ind - 0.1
            if text.__len__() - 1 == 2:
                c1 = c[0] + c[1]
                ind2 = ind - 0.2
            if text.__len__() - 1 == 3:
                c1 = c[0] + c[1] + c[2]
                ind2 = ind - 0.3
        else:
            if text.__len__() - 1 == 1:
                c1 = c[0]
                ind2 = ind - 0.01
            if text.__len__() - 1 == 2:
                c1 = c[0] + c[1]
                ind2 = ind - 0.02
            if text.__len__() - 1 == 3:
                c1 = c[0] + c[1] + c[2]
                ind2 = ind - 0.03

    if text.__contains__(c1):
        t.replace(ind2,ind,c)


base=tk.Tk()
base.geometry("600x600")
t=Text(width=200,height=300)
t.place(x=0,y=0)
t1=tk.Text(width=50,height=400)
t1.place(x=220,y=0)
t1.config(state=DISABLED)
t.bind("<KeyRelease>",sug)
t.bind("<Return>",dell)
t1.bind("<Double-1>",copy)
base.mainloop()