import tkinter as tk
from tkinter import filedialog
from functools import partial
# from file_store_retrieve import store, retrieve
from document_store import *


def upload_file(uid):
    
    documentobj = Document(uid)
    filename = filedialog.askopenfilename()
    print(filename)
    if filename:
        documentobj.store(filename)
        print("File uploaded successfully.")
        # status_label.config(text="File uploaded successfully.")


def retrieve_file(uid,file_id):
    documentobj = Document(uid)
    file_id = file_id
    if file_id:
        try:
            file_id = int(file_id)
            documentobj.retrieve(file_id)
        except ValueError:
            print("Invalid file ID.")
            # status_label.config(text="Invalid file ID.")
    else:
        print("Please enter a file ID.")
        # status_label.config(text="Please enter a file ID.")

# Main application logic
if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("File Storage App")

    # Create and place widgets
    upload_button = tk.Button(root, text="Upload File", command=partial(upload_file, "sample_uid"))
    upload_button.pack(pady=10)

    retrieve_frame = tk.Frame(root)
    retrieve_frame.pack(pady=10)

    file_id_label = tk.Label(retrieve_frame, text="File ID:")
    file_id_label.grid(row=0, column=0)

    file_id_entry = tk.Entry(retrieve_frame)
    file_id_entry.grid(row=0, column=1)

    retrieve_button = tk.Button(retrieve_frame, text="Retrieve File", command=partial(retrieve_file, "sample_uid"))
    retrieve_button.grid(row=0, column=2, padx=10)

    status_label = tk.Label(root, text="")
    status_label.pack(pady=10)

    # Run the application
    root.mainloop()