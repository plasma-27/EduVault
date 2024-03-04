import tkinter as tk
from tkinter import filedialog
from functools import partial
# from file_store_retrieve import store, retrieve
from file_store_retrieve_db import *
import os


def upload_file_selector(uid,file_name_to_store,file_category):
    
    file_name_to_store = file_name_to_store
    file_category = file_category
    documentobj = Document(uid)
    rawFilename = filedialog.askopenfilename()
    print(rawFilename)
    if rawFilename:
        file_size_in_bytes = get_file_size(rawFilename)
        documentobj.store(rawFilename,file_name_to_store,file_category,file_size_in_bytes)
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
        
        
def get_file_size(filename):
    try:
        # Get the size of the file in bytes
        file_size = os.path.getsize(filename)
        return file_size
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None
    except Exception as e:
        print(f"Error getting file size: {e}")
        return None
        

# # Main application logic
# if __name__ == "__main__":
#     # Create the main window
#     root = tk.Tk()
#     root.title("File Storage App")

#     # Create and place widgets
#     upload_button = tk.Button(root, text="Upload File", command=partial(upload_file, "sample_uid"))
#     upload_button.pack(pady=10)

#     retrieve_frame = tk.Frame(root)
#     retrieve_frame.pack(pady=10)

#     file_id_label = tk.Label(retrieve_frame, text="File ID:")
#     file_id_label.grid(row=0, column=0)

#     file_id_entry = tk.Entry(retrieve_frame)
#     file_id_entry.grid(row=0, column=1)

#     retrieve_button = tk.Button(retrieve_frame, text="Retrieve File", command=partial(retrieve_file, "sample_uid"))
#     retrieve_button.grid(row=0, column=2, padx=10)

#     status_label = tk.Label(root, text="")
#     status_label.pack(pady=10)

#     # Run the application
#     root.mainloop()