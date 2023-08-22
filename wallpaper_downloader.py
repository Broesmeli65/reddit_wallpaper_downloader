from bs4 import BeautifulSoup
import requests
import shutil
import sys
import logging
from datetime import datetime
import re
import ctypes

logging.basicConfig(level=logging.INFO)
logging.info("Fetching HTML page ...")

#find the first element in r/wallpaper
url_base = 'https://www.reddit.com'
url = 'https://www.reddit.com/r/wallpaper/top/?t=day'
try:
    html_page = requests.get(url)
    html_page.raise_for_status()
    logging.info("r/Wallpaper/top/day page fetched successfully!")
except requests.exceptions.RequestException as e:
    print(f"Error fetching HTML page: {e}")
    sys.exit(1)
soup = BeautifulSoup(html_page.content, 'html.parser')
element = soup.find('a', class_="absolute inset-0")

#find source link to post
source = element.attrs['href']

#create link to post
full_url = url_base + source

#find link to fullsize image
try:
    html_page2 = requests.get(full_url)
    html_page2.raise_for_status()
    logging.info("Post to image fetched successfully!")
except requests.exceptions.RequestException as t:
    print(f"Error fetching HTML page: {t}")
    sys.exit(1)
soup2 = BeautifulSoup(html_page2.content, 'html.parser')
element2 = soup2.find('div', class_="max-h-[100vw] h-full w-full object-contain overflow-hidden relative bg-black")
a_element = element2.find('a')
full_img = a_element.attrs['href']

#get title to create filename
try:    
    html_title = requests.get(full_url)
    html_title.raise_for_status()
    logging.info("Post to title fetched successfully!")
except requests.exceptions.RequestException as m:
    print(f"Error fetching HTML page: {m}")
    sys.exit(1)
soup3 = BeautifulSoup(html_page2.content, 'html.parser')
shreddit_title_tag = soup3.find('shreddit-title')  # Find <shreddit-title>-Tag

# Extract desired_part from the title
if shreddit_title_tag:
    title = shreddit_title_tag.get('title')
    title_without_brackets = re.sub(r'\[.*?\]', '', title)  # Remove [..] and image size from title
    split_title = title_without_brackets.split(':')
    
    if len(split_title) > 1:
        desired_part = split_title[0].strip()
    else:
        print("Can't find colon")
else:
    print("Can't find <shreddit-title>-Tag.")

# Download image to folder "images" with desired_part and date as the filename
r = requests.get(full_img, stream=True)

download_folder = r'X:\Photos\Wallpapers\Reddit' #configure for yourself

current_date = datetime.now().strftime('%Y-%m-%d')  # Format: YYYY-MM-DD

if r.status_code == 200:
    with open(f"{download_folder}\\{desired_part}_{current_date}.png", 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
        print(f"Downloading wallpaper: {desired_part} ({current_date})")
else:
    print("Error downloading")


SPI_SETDESKWALLPAPER = 20
WALLPAPER_PATH = f'{download_folder}\\{desired_part}_{current_date}.png'

try:
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)
    print("Wallpaper change successful!")
except: 
    print("Wallpaper change failed!")




