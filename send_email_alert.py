import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def send_email_alert(subject, message):
    sender = os.getenv("HIDS_EMAIL_SENDER")
    receiver = os.getenv("HIDS_EMAIL_RECEIVER")
    password = os.getenv("HIDS_EMAIL_PASSWORD")

    print(f"[DEBUG] send_email_alert called")
    print(f"[DEBUG] sender={sender}, receiver={receiver}, password length={len(password) if password else 'None'}")
    print(f"[DEBUG] subject={subject}")
    print(f"[DEBUG] message={message[:50]}...")  # print first 50 chars only

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
        print("[DEBUG] Email sent successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")


