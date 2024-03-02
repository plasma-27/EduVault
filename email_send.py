import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sensitive_credentials import *

def sendMail(recipient,subject,mail_message):
    recipient_email = recipient
    message_to_send = mail_message
    message_subject = subject
    # Set up the SMTP server
    smtp_server = 'smtp.gmail.com'
    port = 587
    sender_email =  server_email   #Add your email id which application will use for sending OTP
    password = server_password     #Email password
    

    

    # Create a message          
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = message_subject

    # Add body to email
    body = message_to_send
    message.attach(MIMEText(body, 'plain'))

    try: 
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)

        # Send email
        server.sendmail(sender_email, recipient_email, message.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print("Failed to send email:", str(e))

    finally:
        # Close the connection
        server.quit()
    
