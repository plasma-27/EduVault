import random
import tkinter as tk
from email_send import *
from current_user_info import *


def generate_otp():
    return random.randint(100000, 999999)

def verify_otp(entered_otp, generated_otp):
    entered_otp = int(entered_otp)  # Convert entered_otp to integer
    return entered_otp == generated_otp
    # return True

def otp_send(generated_otp,user_info):
    
    username = user_info.name.capitalize()
    
    email = user_info.email
    subject = "Signing in? Here's your OTP."
    message = f"Hello {username}, Your OTP to log in to your account is {generated_otp}"
    sendMail(email, subject, message)
    
    
 