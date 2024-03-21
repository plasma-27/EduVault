from tkinter import *
from signup_student import studentSignup
from signup_institute import instituteSignup
from tkinter import messagebox
from dbConnection import *
from password import *
from postLogin import *
from login_activity import *
from otp import *
from tkinter import simpledialog
from current_user_info import *
from user_homepage import *



  
# def show_otp_dialog(userid, window):
#     if (userid[0]=="S"):
#         user_type = "S"
#     else:
#         user_type = "I"    
#     generated_otp = generate_otp()
#     user_info = currentUserInfo(userid,user_type)
#     # otp_send(generated_otp,user_info)
#     while True:  # Keep asking for OTP until correct or user cancels
#         otp = simpledialog.askstring("OTP Verification", f"Please enter the OTP {generated_otp} sent to your registered E-mail Id:")

#         # if otp is None:
            
#         #     window.destroy()  # Close the main window
#         #     return

#         if verify_otp(otp, generated_otp):
#             update_last_login(userid)
#             window.destroy()  # Close the login window
#             # display_hello(userid)
#             userMainWindow = userHomePage(user_info)
#             userMainWindow.run()
#             return
#         else: 
#             messagebox.showerror("Incorrect OTP", "The entered OTP is incorrect. Please try again.")

def show_otp_dialog(userid, window):
    if userid[0] == "S":
        user_type = "S"
    else:
        user_type = "I"

    generated_otp = generate_otp()
    user_info = currentUserInfo(userid, user_type)
    otp_send(generated_otp,user_info)
    attempts = 0

    while attempts < 3:  # Limit the maximum number of attempts to 3
        otp = simpledialog.askstring("OTP Verification", f"Please enter the OTP {generated_otp} sent to your registered E-mail Id:")

        if otp is None:
            window.destroy()  # Close the main window
            return

        if verify_otp(otp, generated_otp):
            update_last_login(userid)
            window.destroy()  # Close the login window
            userMainWindow = userHomePage(user_info)
            userMainWindow.run()
            return
        else:
            attempts += 1
            remaining_attempts = 3 - attempts
            messagebox.showerror("Incorrect OTP", f"The entered OTP is incorrect. You have {remaining_attempts} attempt(s) remaining. Please try again.")

    # If the maximum number of attempts is reached
    messagebox.showerror("Max Attempts Reached", "You have reached the maximum number of OTP attempts. Please try again later.")
    window.destroy()  # Close the main window
   
        
def submit():
    userid = Login_emailName_entry.get()
    password = Login_passwordName_entry.get()
    
    
    if not userid or not password:
        messagebox.showerror("Error", "Please enter both userid and password.")
        
        return
    
    dbobj = db()
    mydb,cursor = dbobj.dbconnect("credentials")
    
    query_boiledPass = "SELECT hash from login WHERE uid=%s"
    query_uid=userid
    cursor.execute(query_boiledPass, (query_uid,))
    resultTuple = cursor.fetchone()
    if resultTuple is None:
        # User does not exist
        messagebox.showerror("Error", "User does not exist.")
        return
    else:
        raw_boiledhash = resultTuple[0]
        
        passFuncobj = passFunc("key",password,password)
        isPasswordVerified = passFuncobj.passVerify(password,raw_boiledhash)
    if isPasswordVerified:
        show_otp_dialog(userid,window)
  
    else:
        messagebox.showerror("Access Denied","Invalid userid or Password")
    
   
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
    text="UserID",
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





