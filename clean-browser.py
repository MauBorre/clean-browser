import os
import subprocess
import sys
from threading import Thread

"""
run:
python clean-browser.py $url
or
python clean-browser.py github twitch
or
python clean-browser.py github soundcloud.com
"""

args = sys.argv

sites_dict = {
    "github": "https://github.com",
    "twitch": "https://twitch.tv",
    "youtube": "https://youtube.com",
    "google": "https://google.com",
    "twitter": "https://twitter.com",
    "gmail": "https://gmail.com",
    "soundcloud": "https://soundcloud.com",
    "reddit": "https://reddit.com",
    "chatgpt": "https://chat.openai.com",
    "bard": "https://bard.google.com",
    "amazon": "https://amazon.com",
    "whatsapp": "https://web.whatsapp.com/",
    "kick": "https://kick.com",
    "mercadolibre": "https://mercadolibre.com.ar",
    "gemini": "https://gemini.google.com"
}

def match_else_complete(argument):
    if argument in sites_dict.keys():
        return sites_dict[argument]
    else: # it might be an incomplete url so:
        return argument if argument.startswith("http") else "https://" + argument

def find_browser():
    paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ]
    for path in paths:
        if os.path.exists(path):
            return path
    return None

def get_browser_command(browser_path):
        flags = [
            browser_path,
            f"--user-data-dir=",
            "--new-window",
            "--no-first-run",
            f"--app={url}"
        ]
        return flags

def start_browser(command_flags):
        subprocess.run(command_flags)

_browser_path = find_browser()

for argument in args[1:]:
    url = match_else_complete(argument)
    browser_command = get_browser_command(_browser_path)
    print(f"opening url: {url}")
    browser_thread = Thread(target=start_browser(browser_command))
    browser_thread.start()
