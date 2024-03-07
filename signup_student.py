from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
import datetime
from password import passFunc
from uidGenerator import uid
from dbConnection import *
from storage_quota import *



def checkStudent(aadhaar_number):
    dbobj = db()
    mydb,cursor = dbobj.dbconnect("credentials")
    sql_query = "SELECT * FROM student WHERE aadhaar_number = %s"
    cursor.execute(sql_query, (aadhaar_number,))
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False
        
        

def studentInsert(uid,full_name, email, dob_value, gender, contact_no, aadhaar_no, password):
    
    dbobj = db()
    mydb,cursor = dbobj.dbconnect("credentials")
    
     # Insert data into the login table
    login_query = "INSERT INTO login (uid,`key`, hash) VALUES (%s, %s, %s)"
    # For simplicity, assuming 'key' is the username and 'hash' is the password hash
    login_data = (uid, "key", password)  # Replace 'password_hash' with the actual hashed password
    cursor.execute(login_query, login_data)
    
    
    # Insert data into the student table
    student_query = "INSERT INTO student (uid, name, gender, dob, phone, email, aadhaar_number) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    student_data = (uid, full_name, gender, dob_value, contact_no, email, aadhaar_no)
    cursor.execute(student_query, student_data)
    
   
    
     # Commit changes and close the connection
    mydb.commit()
    mydb.close()
    
    userID = uid
    successMessage =f"Registration Successful. Your User ID is {userID}"
    messagebox.showinfo("Success",successMessage)
    
    
    


def studentSignup():
    
    def saveinfo():
        # Get all the user inputs
        full_name = e1.get()
        email = e2.get()
        dob_value = dob.get()
        gender = "Male" if var.get() == 1 else "Female"
        contact_number = e3.get()
        aadhaar_number = e4.get()
        password = e5.get()
        uidobj = uid(aadhaar_number,1)
        generated_uid = uidobj.generate_unique_12_digit_number()
        passFuncobj = passFunc("key",password,password)
        boiledPass = passFuncobj.generateBoilpass()
        if not (checkStudent(aadhaar_number)):
            studentInsert(generated_uid,full_name, email, dob_value, gender, contact_number, aadhaar_number, boiledPass)
            storageobj = StorageQuota(generated_uid)
            storageobj.initialise_storage_quota()
        else:
            messagebox.showerror("User Already Exists", f"The Aadhaar number '{aadhaar_number}' is already registered")
    

    
    root = Tk()
    root.geometry('520x540')
    root.title("Student Registration Form")
    root.configure(background='grey')


    l1 = Label(root, text="Student Registration form",width=25,font=("times",20,"bold"),bg='blue',fg='white')
    l1.place(x=40,y=50)
    l2 = Label(root, text="Full Name",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
    l2.place(x=40,y=130)

    e1 = Entry(root,width=30,bd=2)
    e1.place(x=240,y=130)

    l3 = Label(root, text="Email",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
    l3.place(x=40,y=180)

    e2 = Entry(root,width=30,bd=2)
    e2.place(x=240,y=180)

    l4 = Label(root, text="DOB",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
    l4.place(x=40,y=230)

    dob = DateEntry(root, width=27, background='brown', foreground='white',date_pattern='dd/mm/Y', borderwidth=3)
    dob.place(x=240,y=230)

    l5 = Label(root, text="Gender", width=20, font=("times",12,"bold"),anchor="w",bg='grey')
    l5.place(x=40,y=280)

    var = IntVar()
    r1 = Radiobutton(root, text="Male", variable=var, value=1, font=("times",12),bg='grey')
    r1.place(x=235,y=280)
    r2 = Radiobutton(root, text="Female", variable=var, value=2, font=("times",12),bg='grey')
    r2.place(x=315,y=280)

    l6 = Label(root, text="Contact no.",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
    l6.place(x=40,y=320)

    e3 = Entry(root,width=30,bd=2)
    e3.place(x=240,y=320)

    l7 = Label(root, text="Aadhaar no.",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
    l7.place(x=40,y=370)

    e4 = Entry(root,width=30,bd=2)
    e4.place(x=240,y=370)

    l8 = Label(root, text="Password",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
    l8.place(x=40,y=420)

    e5 = Entry(root,width=30,bd=2,show="*")
    e5.place(x=240,y=420)


    b1 = Button(root, text='Submit',command=saveinfo,width=15,bg='green',fg='white',font=("times",12,"bold"))
    b1.place(x=40,y=480)
    b2 = Button(root, text='Cancel',command=root.destroy,width=15,bg='maroon',fg='white',font=("times",12,"bold"))
    b2.place(x=320,y=480)

    root.mainloop()    
    
    

