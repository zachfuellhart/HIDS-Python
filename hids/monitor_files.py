# hids/monitor_files.py

import os
import json
from utils.hash_utils import hash_file
from hids.alert_manager import log_alert

MONITORED_FILES = [
    "/etc/passwd",
    "/etc/ssh/sshd_config",
    "/home/znf5026/testfile.txt"
]

HASH_STORE = "logs/file_hashes.json"

def load_hashes():
    if os.path.exists(HASH_STORE):
        with open(HASH_STORE, "r") as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    with open(HASH_STORE, "w") as f:
        json.dump(hashes, f, indent=4)

def monitor_files():
    current_hashes = load_hashes()
    new_hashes = {}
    alerts = []

    print("[DEBUG] Current hashes loaded:", current_hashes)

    for file in MONITORED_FILES:
        file_hash = hash_file(file)
        if file_hash is None:
            alert_msg = f"File missing: {file}"
            print(f"[DEBUG] {alert_msg}")
            log_alert(alert_msg)
            alerts.append(alert_msg)
            continue

        print(f"[DEBUG] Hashed file: {file} -> {file_hash}")

        new_hashes[file] = file_hash

        if file in current_hashes:
            if file_hash != current_hashes[file]:
                alert_msg = f"File changed: {file}"
                print(f"[DEBUG] {alert_msg}")
                log_alert(alert_msg)
                alerts.append(alert_msg)
        else:
            alert_msg = f"New file hash stored: {file}"
            print(f"[DEBUG] {alert_msg}")
            log_alert(alert_msg)
            alerts.append(alert_msg)

    save_hashes(new_hashes)
    print("[DEBUG] New hashes saved:", new_hashes)
    return alerts
