from tkinter import *
from dbConnection import *


def display_hello(uid):
    
    dbobj = db()
    mydb,cursor = dbobj.dbconnect("credentials")
    query_name = "SELECT name from student WHERE uid=%s"
    query_value = uid
    cursor.execute(query_name, (query_value,))
    result = cursor.fetchone()
    username = result[0]
    
    # Create the main window
    window = Tk()
    window.title("Greetings")
    window.geometry("400x200")
    window.configure(bg="#FFFFFF")

    # Create a label for the greeting
    greeting_label = Label(window, text="Hello, {}!".format(username), font=("Helvetica", 24), fg="#206DB4", bg="#FFFFFF")
    greeting_label.pack(pady=20)

    # Run the Tkinter event loop
    window.mainloop()

# Call the function to display the greeting
