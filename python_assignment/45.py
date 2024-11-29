import hashlib


def get_file_hash(file_path, algorithm='sha256'):
    # Create a hash object based on the chosen algorithm
    hash_obj = hashlib.new(algorithm)

    # Open the file in binary mode
    with open(file_path, 'rb') as file:
        # Read the file in chunks to handle large files
        while chunk := file.read(8192):
            hash_obj.update(chunk)

    # Return the hexadecimal digest of the hash
    return hash_obj.hexdigest()


# Example usage
file_path = "/home/shivam/Pictures/Screenshots/Screenshot from 2024-09-02 17-35-42.png"  # Replace with your file path
file_hash = get_file_hash(file_path, 'sha256')  # You can change 'sha256' to 'md5', 'sha1', etc.

print(f"The SHA-256 hash of the file is: {file_hash}")
