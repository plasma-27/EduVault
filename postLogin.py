from tkinter import *

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Check username and password (dummy validation)
    if username == "admin" and password == "admin":
        # Close the login window
        root.destroy()
        # Open the dummy page
        dummy_page(username)
    else:
        # Show error message for invalid credentials
        error_label.config(text="Invalid username or password")

def dummy_page(username):
    # Create a new window for the dummy page
    dummy_window = Toplevel()
    dummy_window.title("Dummy Page")
    dummy_window.geometry("400x300")
    dummy_window.configure(background='grey')  # Set background color to grey

    # Display the "successfully logged in" message
    logged_in_label = Label(dummy_window, text="Successfully Logged In!", font=("Arial", 16), bg='grey', fg='white')
    logged_in_label.pack(pady=20)

    # Display the "welcome" message with the username
    welcome_label = Label(dummy_window, text=f"Welcome {username}!", font=("Arial", 14), bg='grey', fg='white')
    welcome_label.pack(pady=10)

# Create the main login window
root = Tk()
root.title("Login Page")
root.geometry("400x200")
root.configure(background='grey')  # Set background color to grey

# Username label and entry
label_username = Label(root, text="Username:", bg='grey')
label_username.grid(row=0, column=0, padx=10, pady=10)
entry_username = Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

# Password label and entry
label_password = Label(root, text="Password:", bg='grey')
label_password.grid(row=1, column=0, padx=10, pady=10)
entry_password = Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

# Error label for displaying validation errors
error_label = Label(root, text="", fg="red", bg='grey')
error_label.grid(row=2, columnspan=2)

# Login button
login_button = Button(root, text="Login", command=login, bg='green', fg='white')
login_button.grid(row=3, columnspan=2, padx=10, pady=10)

# Run the main event loop
root.mainloop()
