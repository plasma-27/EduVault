import os
import pyAesCrypt

class fileCrypt:
    
    @staticmethod
    def encrypt(filename, key):
        base_filename = os.path.basename(filename)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.abspath(os.path.join(script_dir, ".."))  # Navigate up one directory from the script directory
        UPLOAD_BUFFER_DIR = os.path.join(root_dir, "testing", "uploadBuffer")
        encrypted_filename = os.path.join(UPLOAD_BUFFER_DIR, base_filename + ".aes")
        
        pyAesCrypt.encryptFile(filename, encrypted_filename, key)
        
        print("File encrypted:", encrypted_filename)  # Print for debugging
        return encrypted_filename
