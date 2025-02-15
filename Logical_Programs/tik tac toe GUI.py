from tkinter import *
from tkinter import messagebox
i=0
j=0
k = 1
p1=0
p2=0
d=0
tt=[]
def player(s,l,bb):
    global i,c,tt,k
    if i%2==0 and s["text"]!="O" and s["text"]!="X":
        s.configure(text="X",fg="Red")
        k=k+1
        i = i + 1

    if i%2!=0 and s["text"]!="X" and s["text"]!="O":
        s.configure(text="O",fg="Yellow")
        k=k+1
        i=i+1
    def check(tt):
        global i,d, k, j, p1, p2
        if (tt[0]['text'] == "X" and tt[1]['text'] == "X" and tt[2]['text'] == "X" or
                tt[3]['text'] == "X" and tt[4]['text'] == "X" and tt[5]['text'] == "X" or
                tt[6]['text'] == "X" and tt[7]['text'] == "X" and tt[8]['text'] == "X" or
                tt[0]['text'] == "X" and tt[3]['text'] == "X" and tt[6]['text'] == "X" or
                tt[1]['text'] == "X" and tt[4]['text'] == "X" and tt[7]['text'] == "X" or
                tt[2]['text'] == "X" and tt[5]['text'] == "X" and tt[8]['text'] == "X" or
                tt[0]['text'] == "X" and tt[4]['text'] == "X" and tt[8]['text'] == "X" or
                tt[2]['text'] == "X" and tt[4]['text'] == "X" and tt[6]['text'] == "X"):
            messagebox.showinfo("Congratulation","Player 1 Wins")
            p1 = p1 + 1
            j = j + 1
            i=0
            k=0
            l.configure(text=j+1)
            bb.focus_set()
            for zz in tt:
                zz.configure(text="")

        if (tt[0]['text'] == "O" and tt[1]['text'] == "O" and tt[2]['text'] == "O" or
                tt[3]['text'] == "O" and tt[4]['text'] == "O" and tt[5]['text'] == "O" or
                tt[6]['text'] == "O" and tt[7]['text'] == "O" and tt[8]['text'] == "O" or
                tt[0]['text'] == "O" and tt[3]['text'] == "O" and tt[6]['text'] == "O" or
                tt[1]['text'] == "O" and tt[4]['text'] == "O" and tt[7]['text'] == "O" or
                tt[2]['text'] == "O" and tt[5]['text'] == "O" and tt[8]['text'] == "O" or
                tt[0]['text'] == "O" and tt[4]['text'] == "O" and tt[8]['text'] == "O" or
                tt[2]['text'] == "O" and tt[4]['text'] == "O" and tt[6]['text'] == "O"):
            messagebox.showinfo("Congratulation","Player 2 Wins")
            p2 = p2 + 1
            j = j + 1
            i=0
            k=0
            bb.focus_set()
            l.configure(text=j+1)
            for zz in tt:
                zz.configure(text="")
        elif k == 9:
            messagebox.showwarning("Drawn","The match has been drawn")
            d = d + 1
            j=j+1
            k=0
            bb.focus_set()
            l.configure(text=j+1)
            i=0
            for zz in tt:
                zz.configure(text="")
        tt[9].delete(0,END)
        tt[9].insert(0, p1)
        tt[10].delete(0, END)
        tt[10].insert(0, p2)
        tt[11].delete(0, END)
        tt[11].insert(0, d)

    check(tt)

    if j==c:
        if p1>p2:
            messagebox.showinfo("Game Over", "The Winner of the game is Player 1")
        if p2>p1:
            messagebox.showinfo("Game Over", "The Winner of the game is Player 2")
        if p1==p2:
            messagebox.showinfo("Game Over", "The Game has been Drawn")
        base.destroy()
def game():
    global j,tt,c
    c=int(sp.get())
    a=e1.get()
    b=e2.get()
    base1=Toplevel(base)
    base1.geometry("500x600")
    base1.title("Game Starts")
    l1 = Label(base1, text="Player 1:", font=("Arial Bold", 14))
    l1.grid(row=0, column=0)
    e3 = Entry(base1, width=30, font=("Times New Roman", 13, "bold", "italic"))
    e3.place(x=123, y=0)
    e3.insert(0, a)
    e4 = Entry(base1, width=30, font=("Times New Roman", 13, "bold", "italic"))
    e4.place(x=123, y=28)
    e4.insert(0, b)
    l2 = Label(base1, text="Player 2:", font=("Arial Bold", 14))
    l2.grid(row=1, column=0)
    l3 = Label(base1, text="Round", font=("Arial Bold", 14),fg="Red")
    l3.place(x=410, y=3)
    l4 = Label(base1, text=j+1, font=("Arial Bold", 14))
    l4.place(x=435, y=25)
    b1 = Button(base1, width=15, height=7, bg="Black", command=lambda: player(b1,l4,base1), font=("Arial Bold", 12))
    b1.grid(row=3, column=0)
    b2 = Button(base1, width=15, height=7, bg="Black", command=lambda: player(b2,l4,base1), font=("Arial Bold", 12))
    b2.grid(row=3, column=1)
    b3 = Button(base1, width=15, height=7, bg="Black", command=lambda: player(b3,l4,base1), font=("Arial Bold", 12))
    b3.grid(row=3, column=2)
    b4 = Button(base1, width=15, height=7, bg="Black", command=lambda: player(b4,l4,base1), font=("Arial Bold", 12))
    b4.grid(row=4, column=0)
    b5 = Button(base1, width=15, height=7, bg="Black", command=lambda: player(b5,l4,base1), font=("Arial Bold", 12))
    b5.grid(row=4, column=1)
    b6 = Button(base1, width=15, height=7, bg="Black", command=lambda: player(b6,l4,base1), font=("Arial Bold", 12))
    b6.grid(row=4, column=2)
    b7 = Button(base1, width=15, height=7, bg="Black", command=lambda: player(b7,l4,base1), font=("Arial Bold", 12))
    b7.grid(row=5, column=0)
    b8 = Button(base1, width=15, height=7, bg="Black", command=lambda: player(b8,l4,base1), font=("Arial Bold", 12))
    b8.grid(row=5, column=1)
    b9 = Button(base1, width=15, height=7, bg="Black", command=lambda: player(b9,l4,base1), font=("Arial Bold", 12))
    b9.grid(row=5, column=2)
    ll1=Label(base1,text=a,font=("Arial Bold", 14))
    ll1.grid(row=6,column=0)
    ee1=Entry(base1,width=14,font=("Times New Roman", 13, "bold"))
    ee1.grid(row=6,column=1)
    ll2=Label(base1,text=b,font=("Arial Bold",14))
    ll2.grid(row=7,column=0)
    ee2 = Entry(base1, width=14, font=("Times New Roman", 13, "bold"))
    ee2.grid(row=7, column=1)
    ll3=Label(base1,text="Draw",font=("Arial Bold",14))
    ll3.grid(row=8,column=0)
    ee3 = Entry(base1, width=14, font=("Times New Roman", 13, "bold"))
    ee3.grid(row=8, column=1)
    tt = [b1, b2, b3, b4, b5, b6, b7, b8, b9,ee1,ee2,ee3]

    base1.mainloop()


base=Tk()
base.geometry("650x650")
base.title("Tik tac Toe")
photo=PhotoImage(file=r"Resources/class.png")
b=Label(image=photo)
b.place(x=0,y=0)
l1=Label(text="Enter the name form player 1",font=("Arial Bold",14))
l1.place(x=140,y=260)
e1=Entry(width=30,bd=3,font=("Times New Roman",13,"bold","italic"))
e1.place(x=142,y=285)
ll=Label(text="Rounds",font=("Arial Bold",14))
ll.place(x=500,y=300)
t=(1,2,3,4,5)
sp=Spinbox(values=t,width=6,font=("Times New Roman",13,"bold"))
sp.place(x=505,y=325)
l2=Label(text="Enter the name form player 2",font=("Arial Bold",14))
l2.place(x=140,y=360)
e2=Entry(width=30,bd=3,font=("Times New Roman",13,"italic","bold"))
e2.place(x=142,y=385)
bb=Button(text="Submit",font=("Arial Bold",14),bg="Yellow",bd=3,command=game)
bb.place(x=250,y=450)
l=Label(text="Tik Tac Toe",font=("Jokerman",36))
l.place(x=300,y=70)
base.mainloop()