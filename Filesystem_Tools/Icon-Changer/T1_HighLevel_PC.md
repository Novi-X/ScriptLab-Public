## **📜 T1_HighLevel_Pseudocode.md**
> **Purpose:** This provides an easy-to-understand, **plain-language** description of what the script does.

```markdown
# High-Level Pseudocode: Directory Structure Generator

## Overview
This script scans a given directory **recursively** and generates an ASCII-based **directory tree** representation of all folders and files.

## Steps:
1. **User Input**:
   - Get the **directory path** from the user.
   - Allow optional **exclusions** (folders or file types).
   - Allow an option to output the structure as **JSON**.
  
2. **Process Directory**:
   - **Scan the folder recursively**:
     - **Identify all subdirectories**.
     - **Identify all files** and their sizes.
     - **Sort everything alphabetically** for consistent output.
   - **Skip hidden files and excluded folders**.

3. **Generate Output**:
   - **Format directory tree with ASCII**.
   - **Use colors in terminal output** (blue for folders, green for files).
   - **Show file sizes** (Convert MB → GB if needed).
   - **Write everything to a text file**.
   - **Optionally, create a JSON version**.

4. **Display Progress & Completion**:
   - Show **progress bar** while scanning.
   - Print **success messages** with the location of saved reports.

```