
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

    # def retrieve_file_from_database(self,file_id):
    #     """Retrieve a file from the MySQL database."""
    #     try:
    #         dbobj = db()
    #         mydb, cursor = dbobj.dbconnect("documents")

    #         select_query = "SELECT file_name, file_data,`key` FROM files WHERE file_id = %s"
    #         cursor.execute(select_query, (file_id,))
    #         row = cursor.fetchone()
    #         mydb.close()
    #         if row:
    #             filename, file_data = row
    #             return filename, file_data
    #         else:
    #             print("File not found in database")
    #             return None, None
    #     except Error as e:
    #         print(f"Error retrieving file from database: {e}")
    #         return None, None
    
    def open_file_with_default_program(self, file_content, file_type):
        """Open the file with the default program based on its type."""
        try:
            with tempfile.NamedTemporaryFile(suffix='.' + file_type.split('/')[1], delete=False) as temp_file:
                temp_file.write(file_content)
                temp_file.flush()
                if os.name == 'posix':  # Check if the OS is Linux or macOS
                    subprocess.Popen(["xdg-open", temp_file.name])  # For Linux
                elif os.name == 'nt':  # Check if the OS is Windows
                    subprocess.Popen(["start", temp_file.name], shell=True)  # For Windows
        except Exception as e:
            print(f"Error opening file: {e}")

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

    

    # def retrieve(self, file_id):
    #     dbobj = db()
    #     mydb, cursor = dbobj.dbconnect("documents")
    #     select_query = "SELECT file_name, file_data, `key` FROM files WHERE file_id = %s"
    #     cursor.execute(select_query, (file_id,))
    #     row = cursor.fetchone()
    #     mydb.close()

    #     if row:
    #         filename, file_data, key = row
    #         try:
    #             # Specify the directory to store the encrypted and decrypted files
    #             upload_buffer_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploadBuffer")
                
    #             # Write the encrypted file to the specified directory
    #             encrypted_filename = os.path.join(upload_buffer_dir, filename)
    #             with open(encrypted_filename, "wb") as encrypted_file:
    #                 encrypted_file.write(file_data)
                
    #             # Decrypt the encrypted file
    #             decrypted_filename = os.path.join(upload_buffer_dir, "decrypted_" + filename[:-4])
    #             pyAesCrypt.decryptFile(encrypted_filename, decrypted_filename, key)
    #             print("File decrypted:", decrypted_filename)  # Print for debugging
                
    #             # Determine the file type
    #             file_type = self.determine_file_type(decrypted_filename)
                
    #             # Read the decrypted file data
    #             with open(decrypted_filename, "rb") as decrypted_file:
    #                 decrypted_file_data = decrypted_file.read()
                
    #             # Open the decrypted file with the default application
    #             self.open_file_with_default_program(decrypted_file_data, file_type)
    #         except Exception as e:
    #             print(f"Error decrypting file: {e}")
    #     else:
    #         print("File not found in database")



    def retrieve(self, file_id):
        dbobj = db()
        mydb, cursor = dbobj.dbconnect("documents")
        select_query = "SELECT file_name, file_data, `key` FROM files WHERE file_id = %s"
        cursor.execute(select_query, (file_id,))
        row = cursor.fetchone()
        mydb.close()

        if row:
            filename, file_data, key = row
            try:
                # # Specify the directory to store the encrypted and decrypted files
                # upload_buffer_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploadBuffer")
                
                # # Write the encrypted file to the specified directory
                # encrypted_filename = os.path.join(upload_buffer_dir, filename)
                # with open(encrypted_filename, "wb") as encrypted_file:
                #     encrypted_file.write(file_data)
                
                # # Decrypt the encrypted file
                # decrypted_filename = os.path.join(upload_buffer_dir, "decrypted_" + filename[:-4])
                # pyAesCrypt.decryptFile(encrypted_filename, decrypted_filename, key)
                # print("File decrypted:", decrypted_filename)  # Print for debugging
                
                # Determine the file type
                # file_type = self.determine_file_type(decrypted_filename)
                
                decrypted_filename, file_type = fileCrypt.decrypt(filename,file_data,key)
                # Read the decrypted file data
                with open(decrypted_filename, "rb") as decrypted_file:
                    decrypted_file_data = decrypted_file.read()
                
                # Open the decrypted file with the default application
                self.open_file_with_default_program(decrypted_file_data, file_type)
            except Exception as e:
                print(f"Error decrypting file: {e}")
        else:
            print("File not found in database")




