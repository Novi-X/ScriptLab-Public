# Filesystem Tools

## Overview
The **Filesystem Tools** collection contains scripts designed to help automate directory and file management tasks. These tools streamline tasks such as **generating directory structures** and **organizing files efficiently**.

## Included Scripts

### **1️⃣ Directory Structure Generator (`dir-structure.py`)**
📌 **Description:** Recursively scans a directory and generates an ASCII-formatted tree structure of all subdirectories and files.

✅ **Features:**
- Outputs a clean directory tree with ASCII formatting (`├──`, `└──`, `│`).
- Displays **📂 folder names** and **📄 file names** for easy readability.
- Marks **empty folders** with `⚠️ This folder is empty`.
- Ignores hidden files and system folders (e.g., `.git`, `__pycache__`).
- Saves the directory structure to a text file.

📌 **Usage:**
```bash
python dir-structure.py /path/to/directory
```

Example output:
```
📂 Music/
├── 📂 Rock/
│   ├── 📄 song1.mp3
│   ├── 📄 song2.mp3
└── 📂 Jazz/
    └── 📄 smooth_jazz.mp3
```

## Installation
To use these tools, **clone the repository** and install any necessary dependencies:
```bash
git clone https://github.com/yung-megafone/ScriptLab.git
cd ScriptLab/filesystem-tools
pip install -r requirements.txt  # If required
```

## Future Enhancements
🔹 Option to **exclude certain folders or file types**.
🔹 **JSON output support** for structured directory representation.
🔹 Add file **size display** next to filenames.

## License
This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.