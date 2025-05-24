import os
import shutil

FILE_TYPES = {
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

def create_folders(base_path):
    for category in FILE_TYPES:
        folder_path = os.path.join(base_path, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def find_category(filename):
    _, ext = os.path.splitext(filename.lower())
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return "Others"

def organize_files(base_path):
    create_folders(base_path)
    for item in os.listdir(base_path):
        full_path = os.path.join(base_path, item)
        if os.path.isfile(full_path):
            category = find_category(item)
            destination_folder = os.path.join(base_path, category)
            destination_path = os.path.join(destination_folder, item)
            if not os.path.exists(destination_path):
                shutil.move(full_path, destination_path)

if __name__ == "__main__":
    user_path = input("Enter the path of the folder to organize: ").strip()
    if os.path.isdir(user_path):
        organize_files(user_path)
        print("Files organized.")
    else:
        print("Invalid path.")
