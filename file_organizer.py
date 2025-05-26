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
    for category, exts in FILE_TYPES.items():
        if ext in exts:
            return category
    return "Others"

def organize_folder(folder):
    if not folder.exists() or not folder.is_dir():
        logging.error("Invalid folder path.")
        print("Invalid folder path.")
        return

    moved = 0
    for file in folder.iterdir():
        if file.name.startswith(('.', '$')) or not file.is_file():
            continue

        category = classify_file(file)
        target_dir = folder / category
        target_dir.mkdir(exist_ok=True)

        dest = target_dir / file.name
        try:
            if not dest.exists():
                shutil.move(str(file), str(dest))
                logging.info(f"Moved '{file.name}' to '{category}/'")
                moved += 1
            else:
                logging.warning(f"Skipped '{file.name}' (already exists in '{category}/')")
        except Exception as e:
            logging.error(f"Error moving '{file.name}': {e}")

    print(f"Done. Moved {moved} file(s).")
    logging.info("Organization complete.")

def main():
    parser = argparse.ArgumentParser(description="Simple File Organizer")
    parser.add_argument('--path', required=True, help="Folder to organize")
    parser.add_argument('--log', default="organizer.log", help="Log file")

    args = parser.parse_args()
    folder = Path(args.path).resolve()

    init_logging(args.log)
    organize_folder(folder)

if __name__ == "__main__":
    main()
