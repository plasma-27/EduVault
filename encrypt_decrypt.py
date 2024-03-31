import os
import mimetypes
import pyAesCrypt
import uuid

class fileCrypt:
    
    
    
    @staticmethod
    def determine_decrypted_file_type(file_type):
        """Determine the file extension based on the file_type."""
        if file_type == "image/jpeg":
            return ".jpeg"
        elif file_type == "image/png":
            return ".png"
        elif file_type == "application/pdf":
            return ".pdf"
        else:
            return None  # Return None for unsupported file types or if file_type is None
    
    @staticmethod
    def encrypt(filename, key):
        base_filename = os.path.basename(filename)
        UPLOAD_BUFFER_DIR = os.path.join(os.getcwd(), "persistentStorage")
        encrypted_filename = os.path.join(UPLOAD_BUFFER_DIR, base_filename + ".aes")
        
        pyAesCrypt.encryptFile(filename, encrypted_filename, key)
        
        print("File encrypted:", encrypted_filename)  # Print for debugging
        return encrypted_filename
    
    
   
  
    
    @staticmethod
    def decrypt(filename, file_type, file_data, key):
        # Specify the directory to store the encrypted and decrypted files
        upload_buffer_dir = os.path.join(os.getcwd(), "persistentStorage")
        
        # Write the encrypted file to the specified directory
        print(filename)
        encrypted_filename = os.path.join(upload_buffer_dir, filename)
        with open(encrypted_filename, "wb") as encrypted_file:
            encrypted_file.write(file_data)
        
        #Determine Decrypted filename
        file_extension = fileCrypt.determine_decrypted_file_type(file_type)

        # Decrypt the encrypted file
        decrypted_filename = os.path.join(upload_buffer_dir, filename + file_extension)
        pyAesCrypt.decryptFile(encrypted_filename, decrypted_filename, key)
        print("File decrypted:", decrypted_filename)  # Print for debugging
        
        
        return decrypted_filename
    
