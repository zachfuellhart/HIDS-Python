import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText

# Load environment variables
load_dotenv()

# Print for debug
print("Sender:", os.getenv("HIDS_EMAIL_SENDER"))
print("Receiver:", os.getenv("HIDS_EMAIL_RECEIVER"))
print("Password Length:", len(os.getenv("HIDS_EMAIL_PASSWORD")))

# Use environment variables
sender = os.getenv("HIDS_EMAIL_SENDER")
receiver = os.getenv("HIDS_EMAIL_RECEIVER")
password = os.getenv("HIDS_EMAIL_PASSWORD")

# Compose the email
subject = "Test Email from HIDS"
body = "This is a test email sent from the HIDS test script."

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
    print("Test email sent successfully!")
except Exception as e:
    print(f"Failed to send test email: {e}")
