# **ytfetch - YouTube Download Automation**

## **📌 Overview**
**ytfetch** is a Python script designed to automate **YouTube video downloads**, ensuring only **new content** is fetched without redownloading previously saved videos. It supports **custom folder organization**, **efficient tracking**, and **automated execution** via scheduling tools.

This script is structured to be **easily configurable** and **scalable**, allowing users to:
- **Specify custom folder names** for different creators.
- **Prevent duplicate downloads** using an archive file.
- **Automate the fetching process** via cron jobs or Task Scheduler.

---

## **⚙️ Features**
✅ **Automatically detects and downloads new videos** from specified channels.  
✅ **Customizable output folders** for better organization.  
✅ **Download tracking** using `downloaded_videos.txt` to avoid re-fetching old content.  
✅ **Supports batch processing** via a `channels.txt` configuration file.  
✅ **Optimized for scheduled execution** to keep media collections up to date.  

---

## **🚀 Usage**
### **1️⃣ Running the script manually**
To fetch new videos:
```bash
python ytfetch.py
```

### **2️⃣ Automate execution (Linux/macOS)**
To schedule it using cron (`crontab -e`):
```bash
0 * * * * /usr/bin/python3 /path/to/ytfetch.py
```

### **3️⃣ Automate execution (Windows Task Scheduler)**
- Open **Task Scheduler**.
- Create a new task to run:
  ```
  python C:\path\to\ytfetch.py
  ```
- Set it to run at regular intervals.

---

## **📂 What This Script Does**
### **1️⃣ Fetch & Download New Videos**
📌 **Reads `channels.txt` to retrieve a list of channels and their assigned folders.**  
- Extracts **new uploads only** to prevent duplicates.  
- Downloads files into the assigned **custom directory**.  
- Stores filenames in `downloaded_videos.txt` to track progress.  

### **2️⃣ Manage Custom Folders**
📌 **Each channel's videos are stored in a user-specified directory.**  
- The `channels.txt` format follows:
  ```
  Folder Name | Channel URL
  ```
  Example:
  ```
  Midwest Safety | https://www.youtube.com/@MidwestSafety
  Engineering Explained | https://www.youtube.com/@EngineeringExplained
  ```

### **3️⃣ Download Tracking (`downloaded_videos.txt`)**
📌 **Ensures only new videos are fetched.**  
- Each downloaded video is logged.
- The script skips any previously downloaded content.

---

## **🛠 Installation**
Ensure you have `yt-dlp` installed:
```bash
pip install yt-dlp
```

---

## **📜 License**
This script is intended for **personal use only**. Please comply with YouTube’s [Terms of Service](https://www.youtube.com/t/terms).

---

## **📌 Why Use ytfetch?**
🔹 **Prevents duplicate downloads** with efficient tracking.  
🔹 **Organizes videos into structured folders** for easy access.  
🔹 **Designed for automation**, requiring minimal manual effort.  
🔹 **Lightweight and efficient**, using `yt-dlp` as the backend.  

This script is ideal for **building a personal media archive without unnecessary duplication**. 🚀

