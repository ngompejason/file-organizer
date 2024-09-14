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

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/file-organizer.git
   cd file-organizer
