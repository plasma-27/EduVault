from tkinter import *
from signup_student import studentSignup
from signup_institute import instituteSignup
from tkinter import messagebox
from dbConnection import *
from password import *
from postLogin import *
from lastlogin import *



def submit():
    username = Login_emailName_entry.get()
    password = Login_passwordName_entry.get()
    
    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password.")
        return
    
    dbobj = db()
    mydb,cursor = dbobj.dbconnect("credentials")
    
    query_boiledPass = "SELECT hash from login WHERE uid=%s"
    query_uid=username
    cursor.execute(query_boiledPass, (query_uid,))
    resultTuple = cursor.fetchone()
    raw_boiledhash = resultTuple[0]
   
    
    passFuncobj = passFunc("key",password,password)
    access_grant = passFuncobj.passVerify(password,raw_boiledhash)
    if access_grant:
        update_last_login(username)
        window.destroy()  # Close the login window
        display_hello(username)
    else:
        messagebox.showerror("Access Denied","Invalid Username or Password")
            
    # print(access_grant)
    # messagebox.showinfo("Success",access_grant)

window = Tk()
window.title("EduVault : Academic Records Management")  # Set the title of the window

height = 650
width = 1240
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 4) - (height // 4)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window.configure(bg="black")

# ================ Background Image ====================
Login_backgroundImage = PhotoImage(file="images/image_1.png")
bg_imageLogin = Label(
    window,
    image=Login_backgroundImage,
    bg="black"
)
bg_imageLogin.place(x=120, y=28)

# ================ Header Text Left ====================
Login_headerText_image_left = PhotoImage(file="images/headerText_image.png")
Login_headerText_image_label1 = Label(
    bg_imageLogin,
    image=Login_headerText_image_left,
    bg="black"
)
Login_headerText_image_label1.place(x=60, y=45)

Login_headerText1 = Label(
    bg_imageLogin,
    text="EduVault",
    fg="#FFFFFF",
    font=("yu gothic ui bold", 20 * -1),
    bg="black"
)
Login_headerText1.place(x=110, y=45)

# ================ LOGIN TO ACCOUNT HEADER ====================
loginAccount_header = Label(
    bg_imageLogin,
    text="Login to continue",
    fg="#FFFFFF",
    font=("yu gothic ui Bold", 28 * -1),
    bg="black"
)
loginAccount_header.place(x=75, y=121)

# ================ NOT A MEMBER TEXT ====================
loginText = Label(
    bg_imageLogin,
    text="Not a Member?",
    fg="#FFFFFF",
    font=("yu gothic ui Regular", 15 * -1),
    bg="black"
)
loginText.place(x=75, y=187)

# ================ GO TO SIGN UP ====================
switchSignup = Button(
    bg_imageLogin,
    text="Student Register",
    fg="#206DB4",
    font=("yu gothic ui Bold", 15 * -1),
    bg="black",
    bd=0,   
    cursor="hand2",
    activebackground="#272A37",
    activeforeground="#ffffff",
    command=studentSignup
)
switchSignup.place(x=220, y=185, width=150, height=35)




switchInstituteSignup = Button(
    bg_imageLogin,
    text="Institute Register",
    fg="#206DB4",
    font=("yu gothic ui Bold", 15 * -1),
    bg="black",
    bd=0,
    cursor="hand2",
    activebackground="#272A37",
    activeforeground="#ffffff",
    command=instituteSignup  
)
switchInstituteSignup.place(x=switchSignup.winfo_x() + switchSignup.winfo_reqwidth() + 250, y=185, width=150, height=35)

# ================ Email Name Section ====================
Login_emailName_image = PhotoImage(file="images/email.png")
Login_emailName_image_Label = Label(
    bg_imageLogin,
    image=Login_emailName_image,
    bg="black"
)
Login_emailName_image_Label.place(x=76, y=242)

Login_emailName_text = Label(
    Login_emailName_image_Label,
    text="Username",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
Login_emailName_text.place(x=25, y=0)

Login_emailName_icon = PhotoImage(file="images/email-icon.png")
Login_emailName_icon_Label = Label(
    Login_emailName_image_Label,
    image=Login_emailName_icon,
    bg="#3D404B"
)
Login_emailName_icon_Label.place(x=370, y=15)

Login_emailName_entry = Entry(
    Login_emailName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
)
Login_emailName_entry.place(x=8, y=17, width=354, height=27)

# ================ Password Name Section ====================
Login_passwordName_image = PhotoImage(file="images/email.png")
Login_passwordName_image_Label = Label(
    bg_imageLogin,
    image=Login_passwordName_image,
    bg="black"
)
Login_passwordName_image_Label.place(x=80, y=330)

Login_passwordName_text = Label(
    Login_passwordName_image_Label,
    text="Password",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
Login_passwordName_text.place(x=25, y=0)

Login_passwordName_icon = PhotoImage(file="images/pass-icon.png")
Login_passwordName_icon_Label = Label(
    Login_passwordName_image_Label,
    image=Login_passwordName_icon,
    bg="#3D404B"
)
Login_passwordName_icon_Label.place(x=370, y=15)

Login_passwordName_entry = Entry(
    Login_passwordName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
)
Login_passwordName_entry.place(x=8, y=17, width=354, height=27)

# =============== Submit Button ====================
Login_button_image_1 = PhotoImage(file="images/button_1.png")
Login_button_1 = Button(
    bg_imageLogin,
    image=Login_button_image_1,
    borderwidth=0,
    highlightthickness=0,
    
    relief="flat",
    activebackground="#272A37",
    cursor="hand2",
    command=submit
)
Login_button_1.place(x=120, y=445, width=333, height=65)

window.resizable(False, False)
window.mainloop()






# def display_hello():
#     # Create the main window
#     window = Tk()
#     window.title("Greetings")
#     window.geometry("400x200")
#     window.configure(bg="#FFFFFF")

#     # Create a label for the greeting
#     greeting_label = Label(window, text="Hello!", font=("Helvetica", 24), fg="#206DB4", bg="#FFFFFF")
#     greeting_label.pack(pady=20)

#     # Run the Tkinter event loop
#     window.mainloop()

# # Call the function to display the greeting
# display_hello()
