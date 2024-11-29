def bytes_to_string(byte_data):
    return byte_data.decode('utf-8')

byte_data = b'\x31\x32\x33\x34\x35'
converted_string = bytes_to_string(byte_data)

print("Converted string:", converted_string)
