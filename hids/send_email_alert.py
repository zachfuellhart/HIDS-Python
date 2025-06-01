# hids/send_email_alert.py

import smtplib
from email.mime.text import MIMEText
from hids.email_config import email_sender, email_receiver, email_password

def send_email_alert(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email_sender
    msg['To'] = email_receiver

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(email_sender, email_password)
            server.sendmail(email_sender, email_receiver, msg.as_string())
        print("[EMAIL] Alert email sent successfully.")
    except Exception as e:
        print(f"[EMAIL] Failed to send alert: {e}")
