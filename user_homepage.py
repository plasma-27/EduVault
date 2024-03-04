import tkinter as tk
from tkinter import messagebox,simpledialog
from file_operations_interface import retrieve_file
from file_store_retrieve_db import *
from doc_upload_selector import *

class userHomePage:
    def __init__(self,user_info):
        self.uid = user_info.uid
        self.root = tk.Tk()
        self.root.title("Welcome to EduVault")
        self.root.geometry("400x300")

        # Create buttons
        update_profile_btn = tk.Button(self.root, text="Update Profile", command=self.dummy_function)
        upload_documents_btn = tk.Button(self.root, text="Upload Documents", command=self.upload_documents)
        view_documents_btn = tk.Button(self.root, text="View Documents", command=self.view_documents)
        change_password_btn = tk.Button(self.root, text="Change Password", command=self.dummy_function)

        # Pack buttons
        update_profile_btn.pack(pady=10)
        upload_documents_btn.pack(pady=10)
        view_documents_btn.pack(pady=10)
        change_password_btn.pack(pady=10)

        # Bind the close event to the on_close method
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def dummy_function(self):
        print("Button clicked!")
        
    def upload_documents(self):
        UploadDocumentsWindowobj = UploadDocumentsWindow(self.uid)
        UploadDocumentsWindowobj.window.mainloop
        
        # upload_file(self.uid) 
        
     
    
    def view_documents(self):
        # Function to view documents
        file_id = simpledialog.askinteger("View Documents", "Enter File ID:")
        if file_id is not None:
            # You can perform actions based on the entered file_id
            print(f"Viewing document with File ID: {file_id}")
            retrieve_file(self.uid,file_id) 
        else:
            messagebox.showinfo("Info", "Please enter a valid File ID.")
    
           

    def on_close(self):
        # Ask for confirmation before closing
        confirmation = messagebox.askyesno("Confirmation", "Do you want to log out?", icon='question')

        if confirmation:
            # Additional cleanup or closing operations if needed
            self.root.destroy()

    def run(self):
        self.root.mainloop()


