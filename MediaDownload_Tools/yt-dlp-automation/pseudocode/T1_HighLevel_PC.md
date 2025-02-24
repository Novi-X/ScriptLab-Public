## **📜 T1_HighLevel_Pseudocode.md**

> **Purpose:** This provides an **easy-to-understand**, **plain-language** description of what `ytfetch` does.

---

# **High-Level Pseudocode: ytfetch**

## **Overview**
`ytfetch` is a script designed to **automate YouTube video downloads**, ensuring only **new content** is fetched without redownloading previously saved videos. It maintains an organized directory structure, tracks downloaded files, and supports scheduled execution for hands-free automation.

---

## **Steps:**

### **1️⃣ Read User Configuration**
- Open and read the `channels.txt` file.
- For each line in `channels.txt`:
  - Extract the **folder name** and **channel URL**.
  - Validate the format to ensure proper structure.

---

### **2️⃣ Check for Previously Downloaded Videos**
- Open and read the `downloaded_videos.txt` file (if it exists).
- Store previously downloaded video IDs to avoid redownloading.

---

### **3️⃣ Fetch and Process New Videos**
- For each channel in the list:
  - Construct the **yt-dlp** command with:
    - Custom output folder (`-P <folder_name>`).
    - Archive tracking (`--download-archive downloaded_videos.txt`).
    - Filename format (`-o "%(title)s.%(ext)s"`).
  - Execute the **yt-dlp** command to fetch new videos.
  - If new videos are downloaded, log their IDs to `downloaded_videos.txt`.

---

### **4️⃣ Handle Execution Output**
- Display **status messages** for each processed channel.
- Show **progress logs** with timestamps.
- If any errors occur:
  - Print an error message with details.
  - Skip the affected channel and proceed with the next.

---

### **5️⃣ Finalize Execution**
- Confirm script completion.
- If verbose mode is enabled, display summary statistics:
  - Number of new videos downloaded.
  - Total execution time.
- Exit gracefully.

