from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import re

class login:
    
    a=0
    b=0
    c=0
    mobile_no=0
    
    def signup(self):
        top=Tk()
        top.title("create form")
        top.geometry("500x450+425+75")
        
        self.var=IntVar()
        Label(top,text="Register Form",font="Helvetica 12 bold",height="3",width="500",fg="white",bg="black").pack()

        Label(top,text="Firstname").place(x=100,y=100)
        self.firstname = Entry(top)
        self.firstname.place(x=180,y=100)

        Label(top,text="Lastname").place(x=100,y=150)
        self.lastname=Entry(top)
        self.lastname.place(x=180,y=150)

        Label(top,text="Gender").place(x=100,y=200)
        R1=Radiobutton(top,text="Male",variable=self.var,value=1,relief=RAISED)
        R1.place(x=200,y=200)

        R2=Radiobutton(top,text="Female",variable=self.var,value=0,relief=RAISED)
        R2.place(x=300,y=200)

        Label(top,text="Mobile_No.").place(x=100,y=250)
        self.mobile_no=Entry(top)
        self.mobile_no.place(x=180,y=250)
        

        Label(top,text="Email").place(x=100,y=300)
        self.email=Entry(top)
        self.email.place(x=180,y=300)

        Label(top,text="Password:").place(x=100,y=350)
        self.password=Entry(top)
        self.password.place(x=180,y=350)

        Button(top,text="Submit",command=self.validate).place(x=170,y=400)
        top.mainloop()

    def validate(self):
        temp = self.mobile_no.get()
        l = len(temp)
        temp1=self.email.get()
        temp2=self.firstname.get()
        temp3=self.lastname.get()
        
        if (l!=10 or temp.isdigit()==False) :
            message=messagebox.showinfo("Warning...!!","INVALID MOBILE NUMBER")
            pass
        elif(temp1=='' or re.search('[@]',temp1) is None or re.search('[.]',temp1) is None):
            message=messagebox.showinfo("Warning...!!","PLEASE ENTER VALID EMAIL")
        elif(temp2==''):
            message=messagebox.showinfo("Warning...!!","PLEASE ENTER FIRSTNAME")
        elif(temp3==''):
            message=messagebox.showinfo("Warning...!!","PLEASE ENTER LASTNAME")
        else:
            self.database()


    def database(self):
        name=self.firstname.get()
        name1=self.lastname.get()
        temp=self.var.get()
        abc=int(temp)
        if abc == 1:
           g="Male"
        else:
           g="Male"
        mb=self.mobile_no.get()
        email=self.email.get()
        passw=self.password.get()
        conn=sqlite3.connect("untitled2.db")
        c=conn.cursor()
        #c.execute("CREATE TABLE form(firstname varchar(50), lastname varchar(50),gender text,mobile_no number,Email text,password text);")
        c.execute("INSERT INTO form(firstname,lastname,gender,mobile_no,Email,password)values(?,?,?,?,?,?)",(name,name1,g,mb,email,passw))
        c.execute("SELECT * from form")
        for i in c:
            print("name",i[0])
            print("name1",i[1])
            print("g",i[2])
            print("mb",i[3])
            print("email",i[4])
            print("password",i[5])                     
        c.close()
        conn.commit()

        
    def login(self):

        top=Tk()
        top.title("Login")
        top.geometry("500x400+425+75")
        Label(top,text="LOGIN PAGE",font="Helvetica 12 bold",height="3",width="500",fg="white",bg="black").pack()

        n=Label(top, text="Email").place(x=100,y=100)
        self.n1=Entry(top)
        self.n1.place(x=180,y=100)

        m=Label(top, text="Password").place(x=100,y=150)
        self.m1=Entry(top)
        self.m1.place(x=180,y=150)

        button_1=Button(top,text='SUBMIT',fg='green',command=self.valid).place(x=170,y=200)
        button_1=Button(top,text='SIGN UP',fg='green',command=self.signup).place(x=270,y=200)

        top.mainloop()

    def valid(self):
        idd=self.n1.get()
        pas=self.m1.get()
        
        if(idd=='' or re.search('[@]',idd) is None or re.search('[.]',idd) is None):
            message=messagebox.showinfo("Warning...!!","PLEASE ENTER VALID EMAIL")
        elif(pas==''):
            message=messagebox.showinfo("Warning...!!","PLEASE ENTER VALID PASSWORD")
        else:
            self.check()


    def check(self):
        conn=sqlite3.connect("untitled2.db")
        c=conn.cursor()
        if(self.n1.get() !='' and self.m1.get()!=''):
            c.execute("select email,password from form where email=? and password=?",(self.n1.get(),self.m1.get()))
            check = c.fetchone()
            print(check)
            if check is None:
                message=messagebox.showinfo("Warning...","INVALID EMAIL ID & PASSWORD.")
            elif check is not None :
                self.set_trip()
                 
        
    def set_trip(self):

        top=Tk()
        top.title("Booking Request IN LPU")
        top.geometry("500x600+425+75")
        Label(top,text="BOOKING REQUEST",font="Helvetica 12 bold",height="3",width="500",fg="white",bg="black").pack()

        lb1=Label(top,text="From Block NO.").place(x=100,y=150)
        self.b=Entry(top,width=12)
        self.b.place(x=200,y=150)

        lb2=Label(top,text="To Block No.").place(x=100,y=200)
        self.a=Entry(top,width=12)
        self.a.place(x=200,y=200)

        lb_date=Label(top,text="Date").place(x=100,y=250)
        Var=IntVar()
        Var.set(1)
        spin=Spinbox(top,from_=1,to=31,width=10,textvariable=Var)
        spin.place(x=200,y=250)

        lb_month=Label(top,text="Month").place(x=100,y=300)
        Var1=IntVar()
        Var1.set(1)
        spin=Spinbox(top,from_=1,to=12,width=10,textvariable=Var1)
        spin.place(x=200,y=300)

        lb_year=Label(top,text="Year").place(x=100,y=350)
        Var2=IntVar()
        Var2.set(2018)
        spin=Spinbox(top,from_=2018,to=2020,width=10,textvariable=Var2)
        spin.place(x=200,y=350)

        button_1=Button(top,text='SUBMIT',fg='green',command=self.validd).place(x=150,y=400)
       
        top.mainloop()
        
    def validd(self):
        fromm=self.b.get()
        too=self.a.get()
        
        if(fromm==''):
            message=messagebox.showinfo("Warning...!!","PLEASE ENTER VALID ROUTE")
        elif(too==''):
            message=messagebox.showinfo("Warning...!!","PLEASE ENTER VALID ROUTE")
        else:
            self.fare()

    def fare(self):
        w=int(self.a.get())
        q=int(self.b.get())
        if w==q:
            message=messagebox.showinfo("WARNING"," END AND START POINT OF TRIP ARE SAME ")
        elif w>57 or w<1:
            message=messagebox.showinfo("WARNING"," ENTER VALID BLOCK NUMBER FROM 1 TO 57 ") 
        elif q>57 or q<1:
            message=messagebox.showinfo("WARNING"," ENTER VALID BLOCK NUMBER FROM 1 TO 57 ")
        else:
            if q>w:
                self.c=(q-w)*2
            else:
                self.c=(w-q)*2
            s="FARE IS :"+str(self.c)    
            message=messagebox.showinfo("THANK YOU",s)

    def contact(self):

        top=Tk()
        top.title("Contact Us")
        top.geometry("500x300+425+75")

        Label(top,text="CONTACT US",font="Helvetica 12 bold",height="3",width="500",fg="white",bg="black").pack()
        o=Label(top,text="KVM CAB DELHI").place(x=100,y=100)
        o=Label(top,text="Plot No. 356 Near Miler ").place(x=100,y=120)
        o=Label(top,text="Ganj, New Delhi. 148011").place(x=100,y=140)
        o=Label(top,text="Email: KVMCAB@gmail.com").place(x=100,y=160)
        o=Label(top,text="Mob. NO. 9875641235").place(x=100,y=180)
        o=Label(top,text="Fax NO. 121454545").place(x=100,y=200)

        top.mainloop()
    
    def __init__(self):
    
        root=Tk()
        root.title("CAB MANAGEMENT SYSTEM")
        root.geometry("500x400+425+125")

        Label(root,text="WELCOME TO CAB BOOKING PORTAL",font="Helvetica 12 bold",height="3",width="500",fg="white",bg="black").pack()

        Button(root,text="Login",bg="Yellow",width="15",height="3",command=self.login,relief=RAISED).place(x="210", y="100")

        Button(root,text="New User",bg="Yellow",width="15",height="3",command=self.signup,relief=RAISED).place(x="210", y="160")
    
        Button(root,text="Available Routes",bg="Yellow",width="15",height="3",command=self.set_trip,relief=RAISED).place(x="210", y="220")

        Button(root,text="Contact Us",bg="Yellow",width="15",height="3",command=self.contact,relief=RAISED).place(x="210", y="280")
        
        root.mainloop()

        
ob=login()
    

    
    
    
