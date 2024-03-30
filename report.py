from dbConnection import db

class Report:
    
    @staticmethod
    def view_report():
        reports_list = []

        try:
            dbobj = db()
            mydb, cursor = dbobj.dbconnect("credentials")

            # Fetch report data
            query = "SELECT report_id, reported_by, reported_to, message, action_taken FROM reports"
            cursor.execute(query)
            reports_list = cursor.fetchall()

        except Exception as e:
            print(f"Error fetching reports: {e}")
        finally:
            # Close the database connection
            if mydb:      
                mydb.close()

        return reports_list
    
    @staticmethod
    def submit_report(iuid, suid, message):
        try:
            dbobj = db()
            mydb, cursor = dbobj.dbconnect("credentials")
            
            # Insert report data into the database with action_taken set to 0
            query = "INSERT INTO reports (reported_by, reported_to, message, action_taken) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (iuid, suid, message, 0))
            mydb.commit()
            report_id = cursor.lastrowid

            print("Report submitted successfully!")
            return report_id

        except Exception as e:
            print(f"Error submitting report: {e}")
            return None
        finally:
            # Close the database connection
            if mydb:
                mydb.close()





# # Example usage:
# reports = Report.view_report()

# # Display the reports
# for report_data in reports:
#     report_id, reported_by, reported_to, message, action_taken = report_data
#     print(f"Report ID: {report_id}, Reported By: {reported_by}, Reported To: {reported_to}, Message: {message}, Action Taken: {action_taken}")
