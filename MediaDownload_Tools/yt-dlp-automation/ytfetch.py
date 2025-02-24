"""
ytfetch - YouTube Download Automation
-----------------------------
Author: yung-megafone
Date: 2025-02-24
License: MIT License

Description:
ytfetch is a Python script that automates YouTube video downloads, ensuring only new content 
is fetched without redownloading previously saved videos. It supports custom folder organization, 
efficient tracking, and automated execution via scheduling tools.

Features:
- Fetches only new videos, preventing duplicate downloads.
- Uses a text-based configuration file (`channels.txt`) for batch processing.
- Saves videos in user-specified folders based on creator names.
- Tracks downloaded content using `downloaded_videos.txt`.
- Supports scheduled execution via cron jobs or Task Scheduler.
- Optimized for automation, requiring minimal manual intervention.

Usage:
    python ytfetch.py

Example:
    python ytfetch.py

Automating the Script:
    - Linux/macOS (via crontab):
        0 * * * * /usr/bin/python3 /path/to/ytfetch.py
    - Windows (Task Scheduler):
        python C:\path\to\ytfetch.py

Configuration:
    The script reads `channels.txt` formatted as:
        Folder Name | Channel URL

Example:
    уυηg-мєgαƒӨПΣ | https://www.youtube.com/@yung-megafone
    Engineering Explained | https://www.youtube.com/@EngineeringExplained
"""
import os           # File and dir ops
import yt_dlp       # To download yt content
import ffmpeg       # For video and audio processing
import subprocess   # To execute python commands (python yt-dlp)
import sys          # For CLI argument handling
import argparse     # For CLI argument flags (ytfetch.py --help)
import shutil       # For file mgmt
import time         # For tracking performance and exec time

CHANNELS_FILE = "channels.txt"  # Define the file containing folder | link pairs
DOWNLOAD_LOG = "downloaded_videos.txt"  # Log file to track downloaded filenames

def load_download_log():
    """Loads previously downloaded filenames from the log file."""
    if not os.path.exists(DOWNLOAD_LOG):
        return set()  # Return an empty set if the file doesn't exist
    with open(DOWNLOAD_LOG, "r", encoding="utf-8") as file:
        return set(line.strip() for line in file if line.strip())

def update_download_log(filename):
    """Appends a new filename to the log file."""
    with open(DOWNLOAD_LOG, "a", encoding="utf-8") as file:
        file.write(filename + "\n")

def download_video(storage_path, url, downloaded_files):
    """Downloads a YouTube video to the specified folder if it hasn't been downloaded before."""
    
    if not url.strip():
        print("Error: URL is empty, skipping...")
        return  

    # Ensure the directory exists
    os.makedirs(storage_path, exist_ok=True)

    # Construct yt-dlp command with metadata output
    command = [
        "python", "-m", "yt_dlp", 
        "--print", "%(title)s.%(ext)s",  # Get expected filename before downloading
        "-o", "%(title)s.%(ext)s",
        "-P", storage_path, url
    ]

    try:
        # Get the expected filename before downloading
        filename = subprocess.check_output(command, universal_newlines=True).strip()
        file_path = os.path.join(storage_path, filename)

        # Skip if already downloaded
        if filename in downloaded_files or os.path.exists(file_path):
            print(f"Skipping {filename} (Already downloaded)")
            return

        # Actual download command
        command = [
            "python", "-m", "yt_dlp",
            "-o", "%(title)s.%(ext)s",
            "-P", storage_path, url
        ]

        start_time = time.time()
        print(f"Downloading {filename} to {storage_path}")
        subprocess.run(command, check=True)
        
        # Log successful download
        update_download_log(filename)
        print(f"Download completed: {filename}")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading {url}: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    end_time = time.time()
    execution_time = end_time - start_time  
    print(f"Execution Time: {execution_time:.2f} seconds\n")

def batch_download():
    """Reads the file and downloads videos to their respective folders while preventing duplicates."""
    if not os.path.exists(CHANNELS_FILE):
        print(f"ERROR: {CHANNELS_FILE} not found")
        return

    downloaded_files = load_download_log()  # Load previously downloaded filenames

    with open(CHANNELS_FILE, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]

    for line in lines:
        try:
            storage_path, url = map(str.strip, line.split("|", 1))  # Split folder and link
            storage_path = storage_path.replace("\\", "/")  # Normalize paths
            download_video(storage_path, url, downloaded_files)
        except ValueError:
            print(f"Invalid format in {CHANNELS_FILE}: {line}")

if __name__ == "__main__":
    batch_download()