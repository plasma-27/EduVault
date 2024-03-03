from signup_student import studentSignup
from signup_institute import instituteSignup
from tkinter import *
from tkinter import messagebox
from password import passFunc
from dbConnection import *

def toggle_password_visibility():
    # Toggle the password visibility between normal and hidden
    current_show_state = e_password.cget("show")
    if current_show_state:
        e_password.config(show="")
        show_password_button.config(text="Hide Password")
    else:
        e_password.config(show="*")
        show_password_button.config(text="Show Password")

def submit():
    username = e_username.get()
    password = e_password.get()
    
    dbobj = db()
    mydb,cursor = dbobj.dbconnect("credentials")
    
    query_boiledPass = "SELECT hash from login WHERE uid=%s"
    query_uid=username
    cursor.execute(query_boiledPass, (query_uid,))
    resultTuple = cursor.fetchone()
    raw_boiledhash = resultTuple[0]
    successMessage =f"result: {raw_boiledhash}"
    messagebox.showinfo("Success",successMessage)
   
    
    passFuncobj = passFunc("key",password,password)
    access_grant = passFuncobj.passVerify(password,raw_boiledhash)
    print(access_grant)
    



root = Tk()
root.geometry('520x540')
root.title("EduVault Login Page")
root.configure(background='grey')  # Set background color to grey

# EduVault label with bold text and blue background
eduvault_text = "EduVault"
eduvault_font = ("times", 30, "bold")
eduvault_bg = '#2979FF'
eduvault_fg = 'white'
eduvault_label_width = len(eduvault_text)
eduvault_x = (520 - (eduvault_label_width * 14)) / 2  # Calculate x-coordinate dynamically
l_eduvault = Label(root, text=eduvault_text, width=eduvault_label_width, font=eduvault_font,
                   bg=eduvault_bg, fg=eduvault_fg)
l_eduvault.place(x=eduvault_x, y=50)

# Username label and entry
l_username = Label(root, text="Username", width=20, font=("times", 12, "bold"), anchor="w", bg='grey', fg='black')
l_username.place(x=40, y=130)

e_username = Entry(root, width=30, bd=2)
e_username.place(x=240, y=130)

# Password label and entry
l_password = Label(root, text="Password", width=20, font=("times", 12, "bold"), anchor="w", bg='grey', fg='black')
l_password.place(x=40, y=180)

e_password = Entry(root, width=30, bd=2, show="*")
e_password.place(x=240, y=180)

# Show Password button
show_password_button = Button(root, text="Show Password", command=toggle_password_visibility, width=15,
                              bg='#4CAF50', fg='white', font=("times", 12, "bold"))
show_password_button.place(x=40, y=230)

# Submit button
b1 = Button(root, text='Submit', command=submit, width=15, bg='#4CAF50', fg='white', font=("times", 12, "bold"))
b1.place(x=40, y=280)

# Cancel button
b2 = Button(root, text='Cancel', command=root.destroy, width=15, bg='#f44336', fg='white', font=("times", 12, "bold"))
b2.place(x=320, y=280)

root.mainloop()







# studentSignup()
# instituteSignup()