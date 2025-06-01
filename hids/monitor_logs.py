# hids/monitor_logs.py

from hids.alert_manager import log_alert  # ✅ Import the logger

def parse_auth_log(log_file="/var/log/auth.log"):
    failed_lines = []
    with open(log_file, "r") as f:
        for line in f:
            if "Failed password" in line:
                failed_lines.append(line.strip())
                log_alert(f"Failed login detected: {line.strip()}")
    return failed_lines


