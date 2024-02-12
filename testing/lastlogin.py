import mysql.connector
from datetime import datetime

def connect_to_mysql():
    # Connect to MySQL database
    return mysql.connector.connect(
        host='your_host',
        user='your_username',
        password='your_password',
        database='your_database'
    )

def update_last_login(uid, connection):
    # Update last login time for the user
    now = datetime.now().strftime("%d-%m-%y %I:%M %p")
    cursor = connection.cursor()
    update_query = "UPDATE last_login SET lastlogin = %s WHERE uid = %s"
    cursor.execute(update_query, (now, uid))
    connection.commit()
    cursor.close()

def get_last_login(uid, connection):
    # Retrieve last login time for the user
    cursor = connection.cursor()
    select_query = "SELECT lastlogin FROM last_login WHERE uid = %s"
    cursor.execute(select_query, (uid,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return result[0]
    else:
        return None

# Example usage
uid = "example_user"

# Connect to MySQL database
connection = connect_to_mysql()

# Update last login time when the user logs in
update_last_login(uid, connection)

# Retrieve and display the last login time
last_login_time = get_last_login(uid, connection)
if last_login_time:
    print(f"Last login time for {uid}: {last_login_time}")
else:
    print(f"No login record found for {uid}")

# Close the database connection
connection.close()
