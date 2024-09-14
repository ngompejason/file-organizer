import os
import shutil
from pathlib import Path
import time
import logging

# FileOrganizer class: Main class for organizing files in a directory
class FileOrganizer:

    # File extensions for different types of files
    # You can add or remove extensions based on your needs
    audio_extensions = (".3ga", ".aac", ".ac3", ".aif", ".aiff", ".alac", ".amr", ".ape", ".au", ".dss", ".flac", ".flv", ".m4a", ".m4b", ".m4p", ".mp3", ".mpga", ".ogg", ".oga", ".mogg", ".opus", ".qcp", ".tta", ".voc", ".wav", ".wma", ".wv")
    video_extensions = (".webm", ".MTS", ".M2TS", ".TS", ".mov", ".mp4", ".m4p", ".m4v", ".mxf")
    img_extensions = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png", ".gif", ".webp", ".svg", ".apng", ".avif")
    doc_extensions = (".pdf", ".docx", ".doc", ".epub", ".txt", ".xlsx", ".pptx")
    archives_extensions = (".zip", ".tar", ".rar", ".7z", ".gz")

    def __init__(self, directory: Path):
        """Initialize the FileOrganizer with the target directory to organize files in."""
        self.directory = directory
        # Set up logging to keep track of actions like file movements or errors
        self.logger = self.file_logger()

    def file_logger(self):
        """Set up logging to keep track of file operations"""
        logger = logging.getLogger(__name__)
        # Set the log level to INFO to track general file operations
        logger.setLevel(logging.INFO)
        
        # Create a file handler for the log file
        myhandler = logging.FileHandler("file_organizer.log")
        # Create a formatter for the log messages
        format = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s: %(message)s")
        myhandler.setFormatter(format)
        
        # Add the handler to the logger
        logger.addHandler(myhandler)
        return logger

    def is_file_type(self, file, extension:tuple) -> bool:
        """Check if the file extension matches one of the specified types."""
        return os.path.splitext(file)[1].lower() in extension

    def mkkdir(self, name: str) -> Path:
        """Create a directory for organizing files, if it doesn't already exist."""
        folder_path = self.directory / name
        if not folder_path.exists():
            folder_path.mkdir(parents=True, exist_ok=True)
            # Log the creation of the directory
            self.logger.info(f"{folder_path} created")
        return folder_path
    
    def movefile(self, destination_path: Path, file: str):
        """Move the file to the destination folder, renaming if a file with the same name already exists."""
        destination_file = destination_path / file
        source_file_path = self.directory / file
        try:
            if destination_file.exists():
                # If the file already exists, append a counter to the filename to avoid overwriting
                filename, extension = os.path.splitext(file)
                count = 1

                while destination_file.exists():
                    new_filename = f"{filename}({count}){extension}"
                    destination_file = destination_path / new_filename
                    count += 1
                self.logger.info(f"Renamed {file} to {new_filename}")

                shutil.move(source_file_path, destination_file)
                self.logger.info(f"Moved {new_filename} to {destination_path}")
            else:
                # If no conflict, move the file directly
                shutil.move(source_file_path, destination_path)
                self.logger.info(f"Moved {file} to {destination_path}")
        except Exception as e:
            # Log any errors that occur during the move operation
            self.logger.error(f"Error moving '{file}': {str(e)}")

    def organize_files(self):
        """Organize the files in the directory into appropriate subfolders based on file type."""
        for file in os.listdir(self.directory):
            # Check the file type and move to appropriate folder
            if self.is_file_type(file, self.audio_extensions):
                destination_path = self.mkkdir("Audio Downloaded")
                self.movefile(destination_path=destination_path,file=file)
            elif self.is_file_type(file, self.video_extensions):
                destination_path = self.mkkdir("Video Downloaded")
                self.movefile(destination_path=destination_path,file=file)
            elif self.is_file_type(file, self.img_extensions):
                destination_path = self.mkkdir("Image Downloaded")
                self.movefile(destination_path=destination_path,file=file)
            elif self.is_file_type(file, self.doc_extensions):
                destination_path = self.mkkdir("Documents Downloaded")
                self.movefile(destination_path=destination_path,file=file)
            elif self.is_file_type(file, self.archives_extensions):
                destination_path = self.mkkdir("Archives Downloaded")
                self.movefile(destination_path=destination_path,file=file)
            else:
                # If the file doesn't match any known type, do nothing
                pass

# Main execution
if __name__ == "__main__":
    # Set the directory to organize (in this case, the user's Downloads folder)
    downloads_dir = Path.home() / "Downloads"
    organizer = FileOrganizer(downloads_dir)

    # Run the organizer continuously, checking every 5 seconds
    while True:
        organizer.organize_files()
        time.sleep(5)