def get_file_extension(filename):
    return filename.split('.')[-1] if '.' in filename else None


filename = "example_document.pdf"
extension = get_file_extension(filename)

if extension:
    print(f"The file extension is: {extension}")
else:
    print("No extension found in the file name.")
