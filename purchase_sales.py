from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import sqlite3
con=sqlite3.connect("cse.db")
cur=con.cursor()
qur=('create table if not exists n1(SNO int,PRODUCT varcahr(20), QTY int,RATE int,TOTAL int)')
cur.execute(qur)
a=Tk()
a.title("welcome")
p=PhotoImage(file="sales.png")
l9=Label(a,image=p)
l9.place(relwidth=1,relheight=1)
l3=Label(a,text="WELCOME TO OUR WEBSITE",bg="black",fg="white",font=("times",40))
l3.pack(fill="x")
def sales():
    c=Tk()
    c.title("SALES")
    f=Frame(c,bd=9)
    f.pack()
    l=Label(f,text="SNO:")
    l.grid(row=0,column=0)
    e=Entry(f)
    e.grid(row=0,column=1)
    l1=Label(f,text="PRODUCT:")
    l1.grid(row=1,column=0)
    e1=Entry(f)
    e1.grid(row=1,column=1)
    l1=Label(f,text="QTY:")
    l1.grid(row=2,column=0)
    e2=Entry(f)
    e2.grid(row=2,column=1)
    l1=Label(f,text="RATE:")
    l1.grid(row=3,column=0)
    e3=Entry(f)
    e3.grid(row=3,column=1)
    def total():
        y=(int(e2.get())*int(e3.get()))
             
        e4.insert(0,y)
   
    l1=Button(f,text="TOTAL:",bg="yellow",command=total)
    l1.grid(row=4,column=0)
    e4=Entry(f)
    e4.grid(row=4,column=1)
    def sub():
        d=Tk()
        d.title("DETAILS")
        t=ttk.Treeview(d)
        t.pack(fill="x")
        t["columns"]=["SNO","PRODUCT","QTY","RATE","TOTAL"]
        t.column("#0",width=10,stretch=NO)
        t.column("#1",anchor="center")
        t.column("#2",anchor="center")
        t.column("#3",anchor="center")
        t.column("#4",anchor="center")
        t.column("#5",anchor="center")
        t.heading("#0",text="")
        t.heading("#1",text="SNO")
        t.heading("#2",text="PRODUCT")
        t.heading("#3",text="QTY")
        t.heading("#4",text="RATE")
        t.heading("#5",text="TOTAL")
        u=([1,"GINGER",3,10,30],[2,"GARLIC",10,10,100])
        for i in u:
            t.insert("",END,values=i)
        def add():
            t.insert("",END,values=(e.get(),e1.get(),e2.get(),e3.get(),e4.get()))
            e.delete(0,END)
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
       
        b5=Button(d,text="ADD",bg="grey",command=add)
        b5.pack(pady=10)
        def DEL():
            g=t.selection()
            t.delete(g)
        b6=Button(d,text="DELETE",bg="reD",command=DEL)
        b6.pack(pady=10)
        def save(a,b,c,d,q):
            a=e.get()
            b=e1.get()
            c=e2.get()
            d=e3.get()
            q=e4.get()
            qur='insert into n1(SNO,PRODUCT,QTY,RATE,TOTAL)values(?,?,?,?,?)'
            v=(a,b,c,d,q)
            cur.execute(qur,v)
            con.commit()
            d1='select*from n1'
            cur.execute(d1)
            f1=cur.fetchall()
            print(f1)

        b10=Button(d,text="SAVE",bg="green",command=save(e,e1,e2,e3,e4))
        b10.pack()
   
    b4=Button(f,text="SUBMIT",bg="grey",command=sub)
    b4.grid(row=5,column=0)
    def dis():
        d=Tk()
        d.title("DETAILS")
        t=ttk.Treeview(d)
        t.pack(fill="x")
        t["columns"]=["SNO","PRODUCT","QTY","RATE","TOTAL"]
       
        t.column("#0",width=10,stretch=NO)
        t.column("#1",anchor="center")
        t.column("#2",anchor="center")
        t.column("#3",anchor="center")
        t.column("#4",anchor="center")
        t.column("#5",anchor="center")
        t.heading("#0",text="")
        t.heading("#1",text="SNO")
        t.heading("#2",text="PRODUCT")
        t.heading("#3",text="QTY")
        t.heading("#4",text="RATE")
        t.heading("#5",text="TOTAL")
        u=([1,"GINGER",3,10,30],[2,"GARLIC",10,10,100])
        for i in u:
            t.insert("",END,values=i)
       
    b9=Button(f,text="DISPLAY",bg="orange",command=dis)
    b9.grid(row=5,column=1)
   
   
   
   
   
def purchase():
    c=Tk()
    c.title("PURCHASE")
    f=Frame(c,bd=9)
    f.pack()
    l=Label(f,text="SNO:")
    l.grid(row=0,column=0)
    e=Entry(f)
    e.grid(row=0,column=1)
    l1=Label(f,text="PRODUCT:")
    l1.grid(row=1,column=0)
    e1=Entry(f)
    e1.grid(row=1,column=1)
    l1=Label(f,text="QTY:")
    l1.grid(row=2,column=0)
    e2=Entry(f)
    e2.grid(row=2,column=1)
    l1=Label(f,text="RATE:")
    l1.grid(row=3,column=0)
    e3=Entry(f)
    e3.grid(row=3,column=1)
    def total():
        y=(int(e2.get())*int(e3.get()))
        e4.insert(0,y)
    l1=Button(f,text="TOTAL:",bg="yellow",command=total)
    l1.grid(row=4,column=0)
    e4=Entry(f)
    e4.grid(row=4,column=1)
   
   
    def sub():
        d=Tk()
        d.title("DETAILS")
        t=ttk.Treeview(d)
        t.pack(fill="x")
        t["columns"]=["SNO","PRODUCT","QTY","RATE","TOTAL"]
        t.column("#0",width=10,stretch=NO)
        t.column("#1",anchor="center")
        t.column("#2",anchor="center")
        t.column("#3",anchor="center")
        t.column("#4",anchor="center")
        t.column("#5",anchor="center")
        t.heading("#0",text="")
        t.heading("#1",text="SNO")
        t.heading("#2",text="PRODUCT")
        t.heading("#3",text="QTY")
        t.heading("#4",text="RATE")
        t.heading("#5",text="TOTAL")
        u=([1,"GINGER",10,10,100],[2,"GARLIC",10,10,100])
        for i in u:
            t.insert("",END,values=i)
        def add():
            t.insert("",END,values=(e.get(),e1.get(),e2.get(),e3.get(),e4.get()))
            e.delete(0,END)
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
       
        b5=Button(d,text="ADD",bg="grey",command=add)
        b5.pack(pady=10)
        def DEL():
            g=t.selection()
            t.delete(g)
        b6=Button(d,text="DELETE",bg="reD",command=DEL)
        b6.pack(pady=10)
        def view():
            g=t.selection()
            s=t.item(g)
            h=s["values"]
            print(h)
        b7=Button(d,text="VIEW",bg="green",command=view)
        b7.pack()
       
   
    b4=Button(f,text="SUBMIT",bg="grey",command=sub)
    b4.grid(row=5,column=0)
   
   
def login():
    if(c.get()=="s"and c1.get()=="1"):
        messagebox.showinfo("LOGIN","SUCCESSFULLY LOGINED")
        b=Tk()
        b.geometry("300x150")
        b.config(bg="grey")
        b.title("CHOOSE YOUR BUTTON")
        b1=Button(b,text="PURCHASE",bg="red",command=purchase)
        b1.pack(pady=10)
        b2=Button(b,text="SALES",bg="green",command=sales)
        b2.pack(pady=10)
       
    else:
        messagebox.showinfo("404 ERROR","PLS ENTER CORRECTLY")
   
f=Frame(a,bd=9,bg="black")
l=Label(f,text="USERNAME:",bg="white",fg="black")
l.grid(row=0,column=0,pady=3)
c=ttk.Combobox(f,width=15)
c["value"]=["DARSHAN","s"]
c.current(1)
c.grid(row=0,column=1)
l1=Label(f,text="PASSWORD:",bg="white",fg="black")
l1.grid(row=1,column=0,pady=3)
c1=ttk.Combobox(f,width=15)
c1["value"]=["12345","1"]
c1.current(1)
c1.grid(row=1,column=1)
b=Button(f,text="LOGIN",bg="green",command=login)
b.grid(row=2,column=1,pady=3)
f.place(x=500,y=500)
