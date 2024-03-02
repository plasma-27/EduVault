import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the SMTP server
smtp_server = 'smtp.gmail.com'
port = 587  # or 25 or 465 depending on your SMTP server configuration
sender_email = 'eduvault.bot@gmail.com'
password = 'acfg jxch yhrf vjlp'

recipient_email = 'voiduser278@gmail.com'

# Create a message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = 'Test mail from Eduvault'

# Add body to email
body = 'Test mail sent from python module'
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
    
