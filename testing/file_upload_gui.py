import tkinter as tk
from tkinter import filedialog
from functools import partial
# from file_store_retrieve import store, retrieve
from file_store_retrieve_db import *


def upload_file():
    uid="S477729132063"
    documentobj = Document(uid)
    filename = filedialog.askopenfilename()
    print(filename)
    if filename:
        documentobj.store(filename)
        status_label.config(text="File uploaded successfully.")


def retrieve_file():
    uid="S477729132063"
    documentobj = Document(uid)
    file_id = file_id_entry.get()
    if file_id:
        try:
            file_id = int(file_id)
            documentobj.retrieve(file_id)
        except ValueError:
            status_label.config(text="Invalid file ID.")
    else:
        status_label.config(text="Please enter a file ID.")


# Create the main window
root = tk.Tk()
root.title("File Storage App")

# Create and place widgets
upload_button = tk.Button(root, text="Upload File", command=upload_file)
upload_button.pack(pady=10)

retrieve_frame = tk.Frame(root)
retrieve_frame.pack(pady=10)

file_id_label = tk.Label(retrieve_frame, text="File ID:")
file_id_label.grid(row=0, column=0)

file_id_entry = tk.Entry(retrieve_frame)
file_id_entry.grid(row=0, column=1)

retrieve_button = tk.Button(retrieve_frame, text="Retrieve File", command=retrieve_file)
retrieve_button.grid(row=0, column=2, padx=10)

status_label = tk.Label(root, text="")
status_label.pack(pady=10)

# Run the application
root.mainloop()
