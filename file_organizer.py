import os
import shutil
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("organizer.log", encoding="utf-8")
    ]
)

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

def create_category_folders(base_path):
    for category in FILE_CATEGORIES:
        try:
            (base_path / category).mkdir(exist_ok=True)
        except Exception as e:
            print(f"Error creating folder '{category}': {e}")
            logging.error(f"Error creating folder '{category}': {e}")

def get_file_category(file_name):
    return next((cat for cat, ext in FILE_CATEGORIES.items() if file_name.suffix.lower() in ext), "Others")

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

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder you want to organize: ").strip()
    path = Path(folder_path)

    if not path.exists() or not path.is_dir():
        print("Invalid folder path. Please check and try again.")
    else:
        organize_files(path)
