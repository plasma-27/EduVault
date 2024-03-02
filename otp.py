import random
import tkinter as tk
from tkinter import simpledialog

def generate_otp():
    return random.randint(100000, 999999)

def verify_otp(entered_otp, generated_otp):
    entered_otp = int(entered_otp)  # Convert entered_otp to integer
    return entered_otp == generated_otp

# def show_otp_dialog():
#     root = tk.Tk()
#     root.withdraw()  # Hide the main window

#     generated_otp = generate_otp()

#     otp = simpledialog.askstring("OTP Verification", f"Generated OTP: {generated_otp}\nPlease enter the OTP:", parent=root)

#     if otp:
#         print("OTP entered:", otp)
#         if verify_otp(otp, generated_otp):
#             print("OTP is correct.")
#             # Process the OTP here
#         else:
#             print("Incorrect OTP.")
#     else:
#         print("OTP entry canceled.")

# # Example usage
# show_otp_dialog()
