# import tkinter as tk
# from tkinter import ttk
# from dbConnection import *

# class DocumentApp:
#     def __init__(self, root, uid):
#         self.root = root
#         self.root.title("Document Viewer")

#         self.uid = uid
#         self.create_gui()

#     def create_gui(self):
#         self.tree = ttk.Treeview(self.root)
#         self.tree["columns"] = ("File Name", "Category", "File Size")

#         self.tree.column("#0", width=0, stretch=tk.NO)  # To hide the default column
#         self.tree.column("File Name", anchor=tk.W, width=200)
#         self.tree.column("Category", anchor=tk.W, width=150)
#         self.tree.column("File Size", anchor=tk.W, width=100)

#         self.tree.heading("#0", text="", anchor=tk.W)
#         self.tree.heading("File Name", text="File Name", anchor=tk.W)
#         self.tree.heading("Category", text="Category", anchor=tk.W)
#         self.tree.heading("File Size", text="File Size", anchor=tk.W)

#         self.tree.pack(expand=tk.YES, fill=tk.BOTH)

        


    

#     def fetch_documents(self):
#         # Clear existing items in the treeview
#         for item in self.tree.get_children():
#             self.tree.delete(item)

#         try:
#             # Fetch documents from the database for the specified user
#             dbobj = db()
#             mydb, cursor = dbobj.dbconnect("documents")

#             query = "SELECT file_name, category, file_size FROM files WHERE uid = %s ORDER BY category"
#             cursor.execute(query, (self.uid,))
#             documents = cursor.fetchall()

#             # Populate the treeview with fetched documents
#             for document in documents:
#                 # Extracting values from the tuple
#                 file_name, category, file_size = document

#                 # Inserting values into the treeview
#                 self.tree.insert("", "end", values=(file_name, category, file_size))
#         finally:
#             # Always close the database connection and cursor
#             if mydb:
#                 mydb.close()
#             if cursor:
#                 cursor.close()


#     def run(self):
#         self.root.mainloop()

# if __name__ == "__main__":
#     # Replace 'your_uid' with the actual user ID
#     user_id = 'your_uid'
    
#     # Create and run the application
#     root = tk.Tk()
#     app = DocumentApp(root, user_id)
#     app.run()

# import tkinter as tk
# from tkinter import ttk
# from dbConnection import *
# from file_operations_interface import retrieve_file

# class DocumentApp:
#     def __init__(self, root, uid):
#         self.root = root
#         self.root.title("Document Viewer")

#         self.uid = uid
#         self.create_gui()

#     def create_gui(self):
#         self.tree = ttk.Treeview(self.root)
#         self.tree["columns"] = ("File Name", "Category", "File Size", "Action")

#         self.tree.column("#0", width=0, stretch=tk.NO)  # To hide the default column
#         self.tree.column("File Name", anchor=tk.W, width=200)
#         self.tree.column("Category", anchor=tk.W, width=150)
#         self.tree.column("File Size", anchor=tk.W, width=100)
#         self.tree.column("Action", anchor=tk.W, width=100)

#         self.tree.heading("#0", text="", anchor=tk.W)
#         self.tree.heading("File Name", text="File Name", anchor=tk.W)
#         self.tree.heading("Category", text="Category", anchor=tk.W)
#         self.tree.heading("File Size", text="File Size", anchor=tk.W)
#         self.tree.heading("Action", text="Action", anchor=tk.W)

#         self.tree.pack(expand=tk.YES, fill=tk.BOTH)

#         fetch_button = tk.Button(self.root, text="Fetch Documents", command=self.fetch_documents)
#         fetch_button.pack(pady=10)

#     def fetch_documents(self):
#         # Clear existing items in the treeview
#         for item in self.tree.get_children():
#             self.tree.delete(item)

#         try:
#             # Fetch documents from the database for the specified user
#             dbobj = db()
#             mydb, cursor = dbobj.dbconnect("documents")

#             query = "SELECT file_id, file_name, category, file_size FROM files WHERE uid = %s ORDER BY category"
#             cursor.execute(query, (self.uid,))
#             documents = cursor.fetchall()

#             # Populate the treeview with fetched documents
#             for document in documents:
#                 file_id, file_name, category, file_size = document

#                 # Inserting values into the treeview
#                 self.tree.insert("", "end", values=(file_name, category, file_size, ""))

#                 # Create a button in the "Action" column for each document
#                 action_button = tk.Button(self.root, text="Open", command=lambda id=file_id: self.open_document(id))
#                 self.tree.set(f"{file_id}", "Action", "")
#                 self.tree.window_create(f"{file_id}", column=3, window=action_button)

#         finally:
#             # Always close the database connection and cursor
#             if mydb:
#                 mydb.close()
#             if cursor:
#                 cursor.close()

#     def open_document(self, file_id):
#         # Call the retrieve_file function with the selected file_id and uid
#         retrieve_file(file_id, self.uid)

#     def run(self):
#         self.root.mainloop()

# if __name__ == "__main__":
#     # Replace 'your_uid' with the actual user ID
#     user_id = 'your_uid'
    
#     # Create and run the application
#     root = tk.Tk()
#     app = DocumentApp(root, user_id)
#     app.run()

import tkinter as tk
from tkinter import ttk
from dbConnection import *
from file_operations_interface import retrieve_file

class DocumentApp:
    def __init__(self, root, uid):
        self.root = root
        self.root.title("Document Viewer")

        self.uid = uid
        self.file_details = []  # Store file details in a list

        self.create_gui()

    def create_gui(self):
        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("File ID", "File Name", "File Type", "Category", "File Size", "Action")

        self.tree.column("#0", width=0, stretch=tk.NO)  # To hide the default column
        self.tree.column("File ID", anchor=tk.W, width=50)
        self.tree.column("File Name", anchor=tk.W, width=200)
        self.tree.column("File Type", anchor=tk.W, width=100)
        self.tree.column("Category", anchor=tk.W, width=150)
        self.tree.column("File Size", anchor=tk.W, width=100)
        self.tree.column("Action", anchor=tk.W, width=100)

        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("File ID", text="File ID", anchor=tk.W)
        self.tree.heading("File Name", text="File Name", anchor=tk.W)
        self.tree.heading("File Type", text="File Type", anchor=tk.W)
        self.tree.heading("Category", text="Category", anchor=tk.W)
        self.tree.heading("File Size", text="File Size", anchor=tk.W)
        self.tree.heading("Action", text="Action", anchor=tk.W)

        self.tree.pack(expand=tk.YES, fill=tk.BOTH)

        fetch_button = tk.Button(self.root, text="Fetch Documents", command=self.fetch_documents)
        fetch_button.pack(pady=10)

    def fetch_documents(self):
        # Clear existing items in the treeview and reset the file_details list
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.file_details = []

        try:
            # Fetch documents from the database for the specified user
            dbobj = db()
            mydb, cursor = dbobj.dbconnect("documents")

            query = "SELECT file_id, file_name, file_type, category, file_size FROM files WHERE uid = %s ORDER BY category"
            cursor.execute(query, (self.uid,))
            documents = cursor.fetchall()

            # Populate the treeview with fetched documents
            for document in documents:
                file_id, file_name, file_type, category, file_size = document

                # Append file details to the list
                self.file_details.append((file_id, file_name, file_type, category, file_size))

                # Inserting values into the treeview
                self.tree.insert("", "end", values=(file_id, file_name, file_type, category, file_size, ""))
                # print(self.file_details)

        finally:
            # Always close the database connection and cursor
            if mydb:
                mydb.close()
            if cursor:
                cursor.close()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    # Replace 'your_uid' with the actual user ID
    user_id = 'your_uid'
    
    # Create and run the application
    root = tk.Tk()
    app = DocumentApp(root, user_id)
    app.run()
