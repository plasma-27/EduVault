# import tkinter as tk


# def show_information_dialog(parent, message):
#     # Create a top-level window (dialog box)
#     dialog_box = tk.Toplevel(parent)
#     dialog_box.title("Information")

#     # Set the dialog box as transient to the parent window
#     dialog_box.transient(parent)

#     # Label to display the message
#     label_message = tk.Label(dialog_box, text=message, padx=20, pady=20)
#     label_message.pack()
    
    

#     # OK button to close the dialog box
#     ok_button = tk.Button(dialog_box, text="OK", command=lambda: close_dialog(dialog_box))
#     ok_button.pack()

#     # Grab the focus to the dialog box
#     dialog_box.grab_set()

#     # Make the main window wait for the dialog box to close
#     parent.wait_window(dialog_box)

# def close_dialog(dialog_box):
#     # Function to close the dialog box
#     dialog_box.destroy()

# # Example usage
# if __name__ == "__main__":
#     # Create the main window
#     root = tk.Tk()
#     root.title("Main Window")

#     # Function to open the information dialog
#     def open_information_dialog():
#         message = "This is an informational message."
#         show_information_dialog(root, message)

#     # Button to trigger the information dialog
#     info_button = tk.Button(root, text="Show Information", command=open_information_dialog)
#     info_button.pack(pady=20)

#     # Run the main window
#     root.mainloop()
