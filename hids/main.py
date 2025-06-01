from dotenv import load_dotenv
load_dotenv()  # Ensure .env is loaded when running main.py directly

from hids.monitor_logs import parse_auth_log
from hids.monitor_files import monitor_files
from hids.email_config import send_email_alert, email_sender, email_receiver, email_password  # import env vars for debug

def main():
    print("[INFO] Running HIDS checks...")

    # Debug prints to check environment variables
    print(f"[DEBUG] Email sender: {email_sender}")
    print(f"[DEBUG] Email receiver: {email_receiver}")
    print(f"[DEBUG] Email password loaded: {'Yes' if email_password else 'No'}")

    alert_sent = False  # Flag to track if any alert email was sent

    # Check failed login attempts
    failed_logins = parse_auth_log()
    if failed_logins:
        print("[INFO] Failed login attempts detected.")
        message = "[ALERT] Failed login attempts:\n" + "\n".join(failed_logins)
        print("[DEBUG] About to send failed login alert email...")
        send_email_alert("HIDS Alert: Failed Logins", message)
        print("[INFO] Alert email sent successfully for failed logins.")
        alert_sent = True

    # Check files for unexpected changes
    file_alerts = monitor_files()
    if file_alerts:
        print("[INFO] File integrity changes detected.")
        message = "[ALERT] File integrity changes:\n" + "\n".join(file_alerts)
        print("[DEBUG] About to send file changes alert email...")
        send_email_alert("HIDS Alert: File Changes", message)
        print("[INFO] Alert email sent successfully for file changes.")
        alert_sent = True

    # Only send a test email if no alert was sent
    if not alert_sent:
        print("[DEBUG] No alerts detected. Sending a test email to verify email function...")
        send_email_alert("HIDS Alert: Test Email", "This is a test email from main.py")
        print("[INFO] Test email sent.")

if __name__ == "__main__":
    main()

