## **📜 T1_HighLevel_Pseudocode.md**

> **Purpose:** This provides an **easy-to-understand**, **plain-language** description of what the script does.

---

# **High-Level Pseudocode: Music File Renamer**

## **Overview**
This script scans a given directory for **music files (MP3, FLAC, WAV)**, extracts **metadata** (Track Number, Artist, Title, and Featured Artists), and **renames** the files accordingly.

It ensures:
- Consistent **file naming conventions**.
- Prevention of **duplicate filenames**.
- **Recursive** scanning of subdirectories (if enabled).
- Option to **copy renamed files** into a separate folder instead of renaming in place.

---

## **Steps:**

### **1️⃣ User Input**
- Accept **directory path** where music files are stored.
- Allow the **--copy flag** to move renamed files to a separate folder.
- Validate:
  - If the **directory exists**, continue.
  - If the **directory is invalid**, show an error and exit.

---

### **2️⃣ Scan Directory**
- **Find all music files** in the directory (including subdirectories).
- **Identify supported file formats** (`.mp3`, `.flac`, `.wav`).
- Display a **progress bar** while scanning.

---

### **3️⃣ Extract Metadata**
- **Read file metadata** using `mutagen`:
  - Get **Track Number**, **Title**, and **Artist**.
  - Detect **Featured Artists** (if any).
- If metadata is missing, assign **default placeholders**.

---

### **4️⃣ Format New Filenames**
- Construct **new filenames** in this format:  
  ```
  01 - Artist - Song Title (feat. Featured Artist).mp3
  ```
- Ensure filenames **do not contain invalid characters**.

---

### **5️⃣ Rename or Copy Files**
- **Check if filename already exists**:
  - If a file with the same name exists, **append (1), (2), etc.** to avoid overwriting.
- If `--copy` is enabled:
  - **Copy** the renamed file to a `Renamed Music` folder.
- Otherwise:
  - **Rename the file in place**.

---

### **6️⃣ Display Progress & Completion**
- **Update progress bar** for each file processed.
- Show **confirmation messages** for:
  - Successfully renamed files.
  - Skipped files (if format is unsupported or metadata is missing).
- Print **final summary** and exit.