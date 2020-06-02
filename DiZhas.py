from tkinter import*
from tkinter import messagebox
import pickle



        
        

r=Tk()
r.geometry('330x400')
r.title('DiZhas')
r.config(bg='light blue')

def reg():
    text=Label(text='до входа в DiZhas зарегистрируйтесь',bg='light gray',fg='black')
    text.pack()

    text_log=Label(text='логин:',bg='light gray',fg='black')
    text_log.pack()

    reg_login=Entry()
    reg_login.pack()

    text_p1=Label(text='введите пароль',bg='light gray',fg='black')
    text_p1.pack()

    reg_p1=Entry(show='*')
    reg_p1.pack()

    text_p2=Label(text='повторите пароль',bg='light gray',fg='black')
    text_p2.pack()

    reg_p2=Entry(show='*')
    reg_p2.pack()

    b_reg=Button(text='зарегистритроваться',bg='light gray',fg='black',command=lambda:save())
    b_reg.pack()

    def save():
        log_s={}
        log_s[reg_login.get()]=reg_p1.get()
        f=open('login.txt','wb')
        pickle.dump(log_s,f)
        f.close()
        log()
        

def log():
    text_log=Label(text='регистрация прошла успешно',bg='light gray',fg='black')
    text_log.pack()

    text_e=Label(text='введите логин',bg='light gray',fg='black')
    text_e.pack()

    e_log=Entry()
    e_log.pack()

    text_p=Label(text='введите пароль',bg='light gray',fg='black')
    text_p.pack()

    e_pass=Entry(show='*')
    e_pass.pack()

    b_e=Button(text='войти',bg='light gray',fg='black',command=lambda:log_p())
    b_e.pack()

    def log_p():
        f= open('login.txt','rb')
        a=pickle.load(f)
        f.close()
        if e_log.get() in a:
            if e_pass.get()== a[e_log.get()]:
                messagebox.showinfo('вход выполнен','вы вошел в свой аккаунт')
                r2=Tk()
                r2.geometry('330x400')
                r2.title('DiZhas')
                r2.config(bg='light green')

                l1=Label(r2,text='GAME by DiZhas',bg='light green',fg='black',font=('Times new roman',20,'bold'))
                l1.place(relx=0.17,rely=0.06)
                
                l2=Label(r2,text='APPS by DiZhas',bg='light green',fg='black',font=('times new roman',20,'bold'))
                l2.place(relx=0.17,rely=0.28)
                
                b1=Button(r2,text='Paint',bg='yellow',fg='blue',font=('times new roman',16))
                b1.place(relx=0.28,rely=0.16)

                b2=Button(r2,text='Calculator',bg='red',fg='blue',font=('times new roman',16))
                b2.place(relx=0.28,rely=0.38)

                b3=Button(r2,text='Clock',bg='white',fg='black',font=('times new roman',16))
                b3.place(relx=0.28,rely=0.49)
            else:
                messagebox.showerror('ОШИБКА','неверный логин или пароль')

reg()




    



    
    






