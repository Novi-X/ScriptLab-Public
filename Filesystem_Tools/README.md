# Filesystem Tools

## Overview
The **Filesystem Tools** collection includes utilities designed to help manage files, directories, and system organization. These scripts automate repetitive tasks such as generating directory structures, renaming files based on metadata, and modifying folder icons.

## 📂 Tools Included

### **1️⃣ Directory Structure Generator**
📌 **Generates an ASCII directory tree of a folder and its subdirectories.**
- Displays file sizes and allows JSON output.
- Supports excluding specific folders or file types.
- Includes a progress bar for better tracking.

📍 **Usage:**
```bash
python dir-structure.py /path/to/folder --json
```

### **2️⃣ Icon Changer**
📌 **Assigns a custom folder icon to all subdirectories.**
- Supports Windows (`.ico` files).
- Includes recursive mode to apply icons to nested subdirectories.

📍 **Usage:**
```bash
python icon-changer.py /path/to/folders /path/to/icon.ico --recursive
```

### **3️⃣ Checksum File Renamer**
📌 **Renames files using their SHAKE-128 checksum.**
- Ensures unique filenames and prevents duplicates.
- Uses multithreading to speed up renaming.
- Includes a progress bar for tracking.

📍 **Usage:**
```bash
python checksum-rename.py /path/to/files
```

### **4️⃣ Music File Renamer**
📌 **Renames music files based on their metadata (ID3, FLAC, WAV tags).**
- Standardizes filenames as `01 - Artist - Song Title.mp3`.
- Supports recursive processing of subdirectories.
- Prevents overwriting and allows moving renamed files.

📍 **Usage:**
```bash
python music-renamer.py /path/to/music --copy
```

## 🛠 Installation
To install dependencies, run:
```bash
pip install -r ../../requirements.txt
```

## 📜 License
This project is licensed under the **MIT License**. See [LICENSE](../../LICENSE) for details.
