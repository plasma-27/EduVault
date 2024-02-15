import sys
# sys.path.append('/home/quantum/vscode/eduVault')  # Adjust the path accordingly
from dbConnection import *
from datetime import datetime



def update_last_login(uid):
    try:
        # Update last login time for the user
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Correct datetime format
        dbobj = db()
        mydb, cursor = dbobj.dbconnect("credentials")
        update_query = "UPDATE last_login SET lastlogin = %s WHERE uid = %s"
        cursor.execute(update_query, (now, uid))
        mydb.commit()
        dbobj.dbclose(mydb, cursor)
        print("Last login updated successfully.")
    except mysql.connector.Error as error:
        print("Error updating last login:", error)


def get_last_login(uid):
    # Retrieve last login time for the user
    dbobj = db()
    mydb, cursor = dbobj.dbconnect("credentials")
    select_query = "SELECT MAX(lastlogin) FROM last_login WHERE uid = %s"
    cursor.execute(select_query, (uid,))
    result = cursor.fetchone()
    dbobj.dbclose(mydb, cursor)
    
    if result[0] is not None:  # Check if the result is not None
        dbtime = result[0]
        formatted_time = dbtime.strftime("%d-%m-%Y %I:%M:%S %p")  # Include seconds in the format
        return formatted_time
    else:
        return None





# Example usage
# uid = "S477729132063"


# last_login_time = get_last_login(uid)
# print(last_login_time)


# update_last_login(uid)


# last_login_time = get_last_login(uid)
# print(last_login_time)