import mysql.connector
from mysql.connector import Error
import mimetypes
import subprocess
import tempfile
import io
from dbConnection import *
import pyAesCrypt
import tkinter as tk
from tkinter import filedialog
import os
from encrypt_file import *
# password = "please-use-a-long-and-random-password"

class Document:
    
    def __init__(self,uid):
        self.uid=uid
        
    def retrieveKey(self):
        uid=self.uid
        dbobj = db()
        mydb,cursor = dbobj.dbconnect("credentials")
        select_query = "SELECT hash from login where uid = %s"
        uid_query = uid
        cursor.execute(select_query,(uid_query,))
        key = cursor.fetchone()
        mydb.close()
        cursor.close()
        if key:
            return key[0]  # Extracting the first element of the tuple (assuming 'hash' is the first column)
        else:
            return None  # Return None if no key is found for the given uid

        
        
        
    
    def store_file_in_database(self,filename, file_data,key):
        """Store a file in the MySQL database."""
        try:
            dbobj = db()
            mydb, cursor = dbobj.dbconnect("documents")
            insert_query = "INSERT INTO files (file_name, file_data,`key`) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (filename, file_data,key))
            mydb.commit()
            mydb.close()

            print("File stored in database successfully")
        except Error as e:
            print(f"Error storing file in database: {e}")

    def retrieve_file_from_database(self,file_id):
        """Retrieve a file from the MySQL database."""
        try:
            dbobj = db()
            mydb, cursor = dbobj.dbconnect("documents")

            select_query = "SELECT file_name, file_data,key FROM files WHERE file_id = %s"
            cursor.execute(select_query, (file_id,))
            row = cursor.fetchone()
            mydb.close()
            if row:
                filename, file_data = row
                return filename, file_data
            else:
                print("File not found in database")
                return None, None
        except Error as e:
            print(f"Error retrieving file from database: {e}")
            return None, None

    def determine_file_type(self,filename):
        """Determine the file type based on the filename."""
        file_type, _ = mimetypes.guess_type(filename)
        return file_type

    def open_file_with_default_program(self,file_data, file_type):
        """Open the file with the default program based on its type."""
        try:
            with tempfile.NamedTemporaryFile(suffix='.' + file_type.split('/')[1], delete=False) as temp_file:
                temp_file.write(file_data)
                temp_file.flush()
                subprocess.Popen(["xdg-open", temp_file.name])  # For Linux
                # subprocess.Popen(["open", temp_file.name])  # For macOS
                # subprocess.Popen(["start", temp_file.name], shell=True)  # For Windows
        except Exception as e:
            print(f"Error opening file: {e}")


    
    def store(self, filename):
        key = self.retrieveKey()

        try:
            # Encrypt the file and get the encrypted filename
            encrypted_filename = fileCrypt.encrypt(filename, key)

            # Read the encrypted file data
            with open(encrypted_filename, "rb") as encrypted_file:
                encrypted_file_data = encrypted_file.read()

            # Store the encrypted file data in the database
            self.store_file_in_database(os.path.basename(encrypted_filename), encrypted_file_data, key)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"Error: {e}")

    def retrieve(self,file_id):
        dbobj = db()
        mydb,cursor = dbobj.dbconnect("credentials")
        select_query = "select hash from login where uid = %s"
        cursor.execute(select_query,(self.uid,))
        password = cursor.fetchone()
        try:
            file_id = int(file_id)
            filename, file_data = self.retrieve_file_from_database(file_id)
            if file_data:
                decrypted_filename = "decrypted_" + filename[:-4]  # Remove ".aes" extension
                pyAesCrypt.decryptFile(filename, decrypted_filename, password)
                print("File decrypted:", decrypted_filename)  # Print for debugging
                self.open_file_with_default_program(file_data, self.determine_file_type(decrypted_filename))
        except ValueError:
            print("Invalid file ID.")
        except Exception as e:
            print(f"Error: {e}")

    # Define the rest of the functions (open_file_with_default_program, mainloop) as they are


# root = tk.Tk()
# root.title("File Storage App")

# # Create and place widgets
# upload_button = tk.Button(root, text="Upload File", command=upload_file)
# upload_button.pack(pady=10)

# retrieve_frame = tk.Frame(root)
# retrieve_frame.pack(pady=10)

# file_id_label = tk.Label(retrieve_frame, text="File ID:")
# file_id_label.grid(row=0, column=0)

# file_id_entry = tk.Entry(retrieve_frame)
# file_id_entry.grid(row=0, column=1)

# retrieve_button = tk.Button(retrieve_frame, text="Retrieve File", command=retrieve_file)
# retrieve_button.grid(row=0, column=2, padx=10)

# status_label = tk.Label(root, text="")
# status_label.pack(pady=10)

# # Run the application
# root.mainloop()
