from tkinter import *
from tkinter import messagebox as mb
import datetime
import hashlib
import random
from dbConnection import *
from uidGenerator import *
from password import *


def checkInstitute(tan):
    dbobj = db()
    mydb,cursor = dbobj.dbconnect("credentials")
    sql_query = "SELECT * FROM institute WHERE tan = %s"
    cursor.execute(sql_query, (tan,))
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False

def instituteInsert(uid,name,tan,email,phone,password):
    dbobj = db()
    mydb,cursor = dbobj.dbconnect("credentials")
    
    institute_query = "INSERT INTO institute (uid,name,tan,email,phone) VALUES (%s, %s, %s, %s, %s)"
    institute_data = (uid,name,tan,email,phone)
    cursor.execute(institute_query, institute_data)
    login_query = "INSERT INTO login (uid,`key`, hash) VALUES (%s, %s, %s)"
    login_data = (uid, "key", password)
    cursor.execute(login_query, login_data)
    
    mydb.commit()
    mydb.close()
    
    userID = uid
    successMessage =f"Registration Successful. Your User ID is {userID}"
    mb.showinfo("Success",successMessage)


    
def instituteSignup():
    def saveinfo():
        institute_name = e1.get()
        institute_email = e2.get()
        institute_phone = e3.get()
        institute_tan = e4.get()
        institute_password = e5.get()

        uidobj = uid(institute_tan,0)
        generated_uid = uidobj.generate_unique_12_digit_number()
        passFuncobj = passFunc("key",institute_password,institute_password)
        boiledPass = passFuncobj.generateBoilpass()

        if not (checkInstitute(institute_tan)):
            instituteInsert(generated_uid,institute_name,institute_tan,institute_email,institute_phone,institute_password)
        else:
            mb.showerror("Warning", f"The TAN number '{institute_tan}' is already registered")
    

    root = Tk()
    root.geometry('520x540')
    root.title("Student Registration Form")
    root.configure(background='grey')


    l1 = Label(root, text="Institute Registration form",width=25,font=("times",20,"bold"),bg='blue',fg='white')
    l1.place(x=40,y=50)
    l2 = Label(root, text="Institute Name",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
    l2.place(x=40,y=130)

    e1 = Entry(root,width=30,bd=2)
    e1.place(x=240,y=130)

    l3 = Label(root, text="Institute Email",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
    l3.place(x=40,y=180)

    e2 = Entry(root,width=30,bd=2)
    e2.place(x=240,y=180)

    l6 = Label(root, text="Institute phone no.",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
    l6.place(x=40,y=230)

    e3 = Entry(root,width=30,bd=2)
    e3.place(x=240,y=230)

    var = IntVar()

    l7 = Label(root, text="Institute TAN no.",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
    l7.place(x=40,y=280)

    e4 = Entry(root,width=30,bd=2)
    e4.place(x=240,y=280)

    l8 = Label(root, text="Password",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
    l8.place(x=40,y=320)

    e5 = Entry(root,width=30,bd=2)
    e5.place(x=240,y=320)

    b1 = Button(root, text='Submit',command=saveinfo,width=15,bg='green',fg='white',font=("times",12,"bold"))
    b1.place(x=40,y=480)
    b2 = Button(root, text='Cancel',command=root.destroy,width=15,bg='maroon',fg='white',font=("times",12,"bold"))
    b2.place(x=320,y=480)

    root.mainloop()