from tkinter import*
def plus():
    n1=int(e.get())
    n2=int(e2.get())
    np=n1+n2
    l2.config(text='answer= '+str(np))
def minus():
    n1=int(e.get())
    n2=int(e2.get())
    nm=n1-n2
    l2.config(text='answer= '+str(nm))
def multiply():
    n1=int(e.get())
    n2=int(e2.get())
    nm2=n1*n2
    l2.config(text='answer= '+str(nm2))
def divide():
    n1=int(e.get())
    n2=int(e2.get())
    nd=n1/n2
    l2.config(text='answer= '+str(nd))
r=Tk()
r.geometry('500x500')
r.title('ASLAN')
r.config(bg='#D1FF33')

l=Label(r,text='ASLAN',bg='#D1FF33',fg='blue',font=('Times new Roman',25,'bold'))
l.place(relx=0.36,rely=0.17)

l2=Label(r,text='answer=',bg='#D1FF33',fg='blue',font=('Times new Roman',20,'bold'))
l2.place(relx=0.53,rely=0.34)



e=Entry(r,width=10)
e.place(relx=0.31,rely=0.30)

e2=Entry(r,width=10)
e2.place(relx=0.62,rely=0.30)

b1=Button(r,text='+',command=plus)
b1.place(relx=0.45,rely=0.30)

b2=Button(r,text='-',command=minus)
b2.place(relx=0.50,rely=0.30)

b3=Button(r,text='*',command=multiply)
b3.place(relx=0.54,rely=0.30)

b4=Button(r,text='/',command=divide)
b4.place(relx=0.58,rely=0.3)


