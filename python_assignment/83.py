import os

def find_txt_files(directory):
    txt_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                txt_files.append(os.path.join(root, file))
    return txt_files

directory_path = '/home/shivam/python_classwork/python_assignment'
txt_files = find_txt_files(directory_path)

print("Text files found:")
for txt_file in txt_files:
    print(txt_file)
