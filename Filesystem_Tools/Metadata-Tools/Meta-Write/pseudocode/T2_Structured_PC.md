## **📌 T2 Structured Pseudocode**
> **Purpose:** A structured, step-by-step breakdown that closely follows the real Python logic.

### **📌 Main Function**
```plaintext
START
    Parse command-line arguments for "directory"
    
    IF directory does not exist:
        PRINT error message and EXIT

    CALL process_files_in_directory(directory)
END
```
📌 Function: process_files_in_directory(directory)
```plaintext
START
    Initialize "supported_extensions" = (".mp3", ".flac", ".wav")
    GET list of all files in "directory"

    IF no supported files found:
        PRINT "No valid music files found."
        EXIT

    FOR each file in "directory":
        CALL parse_filename(file) to extract metadata
        
        IF metadata is valid:
            CALL write_metadata(file, metadata)
        ELSE:
            PRINT "Skipping file (invalid format)"
END
```
📌 Function: parse_filename(filename)
```plaintext
START
    DEFINE "FILENAME_PATTERNS" → List of Regular Expressions for matching:
        - Track Number, Artist, Title, Featured Artists
        - Common separators: "-", "_", "feat.", "ft."

    FOR each pattern in FILENAME_PATTERNS:
        IF filename matches pattern:
            EXTRACT track number, artist, title, and featured artists
            RETURN structured metadata object

    ATTEMPT fallback split using basic separators

    RETURN None IF no valid metadata found
END
```
📌 Function: write_metadata(file_path, metadata)
```plaintext
START
    DETERMINE file extension (.mp3, .flac, .wav)

    IF MP3:
        OPEN file using "EasyID3"
    ELSE IF FLAC:
        OPEN file using "FLAC"
    ELSE IF WAV:
        OPEN file using "WAVE"
    ELSE:
        PRINT "Skipping unsupported file"
        EXIT

    SET metadata fields:
        - "tracknumber" = metadata["track_number"]
        - "artist" = metadata["artist"]
        - "title" = metadata["title"]
    
    IF "featured artists" exist:
        APPEND to "title" as "(feat. Featured Artist)"

    SAVE file metadata

    PRINT success message
END
```
📜 Summary

    Main function: Accepts a directory, verifies it, and calls processing functions.
    process_files_in_directory(): Loops through music files and calls metadata functions.
    parse_filename(): Extracts metadata using regex and fallback methods.
    write_metadata(): Writes metadata to the file using the correct tagging system.
    Handles multiple formats: MP3 (ID3), FLAC, WAV.