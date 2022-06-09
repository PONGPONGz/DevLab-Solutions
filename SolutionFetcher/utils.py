import requests
import os
from infos import *

# Create folders if not exist.
def create_folders():
    for i in range(1, 6):
        os.makedirs(f"../{i} Stars", exist_ok=True)

def request(path):
    return requests.get(url=API_URL + path, cookies=COOKIES)

def clean_filename(name):
    # remove illegal characters from string (these characters cannot be used in naming file)
    for i in '?:*"\'$><|':
        if i in name:
            name = name.replace(i, '')
            # print('cleaner: removed {} from {}'.format(i, name))
    name = name.strip()     # remove whitespaces before/after string
    return name if name != '' else 'Unknown solution'      # to avoid getting confused by empty solution name