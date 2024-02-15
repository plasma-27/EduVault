from tkinter import *
from dbConnection import *
from lastlogin import get_last_login
from datetime import datetime


def display_hello(uid):
    
    if (uid[0]=="S"):
        query_name = "SELECT name from student WHERE uid=%s"
    if (uid[0]=="I"):
        query_name = "SELECT name from institute WHERE uid=%s"
    if (uid[0]=="A"):
        query_name = "SELECT name from admin WHERE uid=%s"    
    dbobj = db()
    mydb,cursor = dbobj.dbconnect("credentials")
    # query_name = "SELECT name from student WHERE uid=%s"
    query_value = uid
    cursor.execute(query_name, (query_value,))
    result = cursor.fetchone()
    username = result[0]
    
    
    #Fetch last Login date and time
    
    lastLogin = get_last_login(uid)
    
    # Create the main window
    window = Tk()
    window.title("Greetings")
    window.geometry("400x200")
    window.configure(bg="#FFFFFF")

    # Create a label for the greeting
    greeting_label = Label(window, text="Hello, {}!".format(username), font=("Helvetica", 24), fg="#206DB4", bg="#FFFFFF")
    greeting_label.pack(pady=20)
    
    last_login_label = Label(window, text="Last Login: {}".format(lastLogin), font=("Helvetica", 24), fg="#206DB4", bg="#FFFFFF")
    last_login_label.pack(pady=20)

    # Run the Tkinter event loop
    window.mainloop()

# Call the function to display the greeting

