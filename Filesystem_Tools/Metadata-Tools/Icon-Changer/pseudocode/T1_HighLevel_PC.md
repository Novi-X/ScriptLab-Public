# **📜 T1_HighLevel_Pseudocode.md**
> **Purpose:** This provides an **easy-to-understand**, **plain-language** description of what the script does.

---

## **High-Level Pseudocode: Folder Icon Changer**

## **Overview**
This script applies a **custom folder icon** to all subdirectories inside a given **parent directory** on **Windows**.  
It ensures Windows properly recognizes the new icon by modifying the **desktop.ini** file and setting required folder attributes.

---

## **Steps:**

### **1. User Input**
   - Get **parent directory path** from the user.
   - Get **icon file path** (must be `.ico`).
   - Ask if the script should apply icons **recursively**.

### **2. Validate Inputs**
   - Ensure the **directory exists**.
   - Ensure the **icon file exists** and is a valid `.ico` file.
   - If any validation **fails**, display an **error message** and exit.

### **3. Gather Folders to Modify**
   - **If recursive mode is enabled** → Get **all** folders inside the directory.
   - **Otherwise** → Get **only** top-level folders.
   - Use a **progress bar** to track the number of folders being processed.

### **4. Apply Icon to Each Folder**
   - Copy the **`.ico` file** into the folder as **`folder.ico`**.
   - Create or modify the **`desktop.ini` file** inside the folder:
     - Set the **icon path** inside the `desktop.ini`.
     - Set **hidden & system attributes** to make Windows recognize the icon.
   - Mark the folder as **read-only** (required for custom icons).
   - If any folder **fails to update**, display an **error message**.

### **5. Refresh Folder Icons**
   - Run the **`ie4uinit.exe -show`** command to **update Windows icons instantly**.
   - Avoids restarting **Explorer.exe** for faster updates.

### **6. Generate Report**
   - Create an **"icon_change_report.txt"** file.
   - Log all **folders that were successfully updated**.
   - Display the **location of the report** when the script finishes.

### **7. Completion**
   - Print a **success message**.
   - End the script.

---

### **✅ Features & Benefits**
- **Automates the process** of applying icons to multiple folders.
- **Ensures Windows applies the icons correctly** by updating folder attributes.
- **Supports recursion** to modify all nested subfolders.
- **Prevents modifying directories outside the parent folder**.
- **Uses a progress bar** for better user experience.
- **Generates a log file** for tracking modified folders.