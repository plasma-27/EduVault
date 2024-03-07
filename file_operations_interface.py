import tkinter as tk
from tkinter import filedialog
from file_store_retrieve_db import *
import os
from datetime import datetime, timedelta
from dbConnection import db



def upload_file_selector(uid, file_name_to_store, file_category):
    file_name_to_store = file_name_to_store
    file_category = file_category
    documentobj = Document(uid)

    raw_filename = filedialog.askopenfilename()
    print(raw_filename)

    if raw_filename:
        file_size_in_bytes = get_file_size(raw_filename)
        
        file_type = documentobj.determine_file_type(raw_filename)

        # Allow uploading only if the file type is 'image' or 'pdf'
        if file_type.startswith('image/') or file_type == 'application/pdf':
            # documentobj.store(raw_filename, file_name_to_store, file_category, file_size_in_bytes)
            if file_size_in_bytes < 1024 * 1024:  # Check if file size is below 1MB
                documentobj.store(raw_filename, file_name_to_store, file_category, file_size_in_bytes)
                print("File uploaded successfully.")
            else:
                print("Max size of document is 1 MB. File not uploaded.")
            
        else:
            print("Invalid file type. Only image or pdf files are allowed.")
        
        
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
 


def grant_file_access(file_id, suid, iuid, validity_days):
    
    dbobj = db()
    mydb, cursor = dbobj.dbconnect("documents")
    try:
        validity_days = int(validity_days)
        
        # Calculate the validity date by adding the specified number of days to the current date
        validity_date = (datetime.now() + timedelta(days=validity_days)).date()

        
        

        # Insert access record into the file_access table
        insert_query = "INSERT INTO file_access (file_id, suid, iuid, validity) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (file_id, suid, iuid, validity_date))

        # Commit the changes to the database
        mydb.commit()
        print("Access granted successfully.")
    except Exception as e:
        print(f"Error granting access: {e}")
    finally:
        # Close the database connection
        if mydb:
            mydb.close()

def revoke_file_access(file_id, suid, iuid):
    try:
        # Connect to the database
        dbobj = db()
        mydb, cursor = dbobj.dbconnect("documents")

        # Delete access record from the file_access table
        delete_query = "DELETE FROM file_access WHERE file_id = %s AND suid = %s AND iuid = %s"
        cursor.execute(delete_query, (file_id, suid, iuid))

        # Commit the changes to the database
        mydb.commit()
        print("Access revoked successfully.")
    except Exception as e:
        print(f"Error revoking access: {e}")
    finally:
        # Close the database connection
        if mydb:
            mydb.close()

def revoke_everything(suid, iuid):
    try:
        # Connect to the database
        dbobj = db()
        mydb, cursor = dbobj.dbconnect("documents")

        # Remove all entries in the file_access table for the specified suid and iuid
        delete_query = "DELETE FROM file_access WHERE suid = %s AND iuid = %s"
        cursor.execute(delete_query, (suid, iuid))

        # Commit the changes to the database
        mydb.commit()
        print("File access revoked successfully.")
    except Exception as e:
        print(f"Error revoking file access: {e}")
    finally:
        # Close the database connection
        if mydb:
            mydb.close()

def delete_file(uid,file_id):
    documentobj = Document(uid)
    documentobj.delete(file_id)
    
