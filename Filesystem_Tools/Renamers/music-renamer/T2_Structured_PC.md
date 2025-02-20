## **📜 T2_Structured_Pseudocode.md**  
> **Purpose:** A **structured, step-by-step** breakdown that closely resembles the real Python logic.

---

# **Structured Pseudocode: Music File Renamer**  

## **Main Function: `main()`**  
```plaintext
START
    PARSE command-line arguments:
        - Get "directory path" from user
        - Check if "--copy" flag is provided

    IF directory does not exist:
        PRINT "Error: Invalid directory path."
        EXIT

    IF "--copy" flag is enabled:
        CREATE "Renamed Music" directory

    CALL "gather_all_music_files(directory)"

    IF no music files found:
        PRINT "No supported music files found."
        EXIT

    FOR each file in the music file list:
        CALL "extract_metadata_from_file(file)"
        IF metadata extraction fails:
            PRINT "Skipping file due to missing metadata."
            CONTINUE

        FORMAT new filename using metadata
        CALL "rename_music_files(file, new_filename, output_directory, copy_files)"

    PRINT "All files processed successfully."
END
```

---

## **Function: `gather_all_music_files(directory)`**  
```plaintext
START
    DEFINE list of supported file extensions (".mp3", ".flac", ".wav")
    INITIALIZE empty list "music_files"

    FOR each file in the directory (including subdirectories):
        IF file extension is in supported extensions:
            ADD file path to "music_files"

    RETURN "music_files" list
END
```

---

## **Function: `extract_metadata_from_file(file_path)`**  
```plaintext
START
    TRY:
        OPEN file with "mutagen" for metadata extraction
        IF file format is unsupported:
            PRINT "Skipping unsupported file."
            RETURN None

        EXTRACT:
            - Track Number (default: "00" if missing)
            - Title (default: "Unknown Title" if missing)
            - Artist (default: "Unknown Artist" if missing)
            - Featured Artists (if present in the title)

        RETURN metadata dictionary:
            {
                "track_number": track_number,
                "title": title,
                "artist": artist,
                "featured_artists": featured_artists
            }

    CATCH exceptions:
        PRINT "Skipping file due to metadata error."
        RETURN None
END
```

---

## **Function: `format_filename(metadata, file_extension)`**  
```plaintext
START
    FORMAT filename as:
        "{track_number} - {artist} - {title} (feat. {featured_artists}){file_extension}"

    IF no featured artist:
        REMOVE "(feat. ...)" from filename

    RETURN sanitized filename
END
```

---

## **Function: `sanitize_filename(filename)`**  
```plaintext
START
    REMOVE invalid characters: `< > : " / \ | ? *`
    RETURN cleaned filename
END
```

---

## **Function: `rename_music_files(file_path, new_filename, output_directory, copy_files)`**  
```plaintext
START
    SET "new_file_path" to:
        - If "--copy" is enabled → Place in "Renamed Music" directory
        - Else → Rename in the same directory

    CHECK IF "new_file_path" already exists:
        - IF exists, append (1), (2), etc., to avoid overwriting

    IF "--copy" is enabled:
        COPY original file to "new_file_path"
    ELSE:
        RENAME original file to "new_file_path"

    PRINT "File renamed successfully."
END
```

---

## **Final Execution Flow**
```plaintext
START PROGRAM

CALL "main()"

END PROGRAM
```