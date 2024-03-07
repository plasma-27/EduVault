import tkinter as tk
from file_operations_interface import *



def grant_file_interface():
    file_id = file_id_entry.get()
    suid_value = suid_entry.get()
    iuid_value = iuid_entry.get()
    validity_days = validity_entry.get()

    # Perform access granting logic here using the provided values
    print(f"Granting access to file {file_id} for suid: {suid_value}, iuid: {iuid_value}, validity: {validity_days} days")
    grant_file_access(file_id,suid_value,iuid_value,validity_days)

# Create the main window
window = tk.Tk()
window.title("File Sharing")
window.geometry("400x500")

# Create and place widgets
file_id_label = tk.Label(window, text="Enter File ID:")
file_id_label.pack(pady=10)

file_id_entry = tk.Entry(window)
file_id_entry.pack(pady=10)

suid_label = tk.Label(window, text="SUID:")
suid_label.pack(pady=10)

suid_entry = tk.Entry(window)
suid_entry.pack(pady=10)

iuid_label = tk.Label(window, text="IUID:")
iuid_label.pack(pady=10)

iuid_entry = tk.Entry(window)
iuid_entry.pack(pady=10)

validity_label = tk.Label(window, text="Validity (days):")
validity_label.pack(pady=10)

validity_entry = tk.Entry(window)
validity_entry.pack(pady=10)

share_button = tk.Button(window, text="Share", command=grant_file_interface)
share_button.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()
