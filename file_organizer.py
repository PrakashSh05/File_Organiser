import os
import shutil

FILE_TYPES = {
    "Documents":[".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Images":[".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".webm"],
    "Audios": [".mp3", ".wav",  ".aac", ".flac", ".ogg"],
    "Programming": [".py",  ".java", ".cpp", ".c", ".cs", ".js", ".ts", ".rb", ".go", ".php"],
    "WebFiles":[".html", ".css", ".js", ".json", ".xml"],
    "Archives": [".zip", ".rar",".tar", ".gz", ".7z"],
    "Executables": [".exe",".msi", ".sh", ".bat", ".apk"],
    "Others":[]
}

def create_category_folders(path):
    for category in FILE_TYPES:
        folder =os.path.join(path, category)
        try:
            os.makedirs(folder, exist_ok=True)
        except Exception as e:
            print(f"Couldn't create folder '{folder}': {e}")

def get_file_category(filename):
    _, ext =os.path.splitext(filename.lower())
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return "Others"

def organize_files_in_folder(path):
    create_category_folders(path)
    try:
        for item in os.listdir(path):
            item_path =os.path.join(path, item)
            if os.path.isfile(item_path):
                category  = get_file_category(item)
                dest_folder= os.path.join(path, category)
                dest_path =  os.path.join(dest_folder, item)
                try:
                    shutil.move(item_path, dest_path)
                except Exception as move_err:
                    print(f"Error moving '{item}' to '{category}': {move_err}")
    except Exception as err:
        print (f"Something went wrong while organizing files: {err}")

if __name__ =="__main__":
    folder = input("Enter the folder path to organize: ").strip()
    if not os.path.isdir(folder):
        print("That path doesn't seem to be valid. Please check and try again.")
    else:
        organize_files_in_folder(folder)
        print("All set! Your files have been organized.")
