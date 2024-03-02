from dbConnection import *

class currentUserInfo:
    dbobj = db()
    mydb, cursor = dbobj.dbconnect("credentials")
    
    def __init__(self, user_id):
        query = "SELECT * FROM student WHERE uid = %s"
        currentUserInfo.cursor.execute(query, (user_id,))
        result = currentUserInfo.cursor.fetchone()

        if result:
            self.uid = result[0]
            self.name = result[1]
            self.gender = result[2]
            self.dob = result[3]
            self.phone = result[4]
            self.email = result[5]
            self.aadhaar_number = result[6]
        else:
            print(f"User with ID {user_id} not found in the 'student' table.")

# Example usage:
# Provide the user_id when creating an instance of the class
# user_id_to_fetch = "S477729132063"
# user_info = currentUserInfo(user_id_to_fetch)
