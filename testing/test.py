import tkinter as tk
from tkinter import simpledialog

class OTPDialog:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("OTP Verification")

        self.otp_label = tk.Label(self.top, text="Please enter the OTP:")
        self.otp_label.pack(pady=10)

        # Entry widget for OTP input
        self.otp_entry = tk.Entry(self.top)
        self.otp_entry.pack(pady=10)

        # OK button to get the OTP and close the child window
        self.ok_button = tk.Button(self.top, text="OK", command=self.top.destroy)
        self.ok_button.pack(pady=10)

        # Make the OTP dialog modal
        self.top.transient(parent)
        self.top.grab_set()
        parent.wait_window(self.top)

    def get_otp(self):
        return self.otp_entry.get()

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Window")

    # Function to open the OTP dialog
    def open_otp_dialog():
        otp_dialog = OTPDialog(root)
        otp = otp_dialog.get_otp()

        if otp:
            print("OTP entered:", otp)
            # Process the OTP here
        else:
            print("OTP entry canceled.")

    # Button to trigger the OTP dialog
    otp_button = tk.Button(root, text="Open OTP Dialog", command=open_otp_dialog)
    otp_button.pack(pady=20)

    # Run the main window
    root.mainloop()
