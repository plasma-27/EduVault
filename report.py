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

# Example usage:
reports = Report.view_report()

# Display the reports
for report_data in reports:
    report_id, reported_by, reported_to, message, action_taken = report_data
    print(f"Report ID: {report_id}, Reported By: {reported_by}, Reported To: {reported_to}, Message: {message}, Action Taken: {action_taken}")
