import os
import subprocess
import sys
from threading import Thread
import argparse

"""
run:
python clean-browser.py $url
or
python clean-browser.py github twitch <- NEW name the site. Wish it was more flexible tho
or
python clean-browser.py github soundcloud.com <- NEW combine urls with sites

"""
# TODO: integrate an argument parse option so we could call e.g. -chrome -edge, etc...

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
    "amazon": "https://amazon.com"
}

for argument in args[1:]:

    def match_or_literal(argument):
        if argument in sites_dict.keys():
            return sites_dict[argument]
        # it might be an incomplete url so:
        else:
            return argument if argument.startswith("http") else "https://" + argument

    url = match_or_literal(argument)

    def find_browser():
        # TODO: make this a dict so we can choose the preferred browser
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
            f"--app={url}"
        ]
        return flags

    browser_path = find_browser()
    browser_command = get_browser_command()

    def start_browser():
        subprocess.run(browser_command)

    print(f"opening url: {url}")
    browser_thread = Thread(target=start_browser)
    browser_thread.start()
