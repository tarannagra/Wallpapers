import subprocess
from datetime import datetime

current_date = datetime.now().strftime("%c")

def pull() -> None:    
    subprocess.Popen(["git", "pull", "origin", "main"])

def backup() -> None:
    subprocess.Popen(["git", "add", "."])
    subprocess.Popen(["git", "commit", "-m", f"'Backup {current_date}'"])
    subprocess.Popen(["git", "push", "origin", "main"])

backup()
