import os
import mimetypes
import pyAesCrypt

class fileCrypt:
    
    
    
    @staticmethod
    def determine_file_type(filename):
        """Determine the file type based on the filename."""
        file_type, _ = mimetypes.guess_type(filename)
        return file_type
    
    @staticmethod
    def encrypt(filename, key):
        base_filename = os.path.basename(filename)
        UPLOAD_BUFFER_DIR = os.path.join(os.getcwd(), "persistentStorage")
        encrypted_filename = os.path.join(UPLOAD_BUFFER_DIR, base_filename + ".aes")
        
        pyAesCrypt.encryptFile(filename, encrypted_filename, key)
        
        print("File encrypted:", encrypted_filename)  # Print for debugging
        return encrypted_filename
    
    
   
  
    
    @staticmethod
    def decrypt(filename, file_data, key):
        # Specify the directory to store the encrypted and decrypted files
        upload_buffer_dir = os.path.join(os.getcwd(), "persistentStorage")
        
        # Write the encrypted file to the specified directory
        encrypted_filename = os.path.join(upload_buffer_dir, filename)
        with open(encrypted_filename, "wb") as encrypted_file:
            encrypted_file.write(file_data)
        
        # Decrypt the encrypted file
        decrypted_filename = os.path.join(upload_buffer_dir, "decrypted_" + filename[:-4])
        pyAesCrypt.decryptFile(encrypted_filename, decrypted_filename, key)
        print("File decrypted:", decrypted_filename)  # Print for debugging
        
        file_type = fileCrypt.determine_file_type(decrypted_filename)
        
        return decrypted_filename, file_type