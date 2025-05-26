# 🗂️ File Organizer Script

A collaborative Python project that helps automatically organize cluttered folders by categorizing files into subfolders based on their types. This tool simplifies digital workspace management by reducing manual effort and promoting clean directory structures.

---

## 🚀 Features

- 🔍 Scans the target folder and identifies files based on their extensions  
- 📁 Automatically creates and organizes files into subfolders such as Documents, Images, Videos, Audios, Programming, Archives, Executables, WebFiles, and Others  
- 🛑 Skips system/hidden files and already organized content  
- 🧾 Logs all activities and handles exceptions gracefully  
- 🧠 Designed with modular and extensible Python code  

---

## 📂 How It Works

The script uses a dictionary to classify common file extensions into categories. It then moves each file into a corresponding folder. If a file’s type isn’t listed, it gets moved to the “Others” folder.
```
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
```
🛠️ Tech Stack
Language: Python 3

Libraries Used:

os – Interact with the operating system
shutil – Move files between directories
pathlib – Modern file path handling
logging – Track file operations
argparse – Command-line interface

📦 Installation
1. Clone this repository:
bash- git clone https://github.com/yourusername/file-organizer.git
bash- cd file-organizer
2. Ensure Python 3 is installed:
python --version

🚀 Usage
To organize a folder, run the script using:
bash- python organizer.py --path /path/to/your/folder

Optional: You can specify a custom log file location:
python organizer.py --path /path/to/folder --log custom_log.log

🧪 Example
Given a cluttered Downloads/ folder:
bash- python organizer.py --path ~/Downloads

📁 After execution, the structure will look like:
Downloads/
 ┣ Documents/
 ┃ ┗ resume.docx
 ┣ Images/
 ┃ ┗ photo.jpg
 ┣ Videos/
 ┃ ┗ demo.mp4
 ┣ Programming/
 ┃ ┗ script.py
 ┣ Others/
 ┃ ┗ unknown.xyz

📓 Logging
A .log file will be created to track all file movements:
2025-05-27 11:15:00 - INFO - Moved 'resume.docx' to 'Documents/'
2025-05-27 11:15:01 - WARNING - Skipped 'photo.jpg' (already exists in 'Images/')
2025-05-27 11:15:02 - ERROR - Error moving 'demo.mp4': [Errno 13] Permission denied

💡 Future Enhancements
1. Integrate GUI using Tkinter or PyQt
2. Add support for file size or creation date filters
3. Enable periodic scheduling (e.g., via cron or Task Scheduler)
4. Add test coverage using unittest or pytest

🙌 Contributions
This project was developed collaboratively. Contributions to improve functionality, readability, or scope are welcome. Fork the repo and submit a pull request!

