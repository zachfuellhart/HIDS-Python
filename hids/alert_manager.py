# hids/alert_manager.py
import logging

# Set up logging configuration
logging.basicConfig(
    filename="logs/hids_alerts.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def log_alert(message):
    print("[ALERT]", message)
    logging.info(message)
