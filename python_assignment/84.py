import os
import time
def get_file_dates(file_path):
    try:
        creation_time = os.path.getctime(file_path)
        modification_time = os.path.getmtime(file_path)

        creation_time_readable = time.ctime(creation_time)
        modification_time_readable = time.ctime(modification_time)

        return creation_time_readable, modification_time_readable
    except FileNotFoundError:
        return "File not found."

file_path = 'source_file.txt'
creation_date, modification_date = get_file_dates(file_path)

print(f"Creation Date: {creation_date}")
print(f"Modification Date: {modification_date}")
