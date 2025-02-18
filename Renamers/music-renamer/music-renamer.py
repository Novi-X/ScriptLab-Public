import os
import re
import glob as fileFinder
import mutagen as metadataAnalyzer
import shutil
import argparse


# We first need to obtain the files we wish to modify
def gather_all_of_the_music_files(directory: str):
    """ Retrieves all of the music files within the supplied directory"""
    # Use Glob to find all .mp3 .flac .wav files (more coming soon!)
    supported_file_extensions = ["*.mp3", "*.flac", "*.wav"]
    music_files = [file for ext in supported_file_extensions for file in fileFinder.glob(os.path.join(directory, ext))]
    
    return music_files


# Then we must extract the metadata and read the necessary parts
def extract_metadata_from_file(file_path):
    """ Extracts metadata from MP3, WAV, and FLAC, files """
    audio = metadataAnalyzer.File(file_path, easy = True) # Automagically detects file format

    # If the file is not audio, skip and provide feedback to the user
    if not audio:
        print(f"Skipping: {file_path} (Unsupported Filetype!)")
        return None

    # Safely extract the metadata
    metadata = {
        "track_number": audio.get("tracknumber", ["00"])[0].split("/")[0].zfill(2),
        "title": audio.get("title", ["Unknown Title"])[0],
        "artist": audio.get("artist", ["Unknown Artist"])[0],
    }

    # Handle featrured artists, if any are in the title
    title = metadata["title"]
    if "feat." in title.lower():
        metadata["featured_artists"] = title.split("feat.")[-1].strip(" ()")
    else:
        metadata["featured_artists"] = ""

    return metadata


# We must now format the new filename properly using the extracted metadata
def format_the_filename(metadata: dict, file_extension: str):
    """ Generates a properly formatted filename based on extracted metadata """
    track = metadata["track_number"].zfill(2) # ensures a two-digit track number
    artist = metadata["artist"]
    title = metadata["title"]
    featured = metadata["featured_artists"]

    # Construct the file format
    if featured:
        new_track_name = f"{track} - {artist} - {title} (feat. {featured}){file_extension}"
    else:
        new_track_name = f"{track} - {artist} - {title}{file_extension}"

    return new_track_name


# Sanitize the title to prevent errors
def sanitize_dirty_filename(filename: str):
    """ Removes invalid characters from filenames """
    return re.sub(r'[<>:"/\\|?*]', '', filename) # Remove forbidden characters


# Rename the files safely to avoid overwrites
def rename_music_files(file_path: str, new_track_name: str, output_directory: str, copy_files: bool):
    """ Renames the file and moves it to an organized directory """
    new_track_name = sanitize_dirty_filename(new_track_name) # Remove invalid chars
    new_file_path = os.path.join(output_directory, new_track_name) if copy_files else os.path.join(os.path.dirname(file_path), new_track_name)

    # Prevent overwriting by incrementing duplicate filenames
    counter = 1
    # If a file already exists
    while os.path.exists(new_file_path):
        # Separate the filename and the extension
        base,ext = os.path.splitext(new_track_name)
        # Append the counter within () at the end of the filename
        new_file_path = os.path.join(output_directory, f"{base} ({counter}){ext}")
        counter += 1

    # Perform copy or rename
    if copy_files:
        shutil.copy2(file_path, new_file_path) # Copy file with metadata
        print(f"Copied: {os.path.basename(file_path)} → {new_track_name}")
    else:
        os.rename(file_path, new_file_path)
        print(f"Renamed: {os.path.basename(file_path)} → {new_track_name}")


# Specify an output directory
def ensure_output_directory(base_directory: str):
    """ Ensures an output dir exists for renamed files """
    output_directory = os.path.join(base_directory, "Renamed Music")
    os.makedirs(output_directory, exist_ok=True) # Create if it doesn't exist
    return output_directory


# Define the main function for this script
def main():
    parser = argparse.ArgumentParser(description="Rename music files using metadata.")
    parser.add_argument("directory", help="Directory containing music files.")
    parser.add_argument("--copy", action="store_true", help="Copy renamed files to a new directory instead of renaming in place.")

    args = parser.parse_args()
    music_folder = args.directory.strip()
    copy_files = args.copy  # Boolean flag

    if not os.path.isdir(music_folder):
        print("Invalid directory. Please enter a valid folder path.")
        return

    # Only create "Renamed Music" directory if --copy flag is used
    if copy_files:
        output_directory = ensure_output_directory(music_folder)
    else:
        output_directory = music_folder  # Keep files in the same directory

    music_files = gather_all_of_the_music_files(music_folder)  # Gather all music files

    for file in music_files:
        metadata = extract_metadata_from_file(file)  # Extract metadata
        if metadata:
            file_extension = os.path.splitext(file)[1]  # Preserve file extension
            new_track_name = format_the_filename(metadata, file_extension)
            rename_music_files(file, new_track_name, output_directory, copy_files)


if __name__ == "__main__":
    main()
