# HIDS-Python

Host-Based Intrusion Detection System (HIDS) implemented in Python to monitor system log files and critical file integrity changes, and send alert emails automatically when suspicious activity is detected.

## Features

- Monitors `/var/log/auth.log` for failed login attempts.
- Checks integrity of critical system files by hashing and detecting changes.
- Sends email alerts when suspicious login failures or file tampering are detected.
- Automated via cron jobs for periodic monitoring.
- Environment variable support for secure email credential management.
- Easy to extend for additional log or file monitoring.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/zachfuellhart/HIDS-Python.git
   cd HIDS-Python

2. Create and activate a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
