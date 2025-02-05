import os
import shutil

# Define the folder to organize
source_folder = r"C:\Users\samit\OneDrive\Documents"

# Define file categories and their corresponding extensions
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".bat"],
}

# Create subfolders if they don't exist
for category in file_types.keys():
    folder_path = os.path.join(source_folder, category)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files to their respective folders
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    # Ensure it's a file, not a folder
    if os.path.isfile(file_path):
        for category, extensions in file_types.items():
            if file.lower().endswith(tuple(extensions)):
                destination_folder = os.path.join(source_folder, category)
                shutil.move(file_path, destination_folder)
                print(f"Moved {file} to {destination_folder}")
                break  # Stop checking once a match is found

print("File organization complete!")