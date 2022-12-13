from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import csv

def Teacher():
    
    def main():
        
        Name = nm.get()
        c=code.get()
        
        if c==Name+"@ggea@tchr":
            new_window= Tk()
            new_window.title("Welcome")
            window.destroy()
            
            def Homework():
                nwindow1=Tk()
                
                label=Label(nwindow1,text="Add a Home Work here")
                label.config(font=("Helvetica",13))
                label.pack()
                
                Hw = Entry(nwindow1, width = '25')
                Hw.pack()
                
                def announcemnt():
                    f=open("Homework.txt","w")
                    Homework=Hw.get()
                    w=f.write(Homework)
                    f.close()
                    
                b1=Button(nwindow1,text="Add",command=announcemnt)
                b1.config(font=("Helvetica",15,'bold'),bg='#0000ff',fg='#f8e5df',activebackground='#ababab')
                b1.pack()
                                
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
                
            def Search():
                nwind=Tk()
                f=open("Lststd.csv","r",newline='\r\n')
                ro=csv.reader(f)
                label=Label(nwind,text="Enter Roll Number to Search:")
                label.config(font=('Helvetica',20))
                label.pack()
                rl=Entry(nwind,width = '25')
                rl.pack()
                
                def srch():
                    c=1
                    b1.destroy()
                    roll=rl.get()
                    
                    for i in ro:
                        
                        if i[0]==roll:
                            prt=("Roll_number:",i[0],",Name:",i[1],",Phone_number",i[2],",Password:",i[3])
                            c=0
                            break
                        
                    if c==0:
                        label=Label(nwind,text=prt)
                        label.config(font=("Helvetica",20))
                        label.pack()                                                      
                            
                    if c==1:
                        label=Label(nwind,text="Not Found :(")
                        label.config(font=("Helvetica",13))
                        label.pack()
                        
                b1=Button(nwind,text="Search",command=srch)
                b1.config(font=("Helvetica",15,'bold'),bg='#0000ff',fg='#f8e5df',activebackground='#ababab')
                b1.pack()
                
            b1=Button(new_window,text="Add Home work",command=Homework)
            b1.config(font=("Helvetica",15,'bold'),bg='#0000ff',fg='#f8e5df',activebackground='#ababab')
            b1.pack()
           
            b3=Button(new_window,text="See Student list",command=seelist)
            b3.config(font=("Helvetica",15,'bold'),bg='#0000ff',fg='#f8e5df',activebackground='#ababab')
            b3.pack()

            b4=Button(new_window,text="Search Student details",command=Search)
            b4.config(font=("Helvetica",15,'bold'),bg='#0000ff',fg='#f8e5df',activebackground='#ababab')
            b4.pack()
      
        else:
            messagebox.showerror("popup","Incorrect teacher's code")
    window=Tk()
    window.title("Teachers")
    
    label1=Label(window,text="Enter Your name: \n")
    label1.config(font=('Helvetica',13))
    label1.pack()
    nm=Entry(window,width = '20')
    nm.pack()
   
    label=Label(window,text="Please Enter Teache code: \n")
    label.config(font=("Helvetica",13))
    label.pack()
    
    code = Entry(window, width = '25')
    code.pack()
    
    b1=Button(window,text="Login",command=main)
    b1.config(font=("Helvetica",15,'bold'),bg='#0000ff',fg='#f8e5df',activebackground='#ababab')
    b1.pack()
    window.mainloop()
Teacher()
