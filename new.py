from random import sample
from Tkinter import *
from tkMessageBox import *
import sqlite3
con=sqlite3.Connection("alpha")
cur=con.cursor()
cur.execute("create table if not exists login(enr_no varchar(10) unique,password varchar(20))")
ran=sample(range(1,6),5)
marks=0
counter=0
j=0
def new_window(a):
        root.destroy()
        root2=Tk()
        root2.geometry('1366x786')
        root2.title("Rules")
        root2.configure(bg='#a5ff4d')
        Label(root2,text="Welcome "+a,font="Arial 12 italic bold",bg='#a5ff4d',fg='black',height=2).place(x=1220,y=10)
        Button(root2,text="Start Quiz",command=lambda:quiz(a,root2),bg='blue',fg='white',height=4,width=20).place(x=530,y=500)
        l=Label(root2,bg='#a5ff4d',fg='black',font='arial 18 ',text='Rules for the QUIZ\n1.After clicking the "Start Quiz" button, the quiz will appear.\n2. The first question will appear after first 10 seconds\n3. Each question is a MCQ.\n4. You have to select one option and click "LOCK" button\n5.You have to press SUMIT key only once\n6. Negative marking will be done if LOCK is pressed twice')
        l.place(x=300,y=100)
        root2.mainloop()
### new signup window---------------------------------------------------------------------------------------
def insert():
        root1=Tk()
        root1.geometry("800x600")
        root1.title("new sign up")
        Label(root1,text='Enrollment number',font="times 20 bold").grid(row=1,column=1)
        Label(root1,text='Password',font="times 20 bold").grid(row=2,column=1)
        e3=Entry(root1,font="times 17 bold",width=25)
        e3.grid(row=1,column=3)
        e4=Entry(root1,font="times 17 bold",width=25)
        e4.grid(row=2,column=3)
        def signup():
                a=e3.get()
                b=e4.get()
                cur.execute('select count(enr_no) from login where enr_no=(+"a")')
                r=cur.fetchall()
                c=r[0]
                if(c[0]!=0):
                        showerror(title='Signup',message='You have are already signed up')
                        root1.destroy()
                else:
                        cur.execute("insert into login values(?,?)",(a,b))
                        con.commit()
                        showinfo(title='Signup',message='You have been signed up')
                        root1.destroy()
        Button(root1,text="signup",command=signup,width=5,height=1,bg="gold",font="time 12",bd=5).grid(row=3,column=1)



##############################################################################################
def quiz(enr,root2):

        root2.destroy()
        root3=Tk()
        root3.geometry('1366x786')
        root3.title("Quiz For You ")

        def calculate():
                global marks
                v=var.get()
                var.set(-1)
                v=int(v)
                if v==1:
                    marks=marks+v

        def result():
                showinfo(title='RESULTS',message='Your Marks are '+str(marks)+'\n Thank u for using this Quiz')
                root3.destroy()
        global background
        background=PhotoImage(file='background.gif')
        Label(root3,image=background).place(x=20,y=0)
        Label(root3,text='Welcome '+enr,font='arial 20 italic',fg='white',bg='black').place(x=1050,y=10)
        def counter_label(label):
                def count():
                        global ran
                        global j
                        global counter
                        if counter==10 and j<5:
                                counter=0
                                k=ran[j]
                                dic.get(k)()
                                j+=1
                        if counter==11:
                                result()
                                return
                        counter+=1
                        label.config(text=str(counter))
                        label.after(1000,count)
                count()
    
        back=PhotoImage(file='frame.gif')
    
        label=Label(root3,fg='green',font='arial 50 bold',height=1,width=2,bg='black')
        label.place(x=620,y=170)
        counter_label(label)
        var=IntVar()
        var.set(-1)

        def q1():       
                frame=Frame(root3,bg='black',height=350,width=1300)
                Label(frame,image=back,height=350,width=1300).place(x=0,y=0)
                Label(frame,text='Who is the Father of Computers?',font='courier 30 italic',bg='pink').place(x=200,y=50)
                Radiobutton(frame,text='Charles Babbage',variable=var,value=1,bg='pink',font='arial 20 bold').place(x=250,y=170)
                Radiobutton(frame,text='Robert Volar',variable=var,value=2,bg='pink',font='arial 20 bold').place(x=250,y=260)
                Radiobutton(frame,text='Dennis Ritche',variable=var,value=3,bg='pink',font='arial 20 bold').place(x=800,y=170)
                Radiobutton(frame,text='Steve Jobs',variable=var,value=4,bg='pink',font='arial 20 bold').place(x=800,y=260)
                frame.place(x=10,y=400)
                Button(frame,text='LOCK',font='arial 10 bold',fg='white',bg='green',height=2,width=4,command=calculate).place(x=630,y=220)

        def q2():       
                frame=Frame(root3,bg='black',height=350,width=1300)
                Label(frame,image=back,height=350,width=1300).place(x=0,y=0)
                Label(frame,text='One kilobyte is equal to?',font='courier 30 italic',bg='pink').place(x=200,y=50)
                Radiobutton(frame,text='1000 bytes',variable=var,value=4,bg='pink',font='arial 20 bold').place(x=250,y=170)
                Radiobutton(frame,text='1023 bytes',variable=var,value=2,bg='pink',font='arial 20 bold').place(x=250,y=260)
                Radiobutton(frame,text='100 bytes',variable=var,value=3,bg='pink',font='arial 20 bold').place(x=800,y=170)
                Radiobutton(frame,text='1024 bytes',variable=var,value=1,bg='pink',font='arial 20 bold').place(x=800,y=260)
                frame.place(x=10,y=400)
                Button(frame,text='LOCK',font='arial 10 bold',fg='black',bg='green',height=2,width=4,command=calculate).place(x=630,y=220)
        def q3():       
                frame=Frame(root3,bg='black',height=350,width=1300)
                Label(frame,image=back,height=350,width=1300).place(x=0,y=0)
                Label(frame,text='Which of the following is not an OS?',font='courier 30 italic',bg='pink').place(x=200,y=50)
                Radiobutton(frame,text='Windows 98',variable=var,value=3,bg='pink',font='arial 20 bold').place(x=250,y=170)
                Radiobutton(frame,text='BSD Unix',variable=var,value=2,bg='pink',font='arial 20 bold').place(x=250,y=260)
                Radiobutton(frame,text='Microsoft Office',variable=var,value=1,bg='pink',font='arial 20 bold').place(x=800,y=170)
                Radiobutton(frame,text='Red Hat Linux',variable=var,value=4,bg='pink',font='arial 20 bold').place(x=800,y=260)
                frame.place(x=10,y=400)
                Button(frame,text='LOCK',font='arial 10 bold',fg='black',bg='green',height=2,width=4,command=calculate).place(x=630,y=220)
        def q4():       
                frame=Frame(root3,bg='black',height=350,width=1300)
                Label(frame,image=back,height=350,width=1300).place(x=0,y=0)
                Label(frame,text='Check the odd term?',font='courier 30 italic',bg='pink').place(x=200,y=50)
                Radiobutton(frame,text='Linux',variable=var,value=2,bg='pink',font='arial 20 bold').place(x=250,y=170)
                Radiobutton(frame,text='Internet',variable=var,value=1,bg='pink',font='arial 20 bold').place(x=250,y=260)
                Radiobutton(frame,text='Unix',variable=var,value=3,bg='pink',font='arial 20 bold').place(x=800,y=170)
                Radiobutton(frame,text='Windows',variable=var,value=4,bg='pink',font='arial 20 bold').place(x=800,y=260)
                frame.place(x=10,y=400)
                Button(frame,text='LOCK',font='arial 10 bold',fg='black',bg='green',height=2,width=4,command=calculate).place(x=630,y=220)

        def q5():       
                frame=Frame(root3,bg='black',height=350,width=1300)
                Label(frame,image=back,height=350,width=1300).place(x=0,y=0)
                Label(frame,text='The errors that can be pointed by compiler?',font='courier 25 italic',bg='pink').place(x=200,y=50)
                Radiobutton(frame,text='Syantax errors',variable=var,value=1,bg='pink',font='arial 20 bold').place(x=250,y=170)
                Radiobutton(frame,text='Logical errors',variable=var,value=2,bg='pink',font='arial 20 bold').place(x=250,y=260)
                Radiobutton(frame,text='Internal errors',variable=var,value=3,bg='pink',font='arial 20 bold').place(x=800,y=170)
                Radiobutton(frame,text='Symantic errors',variable=var,value=4,bg='pink',font='arial 20 bold').place(x=800,y=260)
                frame.place(x=10,y=400)
                Button(frame,text='LOCK',font='arial 10 bold',fg='black',bg='green',height=2,width=4,command=calculate).place(x=630,y=220)
        dic={1:q1,2:q2,3:q3,4:q4,5:q5}
        root3.mainloop()
    
#############################################################################################

#Login function-----------------------------------------------------------------------------------------
def select(event=0):
        a=e1.get()
        b=e2.get()
        p=(e1.get(),)
        cur.execute("select enr_no from login where enr_no=(?)",p)
        result=cur.fetchall()
        if(len(result)==0):
                showinfo(title="First time login",message="Please Sign Up First")
        else:
                cur.execute("select password from login where enr_no=(?)",p)
                result1=cur.fetchall()
                c=result1[0]
                if(c[0]==b):
                        showinfo(title="login successful",message='login successful')
                        new_window(a)
                        #for i in root.winfo_children():
                                #i.destroy()
                else:
                        showerror(title='login failed',message="Wrong Credential")

#main window---------------------------------------------------------------------------------------------
root=Tk()
root.title("Welcome to ALPHA")
root.geometry("1366x768")
root.configure(bg='light green')
image1=PhotoImage(file="output.gif")
Label(root,image=image1).grid(row=0,column=2,sticky=N+W+S+E)
Label(root,text="Username",font='courier 20 bold').place(x=400,y=350)
e1=Entry(root)
e1.place(height=25,width=150,x=550,y=355)
Label(root,text="Password",font='courier 20 bold').place(x=400,y=400)
e2=Entry(root,show="*")
e2.bind('<Return>',select)
e2.place(height=25,width=150,x=550,y=405)
image2=PhotoImage(file='image2.gif')
Label(root,image=image2).place(x=740,y=325)
Label(root,text="New User?",font="courier 15 bold italic").place(x=10,y=650)
Button(root,text="Signup",command=insert,bg="light pink",font='arial 10 bold',bd=7).place(x=130,y=650)
Button(root,text="Login",font='arial 10 bold',height=1,width=38,bg='green',command=select,bd=7).place(x=400,y=450)

root.mainloop()
