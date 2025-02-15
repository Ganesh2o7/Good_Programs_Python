from tkinter import *
z=""
z1=""
sy=""
c=0
i=0
cc=1
sy =""
count=0
co=0
def combine(aa):
    global count
    global z
    global i
    global co
    if count == 0:
        co=co+1
        tx1.delete(0,END)
    tx2.delete(0,END)
    z = z + aa
    aa=""
    tx1.insert(str(tx1.get()).__len__(),str(z))
    tx2.insert(0, str(z))
    if co==4:
        co=co-2
    if count > 0 and co>2 and co<4:
        zz = str(tx1.get())
        tx1.delete(zz.__len__()-1,END)
    if aa=="x":
        z=""
        tx2.delete(0,END)
        tx1.delete(0,END)
    i=i+1
    co=co+1
def operation(s):
    global z
    global z1
    global c
    global sy
    global i
    global count
    count=1
    sy=s
    tx1.insert(str(tx1.get()).__len__(),s)
    i=i+1
    z1=z
    z="0"
    a=float(z1)
    b=float(z)
    if s=="+":
        c=a+b+c
    if s == "-":
        c = a - b - c
        z=0
        z1=0
    if s == "X":
        global cc
        cc = cc * a
        z=0
        z1=0
    if s == "/":
        b=1
        c = a/b
    z=""
    tx2.delete(0,END)
def op1(g):
    global z
    global z1
    global sy
    global c
    global cc
    global i
    global count
    global co
    count = count + 1
    tx1.insert(str(tx1.get()).__len__(),g)
    i=i+1
    a = float(z)
    if sy=="+":
        c=c+a
        z = 0
        z1 = 0
    if sy == "-":
        c = c-a
        z = 0
        z1 = 0
    if sy == "X":
        cc = cc * a
        c=cc
        z = 0
        z1 = 0
    if sy == "/":
        c = c/a
        z=0
        z1=0
    if g=="=":
        tx2.delete(0,END)
        tx2.insert(0,str(int(c)))
        tx1.insert(str(tx1.get()).__len__(),str(int(c)))
        c=0
    if g=="c":
        tx1.delete(0,END)
        tx2.delete(0,END)
        c=0
        cc=1
        i=0
        sy=""
        z=''
        z1=''
        count=0
        co=0
    if g=="x":
        combine("x")
        operation("x")

base= Tk()
base.geometry("257x480")
b=Button(font={"Arial Black",18},height=1,width=1)
bb=Button(font={"Arial Black",18},height=1,width=1,bd=0)
b.grid(row=0,column=0)
bb.grid(row=1,column=0)
tx1=Entry(width=28,font={"Arial Black",100})
tx1.place(x=0,y=0)
tx=Entry(width=28,font={"Arial Black",100})
tx.place(x=0,y=20)
tx2=Entry(width=28,font={"Arial Black",100})
tx2.place(x=0,y=20)
b1=Button(text="1",font={"Arial Black",18},height=3,width=6,command=lambda :combine("1"))
b1.grid(row=3,column=0)
b2=Button(text="2",font={"Arial Black",18},height=3,width=6,command=lambda :combine("2"))
b2.grid(row=3,column=1)
b3=Button(text="3",font={"Arial Black",18},height=3,width=6,command=lambda :combine("3"))
b3.grid(row=3,column=2)
b4=Button(text="+",font={"Arial Black",18},height=3,width=6,bg="Black",fg="White",command=lambda :operation("+"))
b4.grid(row=3,column=3)
b5=Button(text="4",font={"Arial Black",18},height=3,width=6,command=lambda :combine("4"))
b5.grid(row=4,column=0)
b6=Button(text="5",font={"Arial Black",18},height=3,width=6,command=lambda :combine("5"))
b6.grid(row=4,column=1)
b7=Button(text="6",font={"Arial Black",18},height=3,width=6,command=lambda :combine("6"))
b7.grid(row=4,column=2)
b8=Button(text="-",font={"Arial Black",18},height=3,width=6,bg="Black",fg="White",command=lambda :operation("-"))
b8.grid(row=4,column=3)
b9=Button(text="7",font={"Arial Black",18},height=3,width=6,command=lambda :combine("7"))
b9.grid(row=5,column=0)
b10=Button(text="8",font={"Arial Black",18},height=3,width=6,command=lambda :combine("8"))
b10.grid(row=5,column=1)
b11=Button(text="9",font={"Arial Black",18},height=3,width=6,command=lambda :combine("9"))
b11.grid(row=5,column=2)
b12=Button(text="X",font={"Arial Black",18},height=3,width=6,bg="Black",fg="White",command=lambda :operation("X"))
b12.grid(row=5,column=3)
b13=Button(text="00",font={"Arial Black",18},height=3,width=6,command=lambda :combine("00"))
b13.grid(row=6,column=0)
b14=Button(text=".",font={"Arial Black",18},height=3,width=6,command=lambda :combine("."))
b14.grid(row=6,column=1)
b15=Button(text="0",font={"Arial Black",18},height=3,width=6,command=lambda :combine("0"))
b15.grid(row=6,column=2)
b16=Button(text="/",font={"Arial Black",18},height=3,width=6,bg="Black",fg="White",command=lambda :operation("/"))
b16.grid(row=6,column=3)
b17=Button(text="C",font={"Arial Black",18},height=3,width=8,bg="Black",fg="White",command=lambda:op1("c"))
b17.place(x=3,y=335)
b18=Button(text="<X",font={"Arial Black",18},height=3,width=8,bg="Black",fg="White",command=lambda:op1("x"))
b18.place(x=88,y=335)
b18=Button(text="=",font={"Arial Black",18},height=3,width=8,bg="Black",fg="White",command=lambda:op1("="))
b18.place(x=172,y=335)
base.mainloop()