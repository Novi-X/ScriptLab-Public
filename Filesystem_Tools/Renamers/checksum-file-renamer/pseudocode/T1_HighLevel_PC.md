## **📜 T1_HighLevel_Pseudocode.md**  
> **Purpose:** This provides an **easy-to-understand**, **plain-language** description of what the script does.  

---

# **High-Level Pseudocode: Checksum File Renamer**  

## **Overview**  
This script scans a specified directory, calculates **SHAKE-128 checksums** for all files, and renames them based on their **computed checksum**.  
- If a file with the same checksum **already exists**, the duplicate is deleted.  
- It **preserves file extensions** while renaming.  
- Uses **multithreading** to improve processing speed.  
- Allows users to specify **custom checksum length** (default: 12 bytes).  

---

## **Steps:**  

### **1️⃣ User Input & Validation**  
- User provides:  
  - **Target directory path**  
  - **Optional checksum length (default: 12 bytes)**  
- If the directory **does not exist**, display an **error message** and exit.  

---

### **2️⃣ Scan & Collect Files**  
- **Iterate through all files** in the given directory.  
- **Store file paths** in a list for processing.  
- If **no files are found**, print a message and exit.  

---

### **3️⃣ Compute SHAKE-128 Checksum & Rename Files**  
- For **each file in the directory**:  
  - **Read file contents** in chunks (128 KB buffer) for efficiency.  
  - **Generate SHAKE-128 checksum** (length specified by user).  
  - **Preserve the original file extension**.  
  - **Rename file to:**  
    ```
    {SHAKE-128_CHECKSUM}.{original_extension}
    ```
  - If a file **with the same checksum name already exists**, delete the **duplicate file**.  

---

### **4️⃣ Display Progress & Completion**  
- **Show progress bar** while renaming files.  
- **Print success message** when renaming is complete.  

---

## **Final Execution Flow**  
```plaintext
START PROGRAM  
    PROMPT user for "directory path"  
    PROMPT user for "checksum length" (default: 12)  

    IF directory does not exist:  
        PRINT error message and EXIT  

    SCAN directory for files  
    IF no files found:  
        PRINT error message and EXIT  

    FOR each file:  
        COMPUTE SHAKE-128 checksum  
        CHECK if file with same checksum name exists  
            IF yes: DELETE duplicate file  
        RENAME file to "{CHECKSUM}.{EXTENSION}"  

    PRINT "All files processed successfully."  
END PROGRAM  
```  