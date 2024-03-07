from dbConnection import *


class StorageQuota:
    def __init__(self, uid):
        self.uid = uid

    def view_storage_quota(self):
        dbobj = db()
        mydb, cursor = dbobj.dbconnect("documents")
        
        try:
            query = "SELECT storage_limit FROM storage_quota WHERE uid = %s"
            cursor.execute(query, (self.uid,))
            storage_limit = cursor.fetchone()
            
            if storage_limit:
                return storage_limit[0]  # Return the storage limit for the specified user
            else:
                return None  # Return None if no storage limit is found for the given user
        finally:
            if mydb:
                mydb.close()
            if cursor:
                cursor.close()

    def storage_quota_increment(self, file_size):
        current_quota = self.view_storage_quota()

        if current_quota is not None:
            new_quota = min(current_quota + file_size, 1048576)  # Ensure the new quota does not exceed the maximum limit
            self.update_storage_quota(new_quota)

    def storage_quota_decrement(self, file_size):
        current_quota = self.view_storage_quota()

        if current_quota is not None:
            new_quota = max(current_quota - file_size, 0)  # Ensure the new quota is not negative
            self.update_storage_quota(new_quota)

    def is_quota_full(self, file_size):
        current_quota = self.view_storage_quota()

        if current_quota is not None:
            return (current_quota + file_size) > 1048576  # Check if the new quota exceeds the maximum limit
        else:
            return False  # Assume quota is not full if no storage limit is found

    def initialise_storage_quota(self):
        initial_quota_gb = 1
        initial_quota_bytes = initial_quota_gb * 1024 * 1024 * 1024  # Convert GB to bytes
    
        dbobj = db()
        mydb, cursor = dbobj.dbconnect("documents")
    
        try:
            insert_query = "INSERT INTO storage_quota (uid, storage_limit) VALUES (%s, %s)"
            cursor.execute(insert_query, (self.uid, initial_quota_bytes))
            mydb.commit()
        finally:
            if mydb:
                mydb.close()
            if cursor:
                cursor.close()


    def update_storage_quota(self, new_quota):
        dbobj = db()
        mydb, cursor = dbobj.dbconnect("documents")
        
        try:
            update_query = "UPDATE storage_quota SET storage_limit = %s WHERE uid = %s"
            cursor.execute(update_query, (new_quota, self.uid))
            mydb.commit()
        finally:
            if mydb:
                mydb.close()
            if cursor:
                cursor.close()


# Example usage:
# uid = 'your_user_id'
# storage_quota_obj = StorageQuota(uid)
# storage_quota_obj.initialise_storage_quota()  # Initialize storage quota for the user
# is_full = storage_quota_obj.is_quota_full(512)  # Check if the quota will be full after adding 512 bytes
# print(is_full)
