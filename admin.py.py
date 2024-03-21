from dbConnection import *
from email_send import *
class Admin:
    
    @staticmethod
    def student_list():
        students = []
        dbobj = db()
        mydb, cursor = dbobj.dbconnect("credentials")

        try:
            

            # Fetch names and UIDs of students
            query = "SELECT name, uid FROM student"
            cursor.execute(query)
            students = cursor.fetchall()

        except Exception as e:
            print(f"Error fetching student list: {e}")
        finally:
            # Close the database connection
            if mydb:
                mydb.close()

        return students

    @staticmethod
    def institute_list():
        institutes = []
        dbobj = db()
        mydb, cursor = dbobj.dbconnect("credentials")

        try:
            
            # Fetch names and UIDs of institutes
            query = "SELECT name, uid FROM institute"
            cursor.execute(query)
            institutes = cursor.fetchall()

        except Exception as e:
            print(f"Error fetching institute list: {e}")
        finally:
            # Close the database connection
            if mydb:
                mydb.close()

        return institutes

        
    
    @staticmethod
    def pending_approval_list():
        is_verified = 0
        result = []

        try:
            dbobj = db()
            mydb, cursor = dbobj.dbconnect("credentials")

            # Fetch name and uid of institutes with verified value as 0
            search_query = "SELECT name, uid FROM institute WHERE verified = %s"
            cursor.execute(search_query, (is_verified,))
            result = cursor.fetchall()

        except Exception as e:
            print(f"Error fetching pending approvals: {e}")
        finally:
            # Close the database connection
            if mydb:
                mydb.close()

        return result
    
    @staticmethod
    def grant_approval(iuid):
        email = None
        name = None

        try:
            dbobj = db()
            mydb, cursor = dbobj.dbconnect("credentials")

            # Fetch email and name before updating the verified column
            select_query = "SELECT email, name FROM institute WHERE uid = %s"
            cursor.execute(select_query, (iuid,))
            result = cursor.fetchone()

            if result:
                institute_email, name = result
                subject = "Registration Approved"
                email_message = f"hello {name}, Your registration as an Institute is Aproved"

                # Update the verified column to 1 for the specified iuid
                update_query = "UPDATE institute SET verified = 1 WHERE uid = %s"
                cursor.execute(update_query, (iuid,))

                # Commit the changes to the database
                mydb.commit()
                print(f"Approval granted for institute with UID: {iuid}")
                sendMail(institute_email,subject,email_message)

        except Exception as e:
            print(f"Error granting approval: {e}")
        finally:
            # Close the database connection
            if mydb:
                mydb.close()
        
                
                
    @staticmethod
    def suspended_student_list():
        suspended_students = []

        dbobj = db()
        mydb, cursor = dbobj.dbconnect("credentials")
        try:
            
            # Fetch students who have been suspended
            query = "SELECT uid, name FROM student WHERE suspended = 1"
            cursor.execute(query)
            suspended_students = cursor.fetchall()

        except Exception as e:
            print(f"Error fetching suspended students: {e}")
        finally:
            # Close the database connection
            if mydb:
                mydb.close()

        return suspended_students
        
    @staticmethod
    def suspend_unsuspend(uid, action):
        
        dbobj = db()
        mydb, cursor = dbobj.dbconnect("credentials")
        try:
        
            if uid.startswith("S"):
                # If uid starts with "S", update the suspended column in the student table
                update_query = "UPDATE student SET suspended = %s WHERE uid = %s"
                cursor.execute(update_query, (action, uid))
            elif uid.startswith("I"):
                # If uid starts with "I", update the suspended column in the institute table
                update_query = "UPDATE institute SET suspended = %s WHERE uid = %s"
                cursor.execute(update_query, (action, uid))
            else:
                print("Invalid uid format. Should start with 'S' or 'I'.")

            # Commit the changes to the database
            mydb.commit()
            print(f"Suspended/Unsuspended user with UID: {uid}")

        except Exception as e:
            print(f"Error updating suspended status: {e}")
        finally:
            # Close the database connection
            if mydb:
                mydb.close()

# # Example usage:
# approval_instance = Admin()
# pending_approvals = approval_instance.pending_approval_list()

# for institute in pending_approvals:
#     name, uid = institute
#     print(f"Pending Approval: Name - {name}, UID - {uid}")

# Admin.grant_approval("I129319695829")

# # Example usage:
# suspended_students_list = Admin.suspended_student_list()

# for student in suspended_students_list:
#     uid, name = student
#     print(f"Suspended Student: UID - {uid}, Name - {name}")


# Example usage:
# # Suspend a student with UID starting with "S"
# Admin.suspend_unsuspend("S692005561648", 0)

# # Unsuspend an institute with UID starting with "I"
# Admin.suspend_unsuspend("I445169232019", 0)


# # Example usage:
# students = Admin.student_list()
# print("Student List:")
# for student in students:
#     name, uid = student
#     print(f"Name: {name}, UID: {uid}")

# institutes = Admin.institute_list()
# print("\nInstitute List:")
# for institute in institutes:
#     name, uid = institute
#     print(f"Name: {name}, UID: {uid}")