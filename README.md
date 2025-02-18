# ScriptLab

## Overview

**ScriptLab** is a collection of automation scripts designed to streamline and simplify various tasks. This repository includes tools for file renaming, organization, and more, aiming to enhance productivity and efficiency.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Renamers**: Scripts to bulk rename files based on specific criteria.
  - `checksum-rename.py`: Renames files based on their SHAKE-128 checksum.
  - `music-renamer.py`: Renames music files using metadata to format filenames as "## - Artist Name - Song Title (feat. Featured Artist).mp3/flac/wav".

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yung-megafone/ScriptLab.git
   cd ScriptLab
   ```

2. **Install Dependencies**:
   - Ensure you have Python 3.6+ installed.
   - Install required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

## Usage

Navigate to the directory containing the desired script and execute it with Python:

```bash
python script_name.py /path/to/target/directory
```

For example, to use the music renamer script:

```bash
python music_renamer.py /path/to/music/files
```

Follow any on-screen prompts to complete the process.

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request. For major changes, open an issue first to discuss what you'd like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.