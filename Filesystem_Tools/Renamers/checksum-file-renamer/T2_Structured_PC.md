## **📜 T2_Structured_Pseudocode.md**  
> **Purpose:** A **structured, step-by-step** breakdown that closely follows the real Python implementation.  

---

# **Structured Pseudocode: Checksum File Renamer**  

## **Main Function: `main()`**  
```plaintext
START  
    IF user did not provide a directory path:  
        PRINT "Usage: python checksum-rename.py <directory_path>"  
        EXIT  

    SET target_directory ← user input (1st argument)  

    IF target_directory does not exist:  
        PRINT "Error: Invalid directory path."  
        EXIT  

    PROMPT user for checksum length (default: 12)  
    IF user input is invalid:  
        SET digest_length ← 12  

    CALL process_files_in_directory(target_directory, digest_length)  
END  
```

---

## **Function: `process_files_in_directory(directory_path, digest_length)`**  
```plaintext
START  
    INITIALIZE file_list ← empty list  

    FOR each file in directory (including subdirectories):  
        APPEND full file path to file_list  

    IF file_list is empty:  
        PRINT "No files found in the specified directory."  
        RETURN  

    DISPLAY progress bar  
    EXECUTE rename_file_to_checksum() for each file using multithreading  
    CLOSE progress bar  
END  
```

---

## **Function: `rename_file_to_checksum(file_path, digest_length)`**  
```plaintext
START  
    EXTRACT file extension from file_path  

    COMPUTE SHAKE-128 checksum for file (CALL calculate_shake128_checksum())  
    SET new_filename ← "{CHECKSUM}.{EXTENSION}"  
    SET new_file_path ← directory + new_filename  

    IF file name is already correct:  
        RETURN  (Skip renaming)  

    IF new_file_path already exists:  
        DELETE original file (Prevent duplicates)  
    ELSE:  
        RENAME file to new_file_path  
END  
```

---

## **Function: `calculate_shake128_checksum(file_path, digest_length)`**  
```plaintext
START  
    INITIALIZE SHAKE-128 hasher  

    OPEN file in binary mode  
    READ file in chunks (128 KB each)  
    UPDATE hasher with each chunk  

    RETURN SHAKE-128 checksum (hexadecimal, truncated to digest_length bytes)  
END  
```

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