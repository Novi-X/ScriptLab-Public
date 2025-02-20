import os
import re
import argparse
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from mutagen.wave import WAVE
from tqdm import tqdm

# Define flexible regex patterns
FILENAME_PATTERNS = [
    re.compile(r"(\d{1,2})\s*[-_]\s*(.*?)\s*[-_]\s*(.*?)\s*\(?feat\.?\s*(.*?)\)?(\.\w+)$", re.IGNORECASE),
    re.compile(r"(\d{1,2})\s*[-_]\s*(.*?)\s*[-_]\s*(.*?)(\.\w+)$", re.IGNORECASE),
    re.compile(r"(.*?)\s*[-_]\s*(.*?)\s*\(?feat\.?\s*(.*?)\)?(\.\w+)$", re.IGNORECASE),
    re.compile(r"(.*?)\s*[-_]\s*(.*?)(\.\w+)$", re.IGNORECASE)
]

# Alternative feature artist identifiers
FEATURED_PATTERNS = [r"feat\.?", r"ft\.?", r"featuring"]

def parse_filename(filename):
    """ Extract metadata from filename using flexible patterns. """
    # First, remove the file extension to avoid it being treated as part of the title
    filename_no_ext = re.sub(r"\.(mp3|flac|wav)$", "", filename, flags=re.IGNORECASE)
    
    # Check if any predefined pattern matches
    for pattern in FILENAME_PATTERNS:
        match = pattern.match(filename_no_ext)
        if match:
            groups = match.groups()
            metadata = {
                "track_number": groups[0] if groups[0].isdigit() else "00",
                "artist": groups[1].strip(),
                "title": groups[2].strip(),
                "featured_artists": groups[3].strip() if len(groups) > 3 and groups[3] else "",
                "extension": filename.split('.')[-1]  # Get the file extension
            }
            return metadata
    
    # Fallback: Try to split the filename and extract possible metadata
    parts = re.split(r"[-_]", filename_no_ext)
    parts = [p.strip() for p in parts if p.strip()]

    if len(parts) >= 2:
        # Assume the first part is the artist and the last part is the title
        artist = parts[0]
        title = parts[-1]  # Take the last part as the title
        
        # Ensure file extension is removed
        if title.lower().endswith(('mp3', 'flac', 'wav')):
            title = title.rsplit('.', 1)[0]

        # Detect featured artists
        featured_artists = ""
        for feat_pattern in FEATURED_PATTERNS:
            if re.search(feat_pattern, " ".join(parts), re.IGNORECASE):
                title = " ".join(parts[1:]).split(feat_pattern, 1)[0].strip()  # Title up to "feat."
                featured_artists = " ".join(parts[1:]).split(feat_pattern, 1)[-1].strip()  # Everything after "feat."
                break
        
        metadata = {
            "track_number": "00",
            "artist": artist,
            "title": title,
            "featured_artists": featured_artists,
            "extension": filename.split('.')[-1]  # Get the file extension
        }
        
        return metadata

    return None  # Unable to extract valid metadata

def write_metadata(file_path, metadata):
    """ Writes metadata to a file using Mutagen. """
    try:
        file_ext = os.path.splitext(file_path)[1].lower()

        if file_ext == ".mp3":
            audio = EasyID3(file_path)
        elif file_ext == ".flac":
            audio = FLAC(file_path)
        elif file_ext == ".wav":
            audio = WAVE(file_path)
        else:
            print(f"Skipping unsupported file: {file_path}")
            return

        # Set metadata
        audio["tracknumber"] = metadata["track_number"]
        audio["artist"] = metadata["artist"]
        audio["title"] = metadata["title"]
        
        if metadata["featured_artists"]:
            audio["title"] += f" (feat. {metadata['featured_artists']})"

        # Save changes
        audio.save()
        tqdm.write(f"✔ Metadata applied to: {os.path.basename(file_path)}")

    except Exception as e:
        tqdm.write(f"⚠ Error writing metadata to {os.path.basename(file_path)}: {e}")

def process_files_in_directory(directory):
    """ Processes all audio files in a directory and subdirectories, updating their metadata. """
    supported_extensions = (".mp3", ".flac", ".wav")
    
    # Recursively walk through all directories and files
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(supported_extensions):
                file_path = os.path.join(root, file)
                metadata = parse_filename(file)
                if metadata:
                    write_metadata(file_path, metadata)
                else:
                    tqdm.write(f"⚠ Skipping {file} (Invalid format)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract metadata from filenames and embed it into music files.")
    parser.add_argument("directory", help="Directory containing music files.")
    args = parser.parse_args()

    if os.path.isdir(args.directory):
        process_files_in_directory(args.directory)
    else:
        print("Invalid directory. Please enter a valid path.")