from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv

def Management():
    
    def seelist():
        nwin=Tk()
        f=open("Lststd.csv",'r',newline='\r\n')
        ro=csv.reader(f)
        
        for i in ro:
            prnt="Roll_no:",i[0],"->Name:",i[1],"Phone_no.:",i[2],"Password:",i[3]
            
            label=Label(nwin,text=prnt)
            label.config(font=('Helvetica',20))
            label.pack()

        f.close()
        
    def manage():
        un=username.get()
        pc=passcode.get()
        
        if un=="Management@ggea" and pc=="gyan@ganga@mgr":
            
            def Addmision():
                
                nwindow = Tk()
                new_window.destroy()
                nwindow.title("Add student:")
                
                label=Label(nwindow,text='Roll number of the Student: \n')
                label.config(font=('Helvetica',13))
                label.pack()
                
                rlno= Entry(nwindow, width = '25')
                rlno.pack()
                
                label=Label(nwindow,text='Name of the Student: \n')
                label.config(font=('Helvetica',13))
                label.pack()
                
                nm= Entry(nwindow, width = '25')
                nm.pack()
                
                label=Label(nwindow,text='Phone number of the Student: \n')
                label.config(font=('Helvetica',13))
                label.pack()
                
                phno= Entry(nwindow, width = '25')
                phno.pack()
                
                label=Label(nwindow,text='Password of the Student: \n')
                label.config(font=('Helvetica',13))
                label.pack()
                
                paswd= Entry(nwindow, width = '25')
                paswd.pack()
                def Back():                   
                    nwindow.destroy()
                    Management()
                
                def save():
                    lst=open('Lststd.csv','a')
                    roll=rlno.get()
                    name=nm.get()
                    phn=phno.get()
                    pswd=paswd.get()
                    
                    data=[roll,name,phn,pswd]
                    wo=csv.writer(lst)
                    wo.writerow(data)
                    lst.close()
                    
                    label=Label(nwindow,text='Submitted')
                    label.config(font=('Helvetica',19))
                    label.pack()
                    
                b1=Button(nwindow,text="Submit details",command=save)
                b1.config(font=('Helvetica',15,'bold','italic'),bg='#0000ff',fg='#f8e5df',activebackground='#ababab')
                b1.pack()

                b2=Button(nwindow,text="Back",command=Back)
                b2.config(font=('Helvetica',15,'bold','italic'),bg='#0000ff',fg='#f8e5df',activebackground='#ababab')
                b2.pack()
            

            def Search():
                win=Tk()
                new_window.destroy()
                
                label=Label(win,text="Enter Roll number you want to edit ")
                label.config(font=("Helvetica",13))
                label.pack()
                
                rlc=Entry(win,width='25')
                rlc.pack()

            def addannouncement():
                nwindow1=Tk()
                new_window.destroy()
                
                label=Label(nwindow1,text="Add an announcement")
                label.config(font=("Helvetica",13))
                label.pack()
                
                announcement = Entry(nwindow1, width = '25')
                announcement.pack()
                
                def announcemnt():
                    f=open("Announcement.txt","w")
                    announce=announcement.get()
                    w=f.write(announce)
                    f.close()
                def back():
                    nwindow1.destroy()
                    Management()
                    
                b1=Button(nwindow1,text="Add",command=announcemnt)
                b1.config(font=("Helvetica",15,'bold'),bg='#0000ff',fg='#f8e5df',activebackground='#ababab')
                b1.pack()
                b2=Button(nwindow1,text="Back",command=back)
                b2.config(font=("Helvetica",15,'bold'),bg='#0000ff',fg='#f8e5df',activebackground='#ababab')
                b2.pack()
                
            new_window = Tk()
            window.destroy()
            
            b1=Button(new_window,text="Add Student details",command=Addmision)
            b1.config(font=('Helvetica',15,'bold','italic'),bg='#0000ff',fg='#f8e5df',activebackground='#ababab')
            b1.pack()

            '''
            b2=Button(new_window,text="Search Student details",command=Search)
            b2.config(font=('Helvetica',15,'bold','italic'),bg='#0000ff',fg='#f8e5df',activebackground='#ababab')
            b2.pack()
            '''
            b3=Button(new_window,text="See Student details",command=seelist)
            b3.config(font=('Helvetica',15,'bold','italic'),bg='#0000ff',fg='#f8e5df',activebackground='#ababab')
            b3.pack()
            
            b4=Button(new_window,text="Add Announcement",command=addannouncement)
            b4.config(font=('Helvetica',15,'bold','italic'),bg='#0000ff',fg='#f8e5df',activebackground='#ababab')
            b4.pack()
        else:
            messagebox.showerror("Popup","Incorrect Username/Password")
            
    window=Tk()
    window.title("Management Login")
    
    label1=Label(window,text='Please Enter Your Username: \n')
    label1.config(font=('Helvetica',13))
    label1.pack()
    
    username= Entry(window,width = '25')
    username.pack()
    
    label=Label(window,text='Please Enter the Password: \n')
    label.config(font=('Helvetica',13))
    label.pack()
    
    passcode = Entry(window, width = '25')
    passcode.pack()
    
    b1=Button(window,text="Login",command=manage)
    b1.config(font=('Helvetica',15,'bold','italic'),bg='#0000ff',fg='#f8e5df',activebackground='#ababab')
    b1.pack()
