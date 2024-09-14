# File Organizer

A Python script that organizes files in a directory by sorting them into subfolders based on their file types. The script supports a wide range of file formats, such as audio, video, images, documents, and archives. This is particularly useful for cleaning up the `Downloads` folder, where files can accumulate over time.

## Features

- Automatically detects and categorizes files into subfolders like:
  - **Audio Downloaded**
  - **Video Downloaded**
  - **Image Downloaded**
  - **Documents Downloaded**
  - **Archives Downloaded**
- Logs file operations and errors using Python's logging module.
- Prevents file overwriting by renaming files if a conflict arises.
- Continually monitors the target directory and organizes files every 5 seconds.

## Supported File Types

- **Audio**: `.mp3`, `.wav`, `.flac`, etc.
- **Video**: `.mp4`, `.mov`, `.webm`, etc.
- **Images**: `.jpg`, `.png`, `.gif`, etc.
- **Documents**: `.pdf`, `.docx`, `.txt`, etc.
- **Archives**: `.zip`, `.tar`, `.rar`, etc.

## Setup

Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/ngompejason/file-organizer.git && cd file-organizer
   ```
## Usage

1. Run the script:
   ```bash
    python file_organizer.py
   ```
2. By default, the script will organize files in your Downloads folder. To change this, modify the downloads_dir variable in the __main__ section of the script.
3. File conflicts are handled by appending a counter to the filename to avoid overwriting.
4. The script will run continuously, checking for new files every 5 seconds.

## Logging
The script logs all actions and errors to `file_organizer.log` in the same directory as the script.

## Customization
You can customize the following aspects:
- Modify the file extensions in the FileOrganizer class to include additional formats.
- Change the target directory by passing a different path to FileOrganizer.

#### Contributions, issues, and feature requests are welcome.


