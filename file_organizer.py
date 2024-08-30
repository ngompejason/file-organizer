import os
import shutil
from pathlib import Path
import time


class FileOrganizer:

    audio_extensions = (".3ga", ".aac", ".ac3", ".aif", ".aiff", ".alac", ".amr", ".ape", ".au", ".dss", ".flac", ".flv", ".m4a", ".m4b", ".m4p", ".mp3", ".mpga", ".ogg", ".oga", ".mogg", ".opus", ".qcp", ".tta", ".voc", ".wav", ".wma", ".wv")
    video_extensions = (".webm", ".MTS", ".M2TS", ".TS", ".mov", ".mp4", ".m4p", ".m4v", ".mxf")
    img_extensions = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png", ".gif", ".webp", ".svg", ".apng", ".avif")
    doc_extensions = (".pdf", ".docx", ".doc", ".epub", ".txt", ".xlsx", ".pptx")
    archives_extensions = (".zip", ".tar", ".rar", ".7z", ".gz")


    def __init__(self, directory: Path):
        self.directory = directory

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
    
    def organize_files(self):

        for file in os.listdir(self.directory):
            file_path = self.directory / file
            if self.is_audio(file):
                folder_path = self.mkkdir("Audio Downloaded")
            elif self.is_video(file):
                folder_path = self.mkkdir("Video Downloaded")
                shutil.move(file_path, folder_path)
            elif self.is_image(file):
                folder_path = self.mkkdir("Image Downloaded")
                if os.path.exists(folder_path / file):
                    return
                shutil.move(file_path, folder_path)
            elif self.is_document(file):
                folder_path = self.mkkdir("Documents Downloaded")
                shutil.move(file_path, folder_path)
            elif self.is_archive(file):
                folder_path = self.mkkdir("Archives Downloaded")
                shutil.move(file_path, folder_path)
            else:
                pass


if __name__ == "__main__":
    downloads_dir = Path.home() / "Downloads"
    organizer = FileOrganizer(downloads_dir)

    while True:
        organizer.organize_files()
        time.sleep(5)

