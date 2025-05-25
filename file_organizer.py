import os
import shutil
import logging
import argparse
from pathlib import Path

# Define file categories and extensions
FILE_CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".webm"],
    "Audios": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Programming": [".py", ".java", ".cpp", ".c", ".cs", ".js", ".ts", ".rb", ".go", ".php"],
    "WebFiles": [".html", ".css", ".js", ".json", ".xml"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Executables": [".exe", ".msi", ".sh", ".bat", ".apk"],
    "Others": []
}

def setup_logging(log_file="organizer.log"):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler(log_file, encoding="utf-8")]
    )

def create_category_folders(base_path):
    for category in FILE_CATEGORIES:
        try:
            (base_path / category).mkdir(exist_ok=True)
        except Exception as e:
            print(f"Error creating folder '{category}': {e}")
            logging.error(f"Error creating folder '{category}': {e}")

def get_file_category(file_path):
    return next((cat for cat, ext in FILE_CATEGORIES.items() if file_path.suffix.lower() in ext), "Others")

def organize_files(base_path):
    try:
        create_category_folders(base_path)
        for item in base_path.iterdir():
            if item.is_file():
                category = get_file_category(item)
                target = base_path / category / item.name
                try:
                    if not target.exists():
                        shutil.move(str(item), str(target))
                        logging.info(f"Moved '{item.name}' → {category}")
                    else:
                        logging.warning(f"Skipped '{item.name}' (already exists in '{category}')")
                except Exception as e:
                    print(f"Problem moving '{item.name}': {e}")
                    logging.error(f"Failed to move '{item.name}': {e}")
        print("Done! Files have been sorted.")
        logging.info("Organization finished successfully.")
    except Exception as e:
        print(f"Something went wrong: {e}")
        logging.error(f"Unexpected error: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="📁 Organize files in a folder by their file types.",
        epilog="Example: python file_organizer.py --path /path/to/folder"
    )
    parser.add_argument(
        '--path', type=str, required=True,
        help="Path of the folder you want to organize"
    )
    parser.add_argument(
        '--log', type=str, default="organizer.log",
        help="Path to the log file (default: organizer.log)"
    )

    args = parser.parse_args()
    base_path = Path(args.path)

    if not base_path.exists() or not base_path.is_dir():
        print("❌ Invalid folder path. Please check and try again.")
        return

    setup_logging(args.log)
    organize_files(base_path)

if __name__ == "__main__":
    main()