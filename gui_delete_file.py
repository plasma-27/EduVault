import tkinter as tk
from file_operations_interface import *

def delete():
    uid = "S692005561648"
    file_id = file_id_entry.get()
    # Perform deletion logic here using the file_id
    print(f"Deleting file with ID: {file_id}")
    delete_file(uid,file_id)

# Create the main window
window = tk.Tk()
window.title("File Deletion")
window.geometry("400x200")
# Create and place widgets
label = tk.Label(window, text="Enter File ID:")
label.pack(pady=10)

file_id_entry = tk.Entry(window)
file_id_entry.pack(pady=10)

delete_button = tk.Button(window, text="Delete", command=delete)
delete_button.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()
