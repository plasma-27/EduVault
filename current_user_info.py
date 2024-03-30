from dbConnection import *
from global_vars import *

class currentUserInfo:
    dbobj = db()
    mydb, cursor = dbobj.dbconnect("credentials")
    
    def __init__(self, user_id,user_type):
        global G_UID
        global G_Name
        global G_GENDER
        global G_DOB
        global G_PHONE
        global G_EMAIL
        global G_AADHAAR
        global G_TAN

        if(user_type=="S"):
            query = "SELECT * FROM student WHERE uid = %s"
            currentUserInfo.cursor.execute(query, (user_id,))
            result = currentUserInfo.cursor.fetchone()

            if result: 
                G_UID = self.uid = result[0]
                G_Name = self.name = result[1]
                print(G_Name)
                G_GENDER = self.gender = result[2]
                G_DOB = self.dob = result[3]
                G_PHONE = self.phone = result[4]
                G_EMAIL = self.email = result[5]
                G_AADHAAR = self.aadhaar_number = result[6]

            else:
                print(f"User with ID {user_id} not found in the 'student' table.")
        else:
            query = "SELECT * FROM institute WHERE uid = %s"
            currentUserInfo.cursor.execute(query, (user_id,))
            result = currentUserInfo.cursor.fetchone()
            
            if result:
                G_UID = self.uid = result[0]
                G_Name = result[1]
                G_TAN = self.tan = result[2]
                G_EMAIL = self.email = result[3]
                G_PHONE = self.phone = result[4]
            else:
                print(f"User with ID {user_id} not found in the 'institute' table.")    
                
# Example usage:
# Provide the user_id when creating an instance of the class
# user_id_to_fetch = "S026349951448"
# user_info = currentUserInfo(user_id_to_fetch,"S")
# print(G_Name)
