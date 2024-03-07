import tkinter as tk
from tkinter import filedialog
from functools import partial
from file_operations_interface import retrieve_file

uid = "S692005561648"

def dummy():
    pass

def view_file():
    file_id = file_id_entry.get()
    if file_id:
        retrieve_file(uid, file_id)

# Create the main window
root = tk.Tk()
root.title("File Storage App")

# Create and place widgets
upload_button = tk.Button(root, text="Upload File", command=dummy)
upload_button.pack(pady=10)

retrieve_frame = tk.Frame(root)
retrieve_frame.pack(pady=10)

file_id_label = tk.Label(retrieve_frame, text="File ID:")
file_id_label.grid(row=0, column=0)

file_id_entry = tk.Entry(retrieve_frame)
file_id_entry.grid(row=0, column=1)

retrieve_button = tk.Button(retrieve_frame, text="View File", command=view_file)
retrieve_button.grid(row=0, column=2, padx=10)

status_label = tk.Label(root, text="")
status_label.pack(pady=10)

# Run the application
root.mainloop()
