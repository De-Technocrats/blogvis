#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import random
import time
import sys
from termcolor import colored

# Create a function for typing animation


def print_animation(text, color):
    for char in text:
        sys.stdout.write(colored(char, color))
        sys.stdout.flush()
        time.sleep(0.05)
    print()


# Create ASCII art banners
banner = """
                         __..--.._
  .....              .--~  .....  `.
.":    "`-..  .    .' ..-'"    :". `
` `._ ` _.'`"(     `-"'`._ ' _.' '
     ~~~      `.          ~~~
              .'
             /
            (
             ^---'
𝕮𝖗𝖊𝖆𝖙𝖔𝖗 : 𝕴𝖋𝖚𝖑𝖃𝖕𝖑𝖔𝖎𝖙 𝖃 𝕯𝖊-𝕿𝖊𝖈𝖍𝖓𝖔𝖈𝖗𝖆𝖙𝖘
▄▄▄▄· ▄▄▌         ▄▄ •  ▌ ▐·▪  .▄▄ · 
▐█ ▀█▪██•  ▪     ▐█ ▀ ▪▪█·█▌██ ▐█ ▀. 
▐█▀▀█▄██▪   ▄█▀▄ ▄█ ▀█▄▐█▐█•▐█·▄▀▀▀█▄
██▄▪▐█▐█▌▐▌▐█▌.▐▌▐█▄▪▐█ ███ ▐█▌▐█▄▪▐█
·▀▀▀▀ .▀▀▀  ▀█▄▀▪·▀▀▀▀ . ▀  ▀▀▀ ▀▀▀▀ 
𝕲𝖗𝖊𝖆𝖙 𝖙𝖍𝖆𝖓𝖐𝖘 𝖙𝖔 𝕲𝖆𝖑𝖎𝖍𝕬𝕻, 𝕯𝖗.𝕰𝖊𝖗𝖎𝖊 & 𝕬𝖑𝖑 𝖒𝖊𝖒𝖇𝖊𝖗 𝕯𝖊 𝖙𝖊𝖈𝖍𝖓𝖔𝖈𝖗𝖆𝖙𝖘.
"""

# Requesting URL input from the user
print(colored(banner, 'green'))
print_animation("Enter the blogger article link", 'yellow')
url = input(' > ')

# Request input number of requests from the user
print_animation("Enter the number of visitors to be sent", 'yellow')
num_requests = input(' > ')

# Read the list of user agents from the txt file
with open("user-agent.txt", "r") as f:
    user_agents = f.readlines()

# Remove the newline character from each list element
user_agents = [ua.strip() for ua in user_agents]

# Make a typing animation for when sending a request
print_animation("Send visitors...", 'yellow')
for i in range(10):
    time.sleep(0.2)
    sys.stdout.write(colored(".", 'yellow'))
    sys.stdout.flush()
print()

# Loop to send request
for i in range(int(num_requests)):
    # Random user agent from list of read from txt file
    user_agent = random.choice(user_agents)

    # Create a header with the selected user agent
    headers = {
        "User-Agent": user_agent
    }

    try:
        # Sending requests with predefined headers
        response = requests.get(url, headers=headers)

        # Displays the status code of the response
        print_animation(
            f"Visitor #{i+1} - Status code: {response.status_code} Succes", 'cyan')
    except requests.exceptions.RequestException as e:
        # Displays an error message if the request fails
        print_animation(f"Visitor #{i+1} - Error: {e}", 'red')
