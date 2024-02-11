import mysql.connector

class db:
    # Connect to MySQL database
    def dbconnect(self,database):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Admin@123",
        database=database
        )
    
        # Create a cursor object
        mycursor = mydb.cursor()
        return mydb, mycursor
    
    def dbclose(self, db, cursor):
        cursor.close()
        db.close()




