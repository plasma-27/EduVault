
from mysql.connector import Error
import mimetypes
import subprocess
import tempfile
import io
from dbConnection import *
import os
from encrypt_decrypt import *
from storage_quota import *
from current_user_info import *


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

        
        
        
    
    def store_file_in_database(self,original_filename, file_type, file_name_to_store,file_category,file_size_in_bytes ,file_data,key):
        """Store a file in the MySQL database."""
        file_category = file_category
        file_size_in_bytes = file_size_in_bytes
        file_type = file_type
        try:
            
            
            
            dbobj = db()
            mydb, cursor = dbobj.dbconnect("documents")
            # insert_query = "INSERT INTO files (uid, file_name, file_type, file_data, `key`, file_size, category) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            # cursor.execute(insert_query, (self.uid, file_name_to_store, file_type, file_data, key, file_size_in_bytes, file_category))
            params = (self.uid, file_name_to_store, file_type, file_data, key, file_size_in_bytes, file_category)

            insert_query = "INSERT INTO files (uid, file_name, file_type, file_data, `key`, file_size, category) VALUES (%s, %s, %s, %s, %s, %s, %s)"

            cursor.execute(insert_query, params)


            # cursor.execute(insert_query, (filename, file_data,key))
            mydb.commit()
            mydb.close()

            print("File stored in database successfully")
            storageobj = StorageQuota(self.uid)
            storageobj.storage_quota_decrement(file_size_in_bytes)  # decrement storage quota after upload
        except Error as e:
            print(f"Error storing file in database: {e}")

    
    
    
    def open_file_with_default_program(self, file_content, file_type, file_name):
        """Open the file with the default program based on its type."""
        try:
            with open(file_name, 'wb') as file:
                file.write(file_content)

            if os.name == 'posix':  # Check if the OS is Linux or macOS
                subprocess.Popen(["xdg-open", file_name])  # For Linux
            elif os.name == 'nt':  # Check if the OS is Windows
                subprocess.Popen(["start", file_name], shell=True)  # For Windows

        except Exception as e:
            print(f"Error opening file: {e}")

    def determine_file_type(self,filename):
        """Determine the file type based on the filename."""
        file_type, _ = mimetypes.guess_type(filename)
        return file_type

 


    
    def store(self, rawFilename, file_name_to_store,file_category,file_size_in_bytes):
        file_name_to_store = file_name_to_store
        file_category = file_category
        file_size_in_bytes = file_size_in_bytes
        
        file_type = self.determine_file_type(rawFilename)
        key = self.retrieveKey()
        

        try:
            # Encrypt the file and get the encrypted filename
            encrypted_filename = fileCrypt.encrypt(rawFilename, key)

            # Read the encrypted file data
            with open(encrypted_filename, "rb") as encrypted_file:
                encrypted_file_data = encrypted_file.read()

            # Store the encrypted file data in the database
            self.store_file_in_database(rawFilename, file_type, file_name_to_store,file_category,file_size_in_bytes,encrypted_file_data, key)
        except FileNotFoundError:
            print(f"Error: File '{rawFilename}' not found.")
        except Exception as e:
            print(f"Error: {e}")

    


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
               
                decrypted_filename, file_type = fileCrypt.decrypt(filename,file_data,key)
                # Read the decrypted file data
                with open(decrypted_filename, "rb") as decrypted_file:
                    decrypted_file_data = decrypted_file.read()
                
                # Open the decrypted file with the default application
                self.open_file_with_default_program(decrypted_file_data, file_type,filename)
            except Exception as e:
                print(f"Error decrypting file: {e}")
        else:
            print("File not found in database")


    def delete(self, file_id):
        dbobj = db()
        mydb, cursor = dbobj.dbconnect("documents")
    
        try:
            # Check if the file exists
            check_query = "SELECT * FROM files WHERE file_id = %s"
            cursor.execute(check_query, (file_id,))
            existing_file = cursor.fetchone()
    
            if existing_file:
                # Get file size before deleting
                self.file_size = existing_file[6]
    
                
                # Delete entries from file_access for the specified file_id
                delete_access_query = "DELETE FROM file_access WHERE file_id = %s"
                cursor.execute(delete_access_query, (file_id,))
                mydb.commit()
                print(f"File access entries for ID {file_id} deleted successfully.")

                # Delete the file entry from the files table
                delete_query = "DELETE FROM files WHERE file_id = %s"
                cursor.execute(delete_query, (file_id,))
                mydb.commit()
                print(f"File with ID {file_id} deleted successfully.")
    

                # Decrement storage quota
                storageobj = StorageQuota(self.uid)
                storageobj.storage_quota_decrement(self.file_size)
            else:
                print(f"File with ID {file_id} not found.")
    
        finally:
            # Always close the database connection and cursor
            if mydb:
                mydb.close()
            if cursor:
                cursor.close()
    