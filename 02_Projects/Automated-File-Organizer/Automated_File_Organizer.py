from pathlib import Path
import shutil

# Ask user for folder path
folder_path = input("Enter the folder path to organize: ")

folder = Path(folder_path)

# File type categories
file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"]
}

# Loop through files in the folder
for file in folder.iterdir():

    # Skip folders
    if file.is_file():

        moved = False

        # Check file type
        for category, extensions in file_types.items():

            if file.suffix.lower() in extensions:

                target_folder = folder / category
                target_folder.mkdir(exist_ok=True)

                shutil.move(str(file), str(target_folder / file.name))

                print(f"Moved {file.name} → {category}/")
                moved = True
                break

        # If file type not found
        if not moved:
            other_folder = folder / "Others"
            other_folder.mkdir(exist_ok=True)

            shutil.move(str(file), str(other_folder / file.name))

            print(f"Moved {file.name} → Others/")

print("File organization completed.")