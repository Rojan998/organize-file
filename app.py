import os
import shutil
from pathlib import Path
import time


def get_downloads_path() -> Path:
    userName = Path(os.environ["USERNAME"])
    dir_name = userName / "Downloads"
    return dir_name


TARGET_DIR = get_downloads_path()
CHECK_EVERY_SECONDS = 5

file_type = {
    "pdf":{
        ".pdf"
    },
    "word":{
        ".docs",".docx"
    },
    "images":{
        ".png",".jpeg",".jpg",".gif",".bmp",".webp",".tiff"
    },
    "excel":{
        ".xls"
    }
}


def organize_folder():
    


def main():
    print(f"Watching folder: {TARGET_DIR}")
    print(f"Press CTRL + C to abort the process .....\n")

    while True:
        try:
            organize_folder()
            time.sleep(CHECK_EVERY_SECONDS)
        except KeyboardInterrupt:
            print("\n Stopped....")
            break
        except Exception as e:
            print("Error:", e)
            time.sleep(CHECK_EVERY_SECONDS)


if __name__ == "__main__":
    main()
