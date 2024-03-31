
import tkinter as tk
from tkinter import ttk
from file_operations_interface import *

class UploadDocumentsWindow:
    def __init__(self, uid, root):
        self.uid = uid
        self.root = root
        self.root.title("Upload Documents")
        self.root.geometry("400x200")

        # Predefined lists for dropdowns
        self.document_names_dict = {
            "category1": ["doc1", "doc2"],
            "category2": ["doc3", "doc4"],
            "category3": ["doc5", "doc6"]
        }
        self.categories = list(self.document_names_dict.keys())

        # StringVars for document name and category
        self.document_name_var = tk.StringVar(self.root)
        self.category_var = tk.StringVar(self.root)

        # Dropdown for categories
        category_label = tk.Label(self.root, text="Category:")
        category_combobox = ttk.Combobox(self.root, textvariable=self.category_var, values=self.categories, state="readonly")
        category_combobox.bind("<<ComboboxSelected>>", self.update_document_names)
        category_label.pack(pady=10)
        category_combobox.pack(pady=10)

        # Dropdown for document names
        document_name_label = tk.Label(self.root, text="Document Name:")
        self.document_name_combobox = ttk.Combobox(self.root, textvariable=self.document_name_var, state="readonly")
        document_name_label.pack(pady=10)
        self.document_name_combobox.pack(pady=10)

        # Upload button
        upload_button = tk.Button(self.root, text="Upload File", command=self.upload_file)
        upload_button.pack(pady=10)

    def update_document_names(self, event):
        selected_category = self.category_var.get()
        document_names = self.document_names_dict.get(selected_category, [])
        self.document_name_combobox["values"] = document_names
        if document_names:
            self.document_name_var.set(document_names[0])  # Set the first document name by default
            self.document_name_combobox["state"] = "readonly"
        else:
            self.document_name_combobox["state"] = "disabled"

    def upload_file(self):
        # Get selected values from comboboxes
        document_name = self.document_name_var.get()
        category = self.category_var.get()
        
        upload_file_selector(self.uid, document_name, category)

        # Use these values for further processing, for example, calling the upload_file function
        # upload_file(self.uid, document_name, category)

        # For now, just print the selected values
        print(f"Uploading file for UID {self.uid}, Document Name: {document_name}, Category: {category}")

        # You can uncomment the above line and remove the print statement when integrating with your actual upload logic

# Example usage
uid = "S026349951448"
root = tk.Tk()
upload_window = UploadDocumentsWindow(uid, root)
root.mainloop()
