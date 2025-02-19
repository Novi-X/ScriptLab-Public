"""
Directory Structure Generator
-----------------------------
Author: yung-megafone
Date: 2025-02-19
License: MIT License

Description:
This script recursively scans a directory and generates a structured 
ASCII representation of all subdirectories and files.

Features:
- Displays the full folder tree with ASCII characters.
- Shows empty directories as "⚠️ This folder is empty".
- Outputs the directory structure to a text file.
- Displays file sizes in MB, converting to GB if necessary.
- Allows excluding specific file types or directories.
- Provides JSON output support.
- Measures execution time and logs metadata at the top of the output file.
- Supports colorized terminal output for better readability.

Usage:
    python directory_structure.py <directory_path> [--exclude folder1 folder2 --json]

Example:
    python directory_structure.py "/Users/YourName/Music"

Output:
    📂 Music/
    ├── 📂 Rock/
    │   ├── 📄 song1.mp3 (4.35 MB)
    │   ├── 📄 song2.mp3 (3.89 MB)
    └── 📂 Jazz/
        └── 📄 smooth_jazz.mp3 (2.15 MB)
"""
import os
import time
import json
import argparse
from datetime import datetime
from tqdm import tqdm  # Progress bar
from colorama import Fore, Style

def get_directory_tree(root_directory, output_file, exclude=None, json_output=False):
    """Retrieve the directory structure recursively and write it to a file in ASCII format with a progress bar."""
    start_time = time.time()  # Start timing the script execution
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current date/time
    exclude = set(exclude) if exclude else set()  # Convert exclude list to a set for fast lookup

    def generate_tree(folder, prefix="", use_colors=True):
        """Recursively generate the ASCII tree structure."""
        entries = sorted(os.listdir(folder))  # Sort for consistent order
        entries = [e for e in entries if not e.startswith(".") and e not in exclude]  # Filter hidden & excluded items

        folder_entries = [e for e in entries if os.path.isdir(os.path.join(folder, e))]
        file_entries = [e for e in entries if os.path.isfile(os.path.join(folder, e))]
        total_entries = len(folder_entries) + len(file_entries)

        if total_entries == 0:
            return [f"{prefix}⚠️ This folder is empty\n"]

        lines = []
        progress_bar.update(1)  # Update progress bar for each folder processed

        # Iterate through folders
        for index, entry in enumerate(folder_entries):
            is_last = index == (len(folder_entries) + len(file_entries)) - 1
            connector = "└── " if is_last else "├── "
            entry_path = os.path.join(folder, entry)

            folder_name = f"{Fore.BLUE}📂 {entry}/{Style.RESET_ALL}" if use_colors else f"📂 {entry}/"
            lines.append(f"{prefix}{connector}{folder_name}")

            new_prefix = prefix + ("    " if is_last else "│   ")
            lines.extend(generate_tree(entry_path, new_prefix, use_colors))

        # Iterate through files
        for index, entry in enumerate(file_entries):
            is_last = index == len(file_entries) - 1
            connector = "└── " if is_last else "├── "
            entry_path = os.path.join(folder, entry)
            file_size = os.path.getsize(entry_path) / (1024 * 1024)  # Convert to MB

            # Convert to GB if file size > 1024MB
            if file_size > 1024:
                file_size = file_size / 1024
                size_label = f"{file_size:.2f} GB"
            else:
                size_label = f"{file_size:.2f} MB"

            file_entry = f"{Fore.GREEN}📄 {entry} ({size_label}){Style.RESET_ALL}" if use_colors else f"📄 {entry} ({size_label})"
            lines.append(f"{prefix}{connector}{file_entry}")

        return lines

    # Get total folders for progress bar
    total_folders = sum(len(dirs) for _, dirs, _ in os.walk(root_directory))
    global progress_bar
    progress_bar = tqdm(total=total_folders, desc="Scanning Directories", unit="folder", dynamic_ncols=True)

    # Generate tree structure with colors for terminal output
    tree_structure_colored = generate_tree(root_directory, use_colors=True)

    # Generate tree structure without colors for file output
    tree_structure_plain = generate_tree(root_directory, use_colors=False)

    progress_bar.close()  # Close progress bar when done

    end_time = time.time()  # Stop timing execution
    execution_time = end_time - start_time  # Calculate elapsed time

    # Write to file (without color formatting)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("📂 Directory Structure Report\n")
        f.write("Generated by: Directory Structure Generator\n")
        f.write("Author: yung-megafone\n")
        f.write(f"Generated on: {current_date}\n")
        f.write(f"Execution Time: {execution_time:.2f} seconds\n")
        f.write("-" * 50 + "\n\n")  # Separator
        f.write(f"📂 {os.path.basename(root_directory)}/\n")
        f.write("\n".join(tree_structure_plain) + "\n")

    print(f"\n{Fore.GREEN}✔ Directory structure saved to:{Style.RESET_ALL} {output_file}")

    # Print to terminal with colors
    print("\n".join(tree_structure_colored))

    # JSON Output
    if json_output:
        json_file = output_file.replace(".txt", ".json")
        tree_dict = {"name": os.path.basename(root_directory), "children": tree_structure_plain}
        with open(json_file, "w", encoding="utf-8") as jf:
            json.dump(tree_dict, jf, indent=4)
        print(f"{Fore.GREEN}✔ JSON output saved to:{Style.RESET_ALL} {json_file}")

# Command-line argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an ASCII directory structure with file sizes and optional exclusions.")
    parser.add_argument("directory", help="Directory to scan.")
    parser.add_argument("--exclude", nargs="+", help="Folders or file types to exclude", default=[])
    parser.add_argument("--json", action="store_true", help="Output directory structure as JSON")

    args = parser.parse_args()
    root_directory = args.directory.strip()
    output_file = "directory_structure.txt"

    if os.path.isdir(root_directory):
        get_directory_tree(root_directory, output_file, exclude=args.exclude, json_output=args.json)
    else:
        print(f"{Fore.RED}Error:{Style.RESET_ALL} Invalid directory. Please enter a valid path.")