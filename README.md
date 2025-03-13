# TArchiver - Terminal Archiver

## Overview

TArchiver (Terminal Archiver) is a powerful and versatile command-line tool designed to handle various archive formats with ease. Built using Python, TArchiver provides a simple yet robust interface for creating, extracting, and listing files in archives. It supports popular formats such as ZIP, TAR, TAR.GZ, GZIP, 7Z, RAR, and XZ. Whether you're a system administrator, developer, or power user, TArchiver simplifies archive management directly from the terminal.

## Features

- **Multiple Archive Formats**: Supports creation, extraction, and listing of files in ZIP, TAR, TAR.GZ, GZIP, 7Z, RAR, and XZ formats.
- **Password Protection**: Encrypt and decrypt archives using passwords for 7Z and RAR formats.
- **Rich Terminal Output**: Utilizes the `rich` library for visually appealing and informative terminal output.
- **Error Handling**: Provides clear error messages for invalid paths or unsupported operations.
- **Cross-Platform**: Works on any system with Python 3 and the required command-line tools installed.

## Installation

To install TArchiver, follow these steps:

1. **Download the Script**:
   Use `wget` to download the TArchiver script directly from the repository:
   ```bash
   wget https://raw.githubusercontent.com/linuxfanboy4/tarchiver/refs/heads/main/tarchiver.py
   ```

2. **Run the Script**:
   Execute the script using Python 3:
   ```bash
   python3 tarchiver.py
   ```

3. **Dependencies**:
   Ensure the following command-line tools are installed on your system:
   - `zip` and `unzip` for ZIP archives.
   - `tar` for TAR and TAR.GZ archives.
   - `gzip` and `gunzip` for GZIP archives.
   - `7z` for 7Z archives.
   - `rar` and `unrar` for RAR archives.
   - `xz` for XZ archives.

   Install these tools using your package manager if they are not already installed. For example, on Ubuntu:
   ```bash
   sudo apt install zip unzip tar gzip p7zip-full rar unrar xz-utils
   ```

## Usage

TArchiver is designed to be intuitive and easy to use. Below are the available commands and their usage:

### General Syntax
```bash
python3 tarchiver.py <command> <archive> [files] [options]
```

### Commands

1. **Create an Archive**:
   - **ZIP**: `python3 tarchiver.py create archive.zip file1 file2`
   - **TAR**: `python3 tarchiver.py create archive.tar file1 file2`
   - **TAR.GZ**: `python3 tarchiver.py create archive.tar.gz file1 file2`
   - **GZIP**: `python3 tarchiver.py create archive.gz file1`
   - **7Z**: `python3 tarchiver.py create archive.7z file1 file2 -p password`
   - **RAR**: `python3 tarchiver.py create archive.rar file1 file2 -p password`

2. **Extract an Archive**:
   - **ZIP**: `python3 tarchiver.py extract archive.zip destination_folder`
   - **TAR**: `python3 tarchiver.py extract archive.tar destination_folder`
   - **TAR.GZ**: `python3 tarchiver.py extract archive.tar.gz destination_folder`
   - **GZIP**: `python3 tarchiver.py extract archive.gz destination_folder`
   - **7Z**: `python3 tarchiver.py extract archive.7z destination_folder -p password`
   - **RAR**: `python3 tarchiver.py extract archive.rar destination_folder -p password`
   - **XZ**: `python3 tarchiver.py extract archive.xz destination_folder`

3. **List Files in an Archive**:
   - **ZIP**: `python3 tarchiver.py list archive.zip`
   - **TAR**: `python3 tarchiver.py list archive.tar`
   - **TAR.GZ**: `python3 tarchiver.py list archive.tar.gz`
   - **7Z**: `python3 tarchiver.py list archive.7z`
   - **RAR**: `python3 tarchiver.py list archive.rar`

### Options

- **Password Protection**:
  Use the `-p` or `--password` option to specify a password for creating or extracting encrypted archives (7Z and RAR only).

### Examples

1. **Create a ZIP Archive**:
   ```bash
   python3 tarchiver.py create backup.zip file1.txt file2.txt
   ```

2. **Extract a TAR.GZ Archive**:
   ```bash
   python3 tarchiver.py extract archive.tar.gz /path/to/extract
   ```

3. **List Files in a 7Z Archive**:
   ```bash
   python3 tarchiver.py list archive.7z
   ```

4. **Create a Password-Protected RAR Archive**:
   ```bash
   python3 tarchiver.py create secret.rar file1.txt file2.txt -p mypassword
   ```

5. **Extract a Password-Protected 7Z Archive**:
   ```bash
   python3 tarchiver.py extract secret.7z /path/to/extract -p mypassword
   ```
## Contributing

Contributions to TArchiver are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/linuxfanboy4/tarchiver).

## License

TArchiver is released under the MIT License. See the [LICENSE](https://github.com/linuxfanboy4/tarchiver/blob/main/LICENSE) file for more details.

## Support

For support or questions, please open an issue on the [GitHub repository](https://github.com/linuxfanboy4/tarchiver).
