# Music Renamer

## Overview
The **Music Renamer** is a Python script that renames music files using their **metadata (ID3, FLAC, WAV tags)**. It ensures **consistent and organized filenames**, making it easier to manage large music collections.

## Features
✅ **Automatically extracts metadata** (Title, Artist, Track Number).  
✅ **Formats filenames as `01 - Artist - Song Title.mp3`**.  
✅ **Handles featured artists** by appending them to the title.  
✅ **Supports multiple file formats** (MP3, FLAC, WAV).  
✅ **Option to move renamed files to a new directory**.  
✅ **Batch processing with recursive support**.  
✅ **Uses a progress bar (`tqdm`) for real-time tracking**.  

## Installation
To install dependencies, run:
```bash
pip install -r requirements.txt
```

## Usage
Run the script with the directory containing music files:
```bash
python music-renamer.py /path/to/music
```

### **Example Output**
#### **Before Running the Script:**
```
📂 Music/
├── track1.mp3
├── song2.flac
└── audiofile.wav
```

#### **After Running the Script:**
```
📂 Music/
├── 01 - Artist - Track Name.mp3
├── 02 - Artist - Song Title.flac
└── 03 - Artist - Audio File.wav
```

## Advanced Options
### **Move Renamed Files to a New Directory**
Instead of renaming files in place, move them to a new folder:
```bash
python music-renamer.py /path/to/music --copy
```

### **Recursive Processing**
Process all files inside subdirectories:
```bash
python music-renamer.py /path/to/music --recursive
```

## License
This project is licensed under the **MIT License**. See [LICENSE](../LICENSE) for details.

## Future Improvements
🔹 **Add album sorting for better organization**.  
🔹 **Support for additional audio formats** (e.g., AAC, OGG).  
🔹 **Auto-download missing metadata from online sources**.  
🔹 **Option to rename files using a custom naming scheme**.  

For feature requests or contributions, feel free to open an **issue** or **pull request**! 🚀