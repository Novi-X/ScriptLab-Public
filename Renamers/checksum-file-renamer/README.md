# Checksum File Renamer

## Developed by: yung-megafone

## License: MIT License

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Notes](#notes)
- [License](#license)

## Overview

**Version 1.1.0** - This update improves performance by 10.31% over the previous release.

Checksum File Renamer is a Python script that processes files within a directory by renaming them based on their SHAKE-128 checksum. The script ensures uniqueness in file naming and prevents duplication by removing redundant files.

## Features

- Computes SHAKE-128 checksums efficiently for all files.
- Renames files using their checksum while preserving original file extensions.
- Automatically removes duplicate files with the same checksum.
- Utilizes multithreading to improve performance.
- Allows customizable checksum length (default: 12 bytes).

## Requirements

- Python 3.6+

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/yung-megafone/ScriptLab/Renamers/checksum-file-renamer.git
cd checksum-file-renamer
```

## Usage

Run the script with the following command:

```bash
python checksum-rename.py <directory_path>
```

The script will prompt for the checksum length. Press Enter to use the default value (12 bytes), or enter a custom value.

## Example

```bash
python checksum-rename.py /path/to/directory
Enter checksum filename length (default: 12): 16
```

This command renames all files in `/path/to/directory` using a 16-byte SHAKE-128 checksum.

## Notes

- Files already named with their checksum will be skipped.
- If a file with the same checksum-based name exists, duplicates are removed.
- Threading is utilized to enhance processing speed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

