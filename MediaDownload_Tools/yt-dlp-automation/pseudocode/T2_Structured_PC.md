## **📜 T2_Structured_Pseudocode.md**
**Purpose:** A **structured, step-by-step** breakdown that closely resembles the real Python logic.

# **Structured Pseudocode: ytfetch**

## **Main Function**
```plaintext
START PROGRAM

IMPORT necessary libraries (os, subprocess, yt-dlp)

DEFINE script metadata (Author, Version, License)

DEFINE CONSTANTS:
    - CHANNELS_FILE = "channels.txt"
    - DOWNLOAD_ARCHIVE = "downloaded_videos.txt"
    - BASE_DOWNLOAD_PATH = "./Downloads"
    - YT_DLP_COMMAND = ["yt-dlp", "--download-archive", DOWNLOAD_ARCHIVE, "-o", "%(title)s.%(ext)s"]

FUNCTION read_channels():
    PRINT "Reading channels from file..."
    IF CHANNELS_FILE does not exist:
        PRINT "Error: channels.txt not found."
        RETURN empty list
    END IF

    OPEN CHANNELS_FILE and read lines
    PARSE each line into (folder_name, channel_url)
    RETURN list of (folder_name, channel_url) pairs
END FUNCTION

FUNCTION check_download_archive():
    PRINT "Checking previously downloaded videos..."
    IF DOWNLOAD_ARCHIVE does not exist:
        CREATE empty archive file
    END IF

    OPEN DOWNLOAD_ARCHIVE and read video IDs
    RETURN list of downloaded video IDs
END FUNCTION

FUNCTION download_new_videos(channel_list, downloaded_videos):
    FOR each (folder_name, channel_url) in channel_list:
        PRINT "Processing channel:", channel_url

        SET output_path = BASE_DOWNLOAD_PATH + "/" + folder_name
        CREATE directory if not exists

        BUILD yt-dlp command with:
            - Output path
            - Archive file for tracking
            - Channel URL
        
        EXECUTE yt-dlp command
        CAPTURE output and check for new video downloads
        UPDATE downloaded_videos.txt with new entries
    END FOR
END FUNCTION

FUNCTION main():
    PRINT "Starting ytfetch..."
    
    CALL read_channels() -> store in channel_list
    CALL check_download_archive() -> store in downloaded_videos
    
    IF channel_list is empty:
        PRINT "No channels found. Exiting."
        RETURN
    END IF
    
    CALL download_new_videos(channel_list, downloaded_videos)
    
    PRINT "ytfetch completed successfully."
END FUNCTION

IF script is executed directly:
    CALL main()
END PROGRAM