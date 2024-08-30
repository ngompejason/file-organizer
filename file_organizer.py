import os
import shutil
from pathlib import Path
import time
import logging


class FileOrganizer:

    audio_extensions = (".3ga", ".aac", ".ac3", ".aif", ".aiff", ".alac", ".amr", ".ape", ".au", ".dss", ".flac", ".flv", ".m4a", ".m4b", ".m4p", ".mp3", ".mpga", ".ogg", ".oga", ".mogg", ".opus", ".qcp", ".tta", ".voc", ".wav", ".wma", ".wv")
    video_extensions = (".webm", ".MTS", ".M2TS", ".TS", ".mov", ".mp4", ".m4p", ".m4v", ".mxf")
    img_extensions = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png", ".gif", ".webp", ".svg", ".apng", ".avif")
    doc_extensions = (".pdf", ".docx", ".doc", ".epub", ".txt", ".xlsx", ".pptx")
    archives_extensions = (".zip", ".tar", ".rar", ".7z", ".gz")


    def __init__(self, directory: Path):
        self.directory = directory
        self.setup_logger()

    def setup_logger(self):
        pass

    def is_audio (self, file)  -> bool:
        #get the extension of the file and check if it's an audio
        return os.path.splitext(file)[1] in self.audio_extensions

    def is_video(self, file) -> bool:
        #get the extension of the file and check if it's an video
        return os.path.splitext(file)[1] in self.video_extensions

    def is_image(self, file) -> bool:
        #get the extension of the file and check if it's an image
        return os.path.splitext(file)[1] in self.img_extensions

    def is_document(self, file) -> bool:
        return os.path.splitext(file)[1].lower() in self.doc_extensions

    def is_archive(self, file) -> bool:
        return os.path.splitext(file)[1].lower() in self.archives_extensions


    def mkkdir(self, name: str) -> Path:
        folder_path = self.directory / name
        if not folder_path.exists():
            folder_path.mkdir(parents=True, exist_ok=True)
        return folder_path
    
    def movefile(self, destination_path: Path, file: Path):
        destination_file = destination_path / file
        source_file_path = self.directory / file
        if destination_file.exists():
            filename, extension = os.path.splitext(file)
            count = 1

            while destination_file.exists():
                destination_file = destination_path / f"{filename}({count}){extension}"
                count += 1
            shutil.move(source_file_path, destination_file)
        else:
            shutil.move(source_file_path, destination_path)
    
    def organize_files(self):

        for file in os.listdir(self.directory):
            source_file_path = self.directory / file
            if self.is_audio(file):
                destination_path = self.mkkdir("Audio Downloaded")
                self.movefile(destination_path=destination_path,file=file)
            elif self.is_video(file):
                destination_path = self.mkkdir("Video Downloaded")
                self.movefile(destination_path=destination_path,file=file)
            elif self.is_image(file):
                destination_path = self.mkkdir("Image Downloaded")
                self.movefile(destination_path=destination_path,file=file)
            elif self.is_document(file):
                destination_path = self.mkkdir("Documents Downloaded")
                self.movefile(destination_path=destination_path,file=file)
            elif self.is_archive(file):
                destination_path = self.mkkdir("Archives Downloaded")
                self.movefile(destination_path=destination_path,file=file)
            else:
                pass


if __name__ == "__main__":
    downloads_dir = Path.home() / "Downloads"
    organizer = FileOrganizer(downloads_dir)

    while True:
        organizer.organize_files()
        time.sleep(5)

