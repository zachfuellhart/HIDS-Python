import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText

load_dotenv()  # <-- Make sure this is here at the very top

email_sender = os.getenv("HIDS_EMAIL_SENDER")
email_password = os.getenv("HIDS_EMAIL_PASSWORD")
email_receiver = os.getenv("HIDS_EMAIL_RECEIVER")

def send_email_alert(subject, body):
    print(f"[DEBUG] Using sender: {email_sender}, receiver: {email_receiver}")
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email_sender
    msg['To'] = email_receiver

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(email_sender, email_password)
            server.sendmail(email_sender, email_receiver, msg.as_string())
        print("[INFO] Alert email sent successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to send alert email: {e}")


