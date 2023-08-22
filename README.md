# Reddit Wallpaper Downloader

This script allows you to automatically download and set Reddit wallpapers as your desktop background.

## Installation

1. Make sure you have Python installed (version 3.x recommended).

2. Clone this repository:
git clone https://github.com/Broesmeli65/reddit-wallpaper-downloader.git

3. Install the required packages:
pip install -r requirements.txt

## Usage

1. Open the script `wallpaper_downloader.py`.

2. Configure the `download_folder` variable to the directory where you want to save the downloaded wallpapers.

3. Run the script:
python wallpaper_downloader.py



The script will fetch the top daily wallpaper from the r/wallpaper subreddit on Reddit, download it, and set it as your desktop wallpaper.

## Configuration

- The `download_folder` variable should be configured to the directory where you want to save the downloaded wallpapers.
- The script automatically adds the date to the filename for each downloaded wallpaper.
- The wallpaper change is attempted using the Windows API. If it fails, an error message will be shown.
- Configure the automation task in your Windows to automatically run the script at startup.

## Disclaimer

This script uses web scraping to download images from Reddit. Make sure to respect Reddit's terms of use and the rules of the subreddits you are downloading images from.



