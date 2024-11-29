import os
def get_file_size(file_path):
    try:
        size = os.path.getsize(file_path)
        return size
    except FileNotFoundError:
        return "File not found."

file_path = 'source_file.txt'
file_size = get_file_size(file_path)

if isinstance(file_size, int):
    print(f"The size of the file is: {file_size} bytes")
else:
    print(file_size)
