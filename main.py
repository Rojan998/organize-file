import time
import shutil
from pathlib import Path
import os


def get_downloads_folder() -> Path:
    # Works for most Windows setups
    userprofile = Path(os.environ["USERPROFILE"])
    print(userprofile)
    downloads = userprofile / "Downloads"
    return downloads


TARGET_DIR = get_downloads_folder()

CATEGORIES = {
    "pdf": {".pdf"},
    "word": {".doc", ".docx"},
    "images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff"},
    "excel": {".xls", ".xlsx", ".csv"},
    "powerpoint": {".ppt", ".pptx"},
    "text": {".txt", ".md", ".rtf"},
    "archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "audio": {".mp3", ".wav", ".m4a", ".flac", ".aac"},
    "video": {".mp4", ".mkv", ".mov", ".avi", ".wmv"},
}

OTHER_FOLDER = "other"
CHECK_EVERY_SECONDS = 5


def category_for(ext: str) -> str:
    ext = ext.lower()
    for folder, exts in CATEGORIES.items():
        if ext in exts:
            return folder
    return OTHER_FOLDER


def move_file(src: Path, dest_folder: Path) -> None:
    dest_folder.mkdir(parents=True, exist_ok=True)
    dest = dest_folder / src.name

    # avoid overwriting
    if dest.exists():
        stem, suffix = src.stem, src.suffix
        i = 1
        while True:
            candidate = dest_folder / f"{stem} ({i}){suffix}"
            if not candidate.exists():
                dest = candidate
                break
            i += 1

    shutil.move(str(src), str(dest))


def organize_once():
    for item in TARGET_DIR.iterdir():
        if item.is_dir():
            continue

        # skip partial downloads (Chrome/Edge)
        if item.suffix.lower() in {".crdownload", ".tmp", ".part"}:
            continue

        folder_name = category_for(item.suffix)
        move_file(item, TARGET_DIR / folder_name)


def main():
    print(f"Watching folder: {TARGET_DIR}")
    print("Press Ctrl + C to stop.\n")

    while True:
        try:
            organize_once()
            time.sleep(CHECK_EVERY_SECONDS)
        except KeyboardInterrupt:
            print("\nStopped.")
            break
        except Exception as e:
            print("Error:", e)
            time.sleep(CHECK_EVERY_SECONDS)


if __name__ == "__main__":
    main()
