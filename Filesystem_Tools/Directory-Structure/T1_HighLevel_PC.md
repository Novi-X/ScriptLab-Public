## **📜 T1_HighLevel_Pseudocode.md**
> **Purpose:** This provides an easy-to-understand, **plain-language** description of what the script does.

---

## **Main Function**
```plaintext
START
    Prompt user for "directory path" to scan
    Prompt user for "excluded folders or file types" (optional)
    Prompt user for "--json" flag (optional)

    IF directory does not exist:
        PRINT error message and exit

    Initialize "progress bar" to track scanned folders
    CALL get_directory_tree(directory_path, output_file, exclude_list, json_output)

    PRINT "✔ Directory structure saved!"
END
```

---

## **Function: `get_directory_tree(directory, output_file, exclude, json_output)`**
```plaintext
START
    Start execution timer
    Get current date/time for metadata
    Convert "exclude list" into a set for faster lookup

    DEFINE function generate_tree(folder, prefix, use_colors)
        Get all files & folders in "folder"
        Sort entries alphabetically
        REMOVE hidden files and those in "exclude list"

        Separate "folder entries" and "file entries"
        IF folder is empty:
            RETURN "⚠️ This folder is empty"

        FOR each "sub-folder":
            Append folder name to tree
            Recursively CALL generate_tree(sub-folder)

        FOR each "file":
            GET file size in MB
            IF size > 1024MB → Convert to GB
            Append file entry with size to tree

        RETURN directory tree structure
    END

    Initialize progress bar with total number of folders
    CALL generate_tree(directory_path) to get "colored output"
    CALL generate_tree(directory_path) to get "plain text output"
    Close progress bar

    Write metadata and tree structure to "output file"
    PRINT success message

    IF "json_output" is True:
        Convert directory tree to JSON format
        Save JSON output file
        PRINT JSON success message
END
```