import Management
import Teacher
import Student
from tkinter import*

window=Tk()

def Stdnt():
    
    window.destroy()
    Student.Student()
    
def Tchr():
    
    window.destroy()
    Teacher.Teacher()
    
def Mngmnt():
    
    window.destroy()
    Management.Management()
    
b1=Button(window,text=" Student ",command=Stdnt)
b2=Button(window,text="Teacher",command=Tchr)
b3=Button(window,text="Management",command=Mngmnt)
    
b1.config(font=("Helvetica",20,'bold','italic'),bg='#FF0000',fg='#fff83a',activebackground='#ababab')
b2.config(font=('Helvetica',20,'bold','italic'),bg='#FF0000',fg='#fff83a',activebackground='#ababab')
b3.config(font=('Helvetica',20,'bold','italic'),bg='#FF0000',fg='#fff83a',activebackground='#ababab')
    
label=Label(window,text='Select:')
label.config(font=('Helvetica',25))
label.pack()
    
b1.pack(side="left")
b2.pack(side="left")
b3.pack(side="left")

window.mainloop()
