import pyAesCrypt
password = "please-use-a-long-and-random-password"
# encrypt
pyAesCrypt.encryptFile("aes.py", "aes.py.aes", password)
# decrypt
pyAesCrypt.decryptFile("aes.py.aes", "dataout.txt", password)



import tkinter as tk
from tkinter import filedialog
from functools import partial
from file_store_retrieve import store_file_in_database, retrieve_file_from_database
import pyAesCrypt

password = "please-use-a-long-and-random-password"

def upload_file():
    filename = filedialog.askopenfilename()
    if filename:
        try:
            # Encrypt the file
            encrypted_filename = filename + ".aes"
            pyAesCrypt.encryptFile(filename, encrypted_filename, password)
            # Store the encrypted file
            store_encrypted(encrypted_filename)
            status_label.config(text="File uploaded and encrypted successfully.")
        except Exception as e:
            status_label.config(text=f"Error encrypting and uploading file: {e}")


def retrieve_file():
    file_id = file_id_entry.get()
    if file_id:
        try:
            file_id = int(file_id)
            # Retrieve the encrypted file
            encrypted_filename = self.retrieve_encrypted(file_id)
            if encrypted_filename:
                # Decrypt the file
                decrypted_filename = "decrypted_" + encrypted_filename[:-4]  # Remove ".aes" extension
                pyAesCrypt.decryptFile(encrypted_filename, decrypted_filename, password)
                status_label.config(text=f"File retrieved and decrypted: {decrypted_filename}")
            else:
                status_label.config(text="File not found in the database.")
        except ValueError:
            status_label.config(text="Invalid file ID.")
    else:
        status_label.config(text="Please enter a file ID.")


# Create the main window
root = tk.Tk()
root.title("Encrypted File Storage App")

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
