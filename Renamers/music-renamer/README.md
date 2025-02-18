# Music File Renamer

## Overview
Music File Renamer is a Python script that automates the process of renaming music files using their embedded metadata. It retrieves track number, artist, song title, and featured artists (if any) to format the filename in a clean and organized manner.

## Features
- Extracts metadata from **MP3, FLAC, and WAV** files.
- Renames files in the format:
  ```
  01 - Artist - Song Title (feat. Featured Artist).mp3
  ```
- **By default, renames files in place.**
- **Optional:** Use `--copy` flag to copy renamed files to a separate folder instead of renaming them in place.
- Prevents overwriting by automatically appending `(1)`, `(2)`, etc., if duplicate filenames exist.
- Handles special characters to avoid errors.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yung-megafone/ScriptLab.git
   cd ScriptLab
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script with the directory containing music files:
```bash
python music_renamer.py /path/to/music
```

### **Optional: Copy Files Instead of Renaming in Place**
If you want to keep the original files and save renamed versions in a **"Renamed Music"** folder, use the `--copy` flag:
```bash
python music_renamer.py /path/to/music --copy
```

## Example Output
```
Renamed: OldSong.mp3 → 01 - Artist - Song Title.mp3
Copied: OldSong.mp3 → Renamed Music/01 - Artist - Song Title.mp3
```

## Notes
- If metadata is missing, defaults will be used (e.g., "Unknown Artist").
- If "feat." is detected in the title, featured artists will be extracted.
- File extensions are preserved.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
