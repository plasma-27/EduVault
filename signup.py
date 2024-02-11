from password import *
from uidGenerator import *
from dbConnection import *




def studentInsert(uid,full_name, email, dob_value, gender, contact_no, aadhaar_no, password):
    
    dbobj = db()
    mydb,cursor = dbobj.dbconnect("credentials")
    
    # Insert data into the student table
    student_query = "INSERT INTO student (uid, name, gender, dob, phone, email, aadhaar_number) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    student_data = (uid, full_name, gender, dob_value, contact_no, email, aadhaar_no)
    cursor.execute(student_query, student_data)
    
    # Insert data into the login table
    login_query = "INSERT INTO login (uid,`key`, hash) VALUES (%s, %s, %s)"
    # For simplicity, assuming 'key' is the username and 'hash' is the password hash
    login_data = (uid, full_name, password)  # Replace 'password_hash' with the actual hashed password
    cursor.execute(login_query, login_data)
    
     # Commit changes and close the connection
    mydb.commit()
    mydb.close()
    
    
    