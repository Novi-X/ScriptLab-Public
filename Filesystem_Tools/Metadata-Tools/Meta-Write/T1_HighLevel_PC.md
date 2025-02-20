## **📌 T1 High-Level Pseudocode**
> **Purpose:** A broad, easy-to-understand overview of what the script does.

### **Overview**
This script scans a folder for **MP3, FLAC, and WAV files**, extracts **artist, track number, title, and featured artists** from their filenames, and writes this data into the file’s metadata.

### **Steps**
1. **User Input**
   - Accept **directory path** from the user.
   - Validate that the directory exists.
   
2. **Process Files**
   - Scan the **directory** for supported **music files**.
   - **For each file**:
     - Extract metadata from the filename.
     - If metadata is **valid**, write it to the file.
     - If metadata **cannot be extracted**, **skip** the file.
   
3. **Metadata Extraction**
   - Use **regular expressions** to match filename patterns.
   - Identify **track number, artist, title, and featured artists**.
   - Handle **different separators** (`-`, `_`, `feat.`, `ft.`).
   - If the format is **unrecognized**, attempt a **fallback split**.

4. **Metadata Writing**
   - Open the file using **Mutagen**.
   - Write extracted metadata into **ID3 (MP3), FLAC, or WAV tags**.
   - Save and confirm success.

5. **Completion**
   - Print a **summary report** of modified files.
   - Notify the user of any **errors or skipped files**.