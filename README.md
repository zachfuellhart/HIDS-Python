# 1. HIDS-Python

## 1.1 Overview
Host-Based Intrusion Detection System (HIDS) implemented in Python to monitor system log files and critical file integrity changes, and send alert emails automatically when suspicious activity is detected.

Example of what the email alerts look like in a gmail inbox:
![image](https://github.com/user-attachments/assets/272443e1-79f1-45ed-95f6-8f8ff4f6ec0b)

The project includes:
- File integrity monitoring with hash comparisons
- Authentication log monitoring for failed SSH logins
- Email alert notifications for security events
- Cron job setup for periodic automated monitoring

## 1.2 Features

- Monitors `/var/log/auth.log` for failed login attempts.
- Checks integrity of critical system files by hashing and detecting changes.
- Sends email alerts when suspicious login failures or file tampering are detected.
- Automated via cron jobs for periodic monitoring.
- Environment variable support for secure email credential management.
- Easy to extend for additional log or file monitoring.

# 2. Getting Started

## 2.1 Prerequisites 
- Python 3.8 or higher
- Virtual environment (recommended)
- SMTP email account (Gmail recommended) with App Password enabled for sending alerts
- Permission to read system files and logs (sudo)

## 2.2 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/zachfuellhart/HIDS-Python.git
   cd HIDS-Python

2. Create and activate a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Configure environment variables:
   Create a .env file in the project root with the following variables:
   ```ini
   EMAIL_SENDER=your_email@gmail.com
   EMAIL_RECEIVER=receiver_email@gmail.com
   EMAIL_PASSWORD=your_email_password_or_app_password

5. Run the main monitoring script manually or via cron:
   ```bash
   python -m hids.main

6. (Optional) Setup cron to automate monitoring every 5 minutes:
   ```cron
   */5 * * * * cd /home/znf5026/HIDS-Python && /home/znf5026/HIDS-Python/venv/bin/python3 -m hids.main >> /home/znf5026/HIDS-Python/logs/cron_output.log 2>&1

## 2.3 Project Structure
HIDS-Python/
- ├── hids/
- │   ├── __init__.py              # Makes this a Python package
- │   ├── alert_manager.py         # Handles alerts when something suspicious happens
- │   ├── email_config.py          # Stores email settings (sender, receiver, password)
- │   ├── file_hashes.json         # Keeps track of original file hashes
- │   ├── main.py                  # Runs the HIDS system
- │   ├── monitor_files.py         # Checks if important files have been changed
- │   ├── monitor_logs.py          # Looks for suspicious activity in logs
- │   ├── send_email_alert.py      # Sends alert emails
- ├── utils/
- │   ├──hash_utils.py             # Helps with file hashing
- ├── .gitignore                   # Tells Git which files to ignore
- ├── LICENSE                      # Open-source license (MIT)
- ├── README.md                    # Project guide and instructions
- ├── requirements.txt             # List of needed Python packages
- ├── test_email.py                # Tests if email alerts are working

# 3. Usage
- Run the monitoring manually using:
   ```bash
   python -m hids.main
- Review alerts printed to console and saved in log files.
- Check your email for alert notifications on file changes or suspicious logins.
- Use cron to automate running the monitor periodically for continuous protection.

# 4. License
This project is licensed under the MIT License - see the LICENSE file for details.

# 5. Contact
- Created by Zachary Fuellhart.
- email: znf5026@psu.edu
- GitHub: zachfuellhart
- Feel free to reach out for questions or collaboration.



   
