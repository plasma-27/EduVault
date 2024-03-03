from dbConnection import *
from datetime import datetime
import tkinter as tk
from tkinter import ttk

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


def fetch_login_data(uid):
    try:
        dbobj = db()
        mydb, cursor = dbobj.dbconnect("credentials")
        select_query = "SELECT lastlogin FROM last_login WHERE uid = %s ORDER BY lastlogin DESC"
        cursor.execute(select_query, (uid,))
        results = cursor.fetchall()
        dbobj.dbclose(mydb, cursor)
        return results
    except mysql.connector.Error as error:
        print("Error fetching login data:", error)
        return []

def display_login_data(uid):
    login_data = fetch_login_data(uid)

    root = tk.Tk()
    root.title("Login Data")

    for login_time in login_data:
        login_label = tk.Label(root, text=login_time[0].strftime("%Y-%m-%d %H:%M:%S"))
        login_label.pack()

    root.mainloop()
    
# Example usage
# uid = "S477729132063"


# last_login_time = get_last_login(uid)
# print(last_login_time)


# update_last_login(uid)


# last_login_time = get_last_login(uid)
# print(last_login_time)
# 
# display_login_data(uid)