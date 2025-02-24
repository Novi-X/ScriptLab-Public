# **Media Download Tools**

## **📌 Overview**
The **Media Download Tools** category contains Python scripts designed for **automated media downloading**, including YouTube videos, movies, TV shows, books, and other digital content. These tools ensure **structured organization**, **efficient automation**, and **minimal redundancy** when managing downloaded media.

Each program includes:
- **A structured Python script** for automated media downloads.
- **High-level & structured pseudocode** (`T1_HighLevel_PC.md` & `T2_Structured_PC.md`).
- **Clear usage instructions** in its README.
- **Customization options** for output directories and formats.

---

## **📂 Programs Included**

### **1️⃣ ytfetch**
📌 **A script that fetches and downloads new YouTube videos without redownloading old ones.**  
- **Tracks previously downloaded videos** to prevent duplicates.  
- **Uses a text-based configuration (`channels.txt`)** for managing subscriptions.  
- **Supports automation** via cron jobs or Task Scheduler.  
- **Saves videos in custom folders** based on creator names.  

📍 **Usage:**
```bash
python ytfetch.py
```
📍 **Automate the script (Linux/macOS):**
```bash
0 * * * * /usr/bin/python3 /path/to/ytfetch.py
```
📍 **Automate the script (Windows Task Scheduler):**
- Set up a task to run `python /path/to/ytfetch.py` periodically.

---

## **📜 Pseudocode Documentation**
Each program includes **two pseudocode files** to describe its logic clearly:

✅ **T1 High-Level Pseudocode (`T1_HighLevel_PC.md`)** → Broad overview of the program’s functionality.  
✅ **T2 Structured Pseudocode (`T2_Structured_PC.md`)** → Detailed step-by-step logic aligning with the Python implementation.  

---

## **🛠 Installation**
To install dependencies, run:
```bash
pip install -r ../../requirements.txt
```

---

## **📜 License**
This project is intended for **personal use only**. Please comply with content providers’ terms of service.