from dbConnection import *
from datetime import datetime


def update_last_login(uid):
    try:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dbobj = db()
        mydb, cursor = dbobj.dbconnect("credentials")

        # Insert new record for last login time
        insert_query = "INSERT INTO last_login (uid, lastlogin) VALUES (%s, %s)"
        cursor.execute(insert_query, (uid, now))

        mydb.commit()
        dbobj.dbclose(mydb, cursor)
        print("Last login updated successfully.")
    except mysql.connector.Error as error:
        print("Error updating last login:", error)

       
def get_last_login(uid):
    try:
        dbobj = db()
        mydb, cursor = dbobj.dbconnect("credentials")
        select_query = "SELECT lastlogin FROM last_login WHERE uid = %s ORDER BY lastlogin DESC LIMIT 1 OFFSET 1"
        cursor.execute(select_query, (uid,))
        result = cursor.fetchone()
        dbobj.dbclose(mydb, cursor)
        
        if result:  # Check if the result is not empty
            dbtime = result[0]
            formatted_time = dbtime.strftime("%d-%m-%Y %I:%M:%S %p")  # Include seconds in the format
            return formatted_time
        else:
            return None
    except mysql.connector.Error as error:
        print("Error retrieving last login:", error)





# Example usage
# uid = "S477729132063"


# last_login_time = get_last_login(uid)
# print(last_login_time)


# update_last_login(uid)


# last_login_time = get_last_login(uid)
# print(last_login_time)