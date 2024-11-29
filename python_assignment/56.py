import shutil

source = "source_file.txt"
destination = "copied_file.txt"

try:
    shutil.copy(source, destination)
    print("File copied successfully!")
except FileNotFoundError:
    print("Source file not found!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print(f"An error occurred: {e}")
