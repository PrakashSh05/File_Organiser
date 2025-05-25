import os
import shutil
import logging
from pathlib import Path
import argparse

FILE_TYPES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".webm"],
    "Audios": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Programming": [".py", ".java", ".cpp", ".c", ".cs", ".js", ".ts", ".rb", ".go", ".php"],
    "WebFiles": [".html", ".css", ".js", ".json", ".xml"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Executables": [".exe", ".msi", ".sh", ".bat", ".apk"]
}

def init_logging(log_path="organizer.log"):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )

def classify_file(file):
    ext = file.suffix.lower()
    if not ext:
        return "no_extension"
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return ext.lstrip(".")

def organize_folder(folder):
    if not folder.exists() or not folder.is_dir():
        logging.error("Invalid folder path.")
        print("Invalid folder path.")
        return

    moved = 0

    for file in folder.iterdir():
        if file.is_file():
            category = classify_file(file)
            target = folder / category

            if not target.exists():
                try:
                    target.mkdir()
                    logging.info(f"Created folder: {category}")
                except Exception as e:
                    logging.error(f"Could not create folder '{category}': {e}")
                    continue

            destination = target / file.name
            try:
                if not destination.exists():
                    shutil.move(str(file), str(destination))
                    moved += 1
                    logging.info(f"Moved '{file.name}' to '{category}/'")
                else:
                    logging.warning(f"Skipped '{file.name}' (already exists in '{category}/')")
            except Exception as e:
                logging.error(f"Error moving '{file.name}': {e}")

    print(f"Done. Moved {moved} file(s).")
    logging.info("Organization complete.")

def main():
    parser = argparse.ArgumentParser(description="Simple File Organizer")
    parser.add_argument('--path', required=True, help="Path to the folder to organize")
    parser.add_argument('--log', default="organizer.log", help="Log file name")

    args = parser.parse_args()
    folder_path = Path(args.path).resolve()

    init_logging(args.log)
    organize_folder(folder_path)

if _name_ == "_main_":
    main()