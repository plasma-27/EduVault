import mysql.connector
from mysql.connector import Error
import mimetypes
import subprocess
import tempfile
import io
from dbConnection import *


def store_file_in_database(filename, file_data):
    """Store a file in the MySQL database."""
    try:
        dbobj = db()
        mydb,cursor = dbobj.dbconnect("documents")
        insert_query = "INSERT INTO files (file_name, file_data) VALUES (%s, %s)"
        cursor.execute(insert_query, (filename, file_data))
        mydb.commit()
        mydb.close()
        
        print("File stored in database successfully")
    except Error as e:
        print(f"Error storing file in database: {e}")

def retrieve_file_from_database(file_id):
    """Retrieve a file from the MySQL database."""
    try:
        dbobj = db()
        mydb,cursor = dbobj.dbconnect("documents")
        
        select_query = "SELECT file_name, file_data FROM files WHERE file_id = %s"
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

def determine_file_type(filename):
    """Determine the file type based on the filename."""
    file_type, _ = mimetypes.guess_type(filename)
    return file_type


def open_file_with_default_program(file_data, file_type):
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


def store(filename):
    try:
        with open(filename, "rb") as file:
            file_data = file.read()
            print("File data:", file_data)  # Print file data for debugging
            store_file_in_database(filename, file_data)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

        
def retrieve(file_id):
    file_id = file_id  # Change this to the ID of the file you want to retrieve
    filename, file_data = retrieve_file_from_database(file_id)
    if file_data:
        file_type = determine_file_type(filename)  # Pass filename instead of file_data
        if file_type:
            open_file_with_default_program(file_data, file_type)

            
            
            
            
# store("/home/quantum/Pictures/Screenshot.png")            
# retrieve(6)