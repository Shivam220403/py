from datetime import datetime
date_string = "2024-09-22 15:30:00"
date_format = "%Y-%m-%d %H:%M:%S"

date_time_obj = datetime.strptime(date_string, date_format)

print("Original String:", date_string)
print("Converted to datetime object:", date_time_obj)
