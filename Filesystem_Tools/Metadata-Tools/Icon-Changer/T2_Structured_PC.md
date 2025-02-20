# **📜 T2_Structured_Pseudocode.md**
> **Purpose:** A **structured, step-by-step** breakdown that closely resembles the real Python logic.

---

## **📌 Main Function**
```plaintext
START
    Parse command-line arguments (parent_directory, icon_path, --recursive)

    IF parent_directory is not a valid directory:
        PRINT "Error: Invalid directory"
        EXIT

    IF icon_path is not a valid .ico file:
        PRINT "Error: Icon file not found or invalid format"
        EXIT

    CALL apply_folder_icons(parent_directory, icon_path, recursive_flag)

    PRINT "✔ Folder icons successfully applied!"
END
```
📌 Function: apply_folder_icons(parent_directory, icon_path, recursive_flag)
```plaintext
START
    Initialize empty list "modified_folders"

    IF recursive_flag is TRUE:
        GET all subfolders inside parent_directory
    ELSE:
        GET only top-level folders

    SHOW progress bar for folder processing

    FOR each folder in the folder list:
        IF apply_icon_windows(folder, icon_path) is SUCCESSFUL:
            ADD folder to "modified_folders"

    CALL refresh_icons()  # Update Windows shell icons

    CALL generate_report(modified_folders)  # Create a log file
END
```
📌 Function: apply_icon_windows(folder_path, icon_path)
```plaintext
START
    DEFINE desktop_ini_path = folder_path + "desktop.ini"
    DEFINE copied_icon_path = folder_path + "folder.ico"

    TRY:
        COPY icon_path to copied_icon_path

        IF desktop.ini already exists:
            REMOVE hidden/system attributes from desktop.ini

        CREATE or OVERWRITE "desktop.ini":
            WRITE "[.ShellClassInfo]" section
            SET "IconResource=folder.ico,0"

        APPLY Windows folder attributes:
            SET desktop.ini as "hidden + system"
            SET folder as "read-only"

        RETURN SUCCESS

    EXCEPTIONS:
        PRINT "Error applying icon to folder"
        RETURN FAILURE
END
```
📌 Function: refresh_icons()
```plaintext
START
    PRINT "Refreshing folder icons..."
    RUN Windows command "ie4uinit.exe -show" to refresh shell icons
END
```
📌 Function: generate_report(modified_folders)
```plaintext
START
    DEFINE report_file = "icon_change_report.txt"

    CREATE report_file:
        WRITE "📂 Folder Icon Change Report"
        WRITE total number of modified folders
        WRITE separator line

        FOR each folder in modified_folders:
            WRITE "✔ Folder path"

    PRINT "✔ Icon change report saved!"
END
```
🔹 Summary

    Main function validates user input and calls core functions.
    apply_folder_icons() processes all folders and updates icons.
    apply_icon_windows() copies .ico and modifies desktop.ini settings.
    refresh_icons() ensures Windows recognizes the new icons without restarting Explorer.
    generate_report() logs all modified folders in a report file.