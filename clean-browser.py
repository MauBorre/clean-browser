import os
from threading import Thread
import subprocess
import sys

"""
run:
python clean-browser *url*

"""

url = sys.argv[1]

def find_browser():
    paths = [
        "C:\Program Files\Google\Chrome\Application\chrome.exe",
        "C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe",
        "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ]
    for path in paths:
        if os.path.exists(path):
            return path
    return None

def get_browser_command():
    flags = [
        browser_path,
        f"--user-data-dir=",
        "--new-window",
        "--no-first-run",
    ]

    flags.extend([f"--app={url}"])

    return flags

browser_path = find_browser()
browser_command = get_browser_command()

def start_browser():
    subprocess.run(browser_command)

browser_thread = Thread(target=start_browser)

browser_thread.start()