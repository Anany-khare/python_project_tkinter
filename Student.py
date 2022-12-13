from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import csv

def Student():
    window=Tk()
    window.title("Students")
    
    def announcement():
        f=open("Announcement.txt","r")
        r=f.read()
        nwindow=Tk()
        
        label=Label(nwindow,text=r)
        label.config(font=('Helvetica',23,"bold"))
        label.pack()
        
    def Hw():
        f=open("Homework.txt","r")
        r=f.read()
        nwindow=Tk()
        
        label=Label(nwindow,text=r)
        label.config(font=('Helvetica',23,"bold"))
        label.pack()
        
    def Personal():
        new_window = Tk()
        new_window.title("Login page")
        window.destroy()
        
        label1=Label(new_window,text='Please Enter Your Name: \n')
        label1.config(font=('Helvetica',13))
        label1.pack()
        
        name= Entry(new_window,width = '25')
        name.pack()
        
        label=Label(new_window,text='Please Enter the Password: \n')
        label.config(font=('Helvetica',13))
        label.pack()
        
        passcode = Entry(new_window, width = '25')
        passcode.pack()
        def Back():    
            new_window.destroy()
            Student()
            
        def student_details():
            
            n=name.get()
            p=passcode.get()
            f=open("Lststd.csv",'r',newline="\r\n")
            fr=csv.reader(f)
            k=0
            for i in fr:
                if n==i[1] and p==i[3]:
                    k+=1
                    nw=Tk()
                    new_window.destroy()
                    label=Label(nw,text='Welcome')
                    label.config(font=('Helvetica',20))
                    label.pack()
                    
                    f=open("Lststd.csv","r",newline='\r\n')
                    ro=csv.reader(f)
                    c=1
                    
                    for i in ro:
                        if i[1]==n:
                            drn="Roll_number:",i[0]
                            dnm="Name:",i[1]
                            dphn="Phone_number",i[2]
                            dpw="Password:",i[3]
                            c=1
                            
                            break
                        else:
                            c=0
                            
                    if c==1:
                        label=Label(nw,text=drn)
                        label.config(font=('Helvetica',20))
                        label.pack()
                        label=Label(nw,text=dnm)
                        label.config(font=('Helvetica',20))
                        label.pack()
                        label=Label(nw,text=dphn)
                        label.config(font=('Helvetica',20))
                        label.pack()
                        label=Label(nw,text=dpw)
                        label.config(font=('Helvetica',20))
                        label.pack()
                        
                else:
                    k+=0         
            if k==0:
                messagebox.showerror("Popup","Incorrect Credentials")
            
            def back():
                nw.destroy()
                Student()

            try:
                b5=Button(nw,text="Back",command=back)
                b5.config(font=('Helvetica',15,'bold','italic'),bg='#0000ff',fg='#f8e5df',activebackground='#ababab')
                b5.pack()
            except:
                x=1
        
        b3=Button(new_window,text="Login",command=student_details)
        b3.config(font=('Helvetica',15,'bold','italic'),bg='#0000ff',fg='#f8e5df',activebackground='#ababab')
        b3.pack()

        b4=Button(new_window,text="Back",command=Back)
        b4.config(font=('Helvetica',15,'bold','italic'),bg='#0000ff',fg='#f8e5df',activebackground='#ababab')
        b4.pack()
       
    b1=Button(window,text=" Announcement ",command=announcement)
    b2=Button(window,text="Profile Login",command=Personal)
    b3=Button(window,text="See Home Work",command=Hw)
    
    b1.config(font=("Helvetica",20,'bold','italic'),bg='#FF0000',fg='#fff83a',activebackground='#ababab')
    b2.config(font=('Helvetica',20,'bold','italic'),bg='#FF0000',fg='#fff83a',activebackground='#ababab')
    b3.config(font=('Helvetica',20,'bold','italic'),bg='#FF0000',fg='#fff83a',activebackground='#ababab')
    
    label=Label(window,text='What do you want to \nselect:')
    label.config(font=('Helvetica',25))
    label.pack()
    
    b1.pack(side="left")
    b2.pack(side="left")
    b3.pack(side="left")
    
    window.mainloop()
