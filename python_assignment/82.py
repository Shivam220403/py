def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        return "File not found."

file_path = 'source_file.txt'
line_count = count_lines_in_file(file_path)

print(f"The number of lines in the file is: {line_count}")
