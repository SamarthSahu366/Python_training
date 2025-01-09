from datetime import datetime

def log_activity(username, action):
    with open("user_activity.log", "a") as log_file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_file.write(f"{timestamp} - {username}: {action}\n")
